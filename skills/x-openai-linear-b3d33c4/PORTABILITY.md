# 迁移记录

来源：`upstream/openai/skills`

原名称：`linear`

原始副本位于导出包 `original-skills/x-openai-linear-b3d33c4`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。Linear 接入先发现真实连接和 schema；自动 Codex 配置/重启改为明确目标客户端的可选设置，缺少访问时交付本地修改规格。
- 阅读证据：`SKILL.md` (93 行), `agents/openai.yaml` (14 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：已授权 Linear OAuth/MCP 或等价 API/CLI；真实 workspace/team/project；创建和修改仍须任务授权。
- 保留的真实产品/API/URL：Codex、OpenAI、https://mcp.linear.app/mcp。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
