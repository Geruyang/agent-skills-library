# Agent Foundation 的三个入口

来源 `converge-ai-labs/agent-foundation`，提交 `136cb59eb1a7fa778ff640bd23d2cc0a0a58d1e1`，Apache-2.0。本次另外生成的 `export/custom-skills/agent-foundation` 可作为深入入口，但本文件自包含关键边界，不依赖该技能已安装。

## 选择

- **Harness**：嵌入 Python 应用，基于 Pydantic AI 的 canonical loop，增加统一工具边界、上下文/模型生命周期、环境、能力和观测。不是另写一个独立模型循环。
- **Service**：自托管 API、组织/工作区、资源、agent 和持久执行。部署引入 PostgreSQL、Redis、worker/执行环境；外部 Service SDK 在独立仓库，不把 Harness 当 HTTP SDK。
- **Harness UI / Console**：前者给开发者 TUI/WebUI 试验环境，后者服务平台管理和观察。界面存在不证明生产业务流程已验证。

## 定义、构建、每次运行

`AgentSpec` 保存可移植配置；`AgentDefinition` / `HarnessBuilder.build` 固定模型、输出契约、能力、插件和子 agent 拓扑。每次 root、resume、child run 都创建新 `RunBindings`，注入身份、环境、当前策略、模型 resolver 和临时凭证。不要保存或跨租户复用 live bindings。

`run()` 返回的 status 包含 completed、suspended、failed、cancelled。`output_or_raise()` 适合仅接受完成结果的调用；审批场景显式处理 suspended 与 deferred。`previous_state=...` 才继续之前的 thread，新 run 有新 run_id；fork 创建新的独立历史。

`stream()` 必须放在异步上下文管理器里；单次进入、单消费者，消费终态后才知道 cleanup 结果。`export_state()` 给安全边界状态，不是外部副作用的事务日志。宿主负责进程丢失后的持久重启和结果对账。

## 能力与 MCP

定义层选择稳定 capability；运行绑定只放当前身份/策略和所支持的临时资源。静态 MCP 使用 `MCP`；动态请求头、短时凭证和上下文工厂使用 `ContextualMCP`。共享进入后的 transport 也要为每个 run 生成新的工具投影。

本地 MCP 工具经过统一函数结果边界，默认截断过大结果；该限额发生在客户端收到结果之后，不是网络下载/内存限制。provider-native MCP 不经过本地函数工具边界。做安全和计费设计时分别处理两条执行路径。

默认 request_limit 与重试不是整个 agent 树预算。output contract 不能每 run 任意改变；`with_updates` 替换顶层字段，不自动递归合并模型设置。模型 transport retry、自愈历史修复、run 内断线恢复与宿主持久恢复各有 owner；不会因此获得 exactly-once。

## 源码与验证入口

| 主题 | 资源根相对路径 |
|---|---|
| 运行定义和状态 | `code/converge-ai-labs/agent-foundation/docs/a13n-harness/agents-and-runs.md` |
| MCP 和代理发现 | 同仓库 `docs/a13n-harness/mcp.md`、`tool-proxy.md` |
| 嵌入持久化例子 | `examples/agent-app/` |
| 离线测试 | 例子和测试中的 `FunctionModel`；先按例子 README 安装依赖 |
| Service | `packages/a13n-service/`、`docs/a13n-service/`、`deploy/docker/compose/` |
| 环境 | `docs/environments/`、`crates/a13n-envd/`、`packages/a13n-envd-client/` |
| 事件/UI | `packages/a13n-stream-protocol/`、`frontend/apps/a13n-harness-ui/`、`frontend/apps/a13n-console/` |

本次设计整合没有安装并运行整个框架。未来先执行无需凭证的 FunctionModel 切片，再验证真实模型、远程环境、Service 恢复和 UI；分别报告。Python/Node/pnpm 与发布耦合按目标 commit 的项目文件，不沿用个人电脑路径或旧全局版本。
