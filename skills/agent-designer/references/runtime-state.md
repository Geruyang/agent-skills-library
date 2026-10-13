# 运行、编排与状态

源码依据：Pi `packages/agent/src/agent-loop.ts`；Goose `crates/goose/src/agents/state_machine/mod.rs`；anomalyco OpenCode `packages/core/src/session/run-coordinator.ts`；OpenHands SDK `conversation/state.py`；Agents SDK 的 `run_state.py` / `runState.ts`；a13n `docs/a13n-harness/agents-and-runs.md`。完整路径和 hash 见 [来源目录](source-index.json)。

## 拓扑不等于可靠性

| 拓扑 | 适用 | 关键契约 |
|---|---|---|
| 单循环 | 同一上下文即可完成，大多数原型起点 | 最大步数/费用、工具结果配对、停止原因 |
| 固定工作流 | 步骤可预知、审计或恢复要求高 | 输入/输出 schema，重试责任、补偿和条件分支 |
| Manager 调 specialist-as-tool | 最终结果需要统一汇总 | 子任务输出格式、期限、错误处理；子 agent 不获得额外权限 |
| Handoff | 当前对话责任转移给另一专业角色 | 明确转交目标和历史过滤；不是隐式并行，也不是函数返回 |
| 独立并行分支 | 可独立读/算，结果可合并 | 文件/数据所有权、并发上限、失败策略与总预算 |

并行写同一工作区不是默认设计。读任务可共享快照；写任务用独立工作区或明确单写者。将 worker 的输出当作待核对结果而不是新授权。多 agent 的价值应由对照单 agent 的成功率、时延、成本证明。

## 最小状态契约

以下是应用层建议，不是假装所有框架有相同 API：

```text
AgentDefinition: definition_version, instructions_ref, output_schema, tool_policy_ref
Run: run_id, thread_id, tenant_id, status, parent_run_id, budget, definition_version
Event: event_id, run_id, sequence, type, time, payload_ref
ToolAttempt: call_id, operation_key, arguments_digest, approval_ref,
             status(planned/authorized/dispatched/succeeded/failed/unknown), result_ref
Checkpoint: schema_version, last_sequence, messages_ref, pending_calls, business_state_ref
Artifact: artifact_id, tenant_id, media_type, storage_ref, digest, retention
```

把消息历史、UI 投影、业务事实、可恢复控制状态分开。保存聊天历史不能证明正在执行的工具可恢复。凭证、活动 socket、文件句柄、审批回调不能序列化进检查点；恢复时通过当前身份重新绑定。

同一 thread 的写入必须串行化或采用乐观版本检查。OpenCode coordinator 区分 `interrupt` 接收取消与最终 cleanup settlement：API 返回“取消已接受”时 UI 不能立即宣称资源释放。Goose 对整批 tool request/result 配对，不能因末尾已有一个 tool result 就误认为整批完成。OpenHands 把 IDLE 与 FINISHED/ERROR/STUCK 分开，初次连接的 idle 不是任务完成。

## 恢复设计

1. 请求被接受时记录业务 operation key 和目标 run；重复提交返回已有 run 或显式创建新 run。
2. 外部工具 dispatch 前保存 intent；返回后保存 receipt。若进程在中间失联，将 attempt 标为 unknown，先用服务端查询/幂等键对账，再决定重试。
3. 消费端按 event_id/sequence 去重；重连从游标或完整 snapshot 继续。snapshot 与 delta 明确先后，不拼接两个 run 的流。
4. 恢复时重新检查身份、工具定义版本、审批范围、工作区状态和预算；旧许可不能无条件授权已改变的参数。
5. 分开 provider transport retry、模型格式修复、工具业务重试、worker 重启。只给一个层负责同类重试，设置总 deadline 和累积上限。

不要声称通用 exactly-once。可实现的是在业务提供幂等/事务支持时避免重复副作用；否则需要对账和补偿。Git checkpoint、消息回放、模型断线重试互不替代。

## 上下文压缩与预算

在调用模型前使用显式预算，给工具 schema、检索资料、输出保留空间。压缩保持未完成 tool call/result 对、用户约束、待审批动作、证据引用和产物路径。压缩摘要是派生信息；业务事实仍由数据库/文件系统确认。

总预算需聚合 root、children、重试、compaction 和外部工具成本。a13n 当前快照的 inline child 使用独立 usage accumulator，父限制不是整树总限额；应用要做预留与结算。模型或 tokenizer 的估计不能替代提供方实际 usage；缺失费用标 unknown。

## 可实现的退出条件

成功以输出契约和业务验收判定，不仅是模型说“完成”。区分 completed、failed、cancelled、suspended/needs_input、budget_exhausted。工具反复产生相同无进展输出时保存诊断并结束或请求必要输入；不要无限循环。完成时清理 owned 资源；共享 MCP transport/环境由其 owner 清理。
