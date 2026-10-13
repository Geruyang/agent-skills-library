---
name: agent-foundation
description: 使用 Converge Agent Foundation（a13n）设计和开发 agent 系统，选择 Harness 嵌入、Service 自托管或 Harness UI；实现工具与 MCP、状态恢复、执行环境、插件及离线测试。用于该框架的集成、源码开发与排错。
---

# Agent Foundation（a13n）

依据真实源码和当前任务选择集成边界。此技能在 ChatGPT/Codex、TRAE、Claude Code 等支持 SKILL.md 的客户端使用；不依赖某个客户端专属工具名称。技能安装不等于框架运行时已安装。

## 选择入口

- 应用自己管理持久化、凭证及恢复策略：使用 `a13n-harness`，通过 `AgentSpec` 与 `HarnessBuilder` 构建可重复执行的 agent。
- 需要组织/工作区、API、托管 agent、持久执行和 Console：使用 Service。其 SDK 位于独立仓库，不要把 Harness 当作 Service HTTP SDK。
- 需要交互体验模型、工具和环境：使用 `a13n-harness-ui` 的 TUI 或 WebUI。

具体实现先读 [references/integration.md](references/integration.md)。修改源码、定位契约或测试入口时读 [references/source-map.md](references/source-map.md)。版本和许可证见 [references/provenance.json](references/provenance.json) 与 [LICENSE](LICENSE)。引用的源代码快照为 `136cb59eb1a7fa778ff640bd23d2cc0a0a58d1e1`；更新后重新核对 API 和锁文件。

## 关键实现约束

1. 本地仓库优先定位当前项目的 `code/converge-ai-labs/agent-foundation`；换机时先查实际路径，缺失则克隆 provenance 中的仓库并检出对应提交。不要依赖原电脑绝对路径。
2. `AgentSpec` 放可序列化定义；稳定行为放定义或 builder；当前身份、调用策略、临时凭证和 MCP 投影放新的 `RunBindings`。不要把活动客户端、密钥和环境句柄写入可移植状态。
3. `run()` 产生新 run；传 `previous_state=first.state` 才继续同一 Harness Thread。保存 `HarnessState` 后，恢复时仍须重建凭证和环境资源。Service 的持久执行机制与嵌入库的应用恢复责任不同。
4. streaming 使用异步上下文管理器，检查结果事件/状态，并在取消或提前退出时释放资源。
5. Capability 的存在不等于动作获得授权。沿用用户请求范围及运行时权限；安装技能不授权部署、外部发送、密钥操作或仓库发布。
6. MCP 静态连接用原生 `MCP`；每次 run 动态身份请求头用 `ContextualMCP`。共享已进入的客户端时每个 run 创建新的工具投影。工具调用成功不代表客户端支持 MCP Apps 的交互渲染；分别验证协议结果和可见 UI。
7. 首先跑不需账号的 `FunctionModel` 离线路径，再按任务测试真实模型、远程环境或账号业务。没有实际测试的功能明确标为未验证。

## 交付

给出选定入口、实际修改、运行前提、验证命令与观察结果。仅复制技能到客户端无需启动服务；任务明确要求部署/运行时才执行对应操作。保留项目与客户端现有配置。
