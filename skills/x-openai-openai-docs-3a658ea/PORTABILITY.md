# 迁移记录

来源：`upstream/openai/skills`

原名称：`openai-docs`

原始副本位于导出包 `original-skills/x-openai-openai-docs-3a658ea`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。保留 OpenAI/Codex 产品教程、模型名及官方链接；改为实际文档能力发现，移除普通查询时自动安装 Codex MCP 与固定 eval 路径。
- 阅读证据：`SKILL.md` (172 行), `agents/openai.yaml` (14 行), `references/latest-model.md` (36 行), `references/upgrade-guide.md` (181 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：官方 OpenAI 文档搜索/获取或受限官方域浏览；可选 Node.js 与允许的缓存目录；Codex 安装命令仅用于明确 Codex 配置请求。
- 保留的真实产品/API/URL：Codex、OpenAI、ChatGPT、Google、Expo、https://developers.openai.com/api/docs/guides/latest-model.md、https://developers.openai.com/codex/codex-manual.md、https://developers.openai.com/mcp。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
