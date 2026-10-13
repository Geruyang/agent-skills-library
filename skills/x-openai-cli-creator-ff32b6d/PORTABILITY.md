# 迁移记录

来源：`upstream/openai/skills`

原名称：`cli-creator`

原始副本位于导出包 `original-skills/x-openai-cli-creator-ff32b6d`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。替换执行者身份和个人技能安装路径，保留 API/CLI 契约以及 codex 示例频道值；补可验证技能目录与 workspace 暂存分支。
- 阅读证据：`SKILL.md` (166 行), `agents/openai.yaml` (4 行), `references/agent-cli-patterns.md` (154 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：可用 shell 与 Rust/Node.js/Python 工具链；已授权 PATH/技能安装目录；目标服务 API 与凭据按需提供。
- 保留的真实产品/API/URL：OpenAI、Cursor、Expo。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
