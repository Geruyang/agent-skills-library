# 源码导航

固定提交：136cb59eb1a7fa778ff640bd23d2cc0a0a58d1e1。

| 任务 | 优先阅读 |
| --- | --- |
| 嵌入执行与定义 | packages/a13n-harness/a13n_harness；docs/a13n-harness/getting-started.md、agents-and-runs.md |
| 状态保存和重启 | examples/agent-app/README.md、源码和测试 |
| 工具、MCP、运行绑定 | docs/a13n-harness/mcp.md、capabilities.md、model-authentication.md |
| 环境与沙箱 | docs/environments；examples/environment-provider；crates/a13n-envd；packages/a13n-envd-client |
| 扩展和 provider | examples/plugins、examples/provider-plugin |
| 交互 MCP Apps | examples/mcp-apps；先读 README 并按其 Node/npm 构建步骤执行 |
| 自托管 API、资源、恢复 | packages/a13n-service；docs/a13n-service；deploy/docker/compose |
| TUI/WebUI | packages/a13n-harness-ui；frontend/apps/a13n-harness-ui；docs/a13n-harness-ui |
| Console | frontend/apps/a13n-console；frontend/packages/a13n-ui |
| AG-UI 事件适配 | packages/a13n-stream-protocol；docs/a13n-stream-protocol |

修改仓库前读取其 AGENTS.md、CONTRIBUTING.md、DEVELOPMENT.md；架构契约从 spec/README.md 导航。不要把仓库内部的贡献流程施加到与该仓库无关的用户项目。

源码开发 Python 3.13、uv、Make；前端需要 Node.js 24 与固定 pnpm，Service 开发需要 Docker。按变更组件运行贡献文档对应的检查。`make examples-check-all` 是完整例子门禁；局部开发优先各例子 README。

发布版本耦合：Harness/Stream Protocol 同版本且后者精确依赖前者；Envd/其 Python client 同版本；UI、Service、Logging 独立发布。不要仅靠包名推断兼容版本。

无法读取本地源码时使用固定版本文档：
https://github.com/converge-ai-labs/agent-foundation/tree/136cb59eb1a7fa778ff640bd23d2cc0a0a58d1e1/docs
