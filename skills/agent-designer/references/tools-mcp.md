# 工具、MCP 与客户端适配

## 先定义工具契约

一个工具应说明何时调用、必需输入、单位与枚举、输出 schema、错误类型、副作用和分页/大小限制。把面向用户的操作与内部 API 拆分：模型传业务标识，身份和租户从宿主注入。schema 校验后还要做资源级授权。写工具返回可查询 receipt；不把“请求已接受”写成“任务已完成”。

不为每个 REST endpoint 暴露一个模型工具。多个操作可按业务能力合并，但避免万能 `execute(anything)` 让授权无法检查。确需 shell/code execution 时视作高能力工具，使用独立环境边界。

## 四类协议不要混用

| 协议/格式 | 责任 | 不提供的保证 |
|---|---|---|
| MCP | 工具、资源、提示模板及协议能力协商 | 不自动提供业务授权、UI 渲染或可靠调度 |
| Agent Skills | 任务知识与渐进加载资源 | 不安装运行时、不赋予工具权限 |
| AG-UI | agent 与用户应用之间的事件、状态和交互 | 不替代 agent loop 或安全边界 |
| 客户端/插件私有格式 | 声明安装、指令、hooks、连接装配 | 不保证其他客户端支持相同字段 |

MCP TypeScript SDK 下载快照 main 是 v2 分包（`@modelcontextprotocol/server` / `client`），旧 `@modelcontextprotocol/sdk` 属于 v1 分支。参考服务器和插件可能固定不同主版本；按每个 lockfile 和 import 检查，不全局替换。旧 SSE 与 Streamable HTTP 的 URL/生命周期也需按服务器实况选择。

stdio 服务把 stdout 留给协议，日志到 stderr；关闭客户端时清理子进程。HTTP 服务校验请求身份、origin/session 和访问范围；连接恢复不绕过授权。会话标识不是用户身份证明。

## 大目录：发现、schema、调用

本次语料中 667 个技能、45 个 MCP 配置定义（43 个去重 endpoint/launch）说明全量提示词装载不可取。可采用：

1. 轻量分类/搜索，返回有界候选名称、用途、来源和前提。
2. 入选后返回完整原始 schema、必要说明和版本。
3. 调用时做 allowlist、参数验证、身份/资源检查、限流，保留原始结构化结果、媒体和资源引用。

导出 `trae_gateway.mjs` 采用 `discover_tools → get_tool_schema → call_tool`；这是本次客户端适配，不是 MCP 标准的新协议。必须保存上游工具指导信息、原始结果与资源 URI；不要为了缩短文本破坏审批/工具参数语义。a13n ToolProxy 同样减少模型上下文，不意味着省去底层初始化和 list_tools 成本。

## 按需选择下载目录

用 [mcp-index.json](mcp-index.json) 或查询脚本查候选：保留 source、launch/endpoint 类型、历史状态、前提，不携带凭证。索引既包含 45 个上游配置定义，也列出本次本地实现的独立记录，重叠不可相加当作独立服务数。

七个 reference servers：everything、filesystem、fetch、git、memory、sequentialthinking、time。它们是协议和实现参考，仓库 README 明确不把参考实现当生产方案。memory 的图存储不等于完整企业记忆；sequentialthinking 的步骤记录不证明模型准确率提升。

另有来自下载插件的图表/可视 UI 与本地服务、远程 SaaS 连接定义。账号凭证、macOS/Xcode、Bun、机器人授权、项目初始化等前提分别处理；下载一个 `.mcp.json` 不等于下载其 SaaS 后端源码。

## 验证梯度

1. 配置解析和 scope：只启用选中的来源，路径/环境变量可移植。
2. initialize 与 tools/list：协议可连接，检查 timeout/取消/退出。
3. fixture 业务调用：schema 正确，真实工具产生符合预期的输出。
4. 账号业务调用：用户权限、真实资源和副作用按授权验证。
5. 客户端体验：文本、图片、资源和交互 UI 分别实际展示。

历史报告提供 16 个本地握手、20 个 Claude 连接等证据；没有提供全部账号业务成功。TRAE 网关已验证真实图表 renderer → PNG 与预览交付，但 `native_mcp_apps_embed=false`。静态图片兼容不是原生 MCP Apps 交互兼容，不能合并为“全部 UI 正常”。
