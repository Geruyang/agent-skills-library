# 迁移记录

来源：`upstream/openai/plugins`

原名称：`build-dashboard`

原始副本位于导出包 `original-skills/x-openai-build-dashboard-03f8042`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。将 dashboard 视觉规范的强制 Codex chrome tokens 改为实际宿主 token 映射与独立主题回退；保留原 dashboard schema、数据来源和已存在的 HTML 交付分支。
- 阅读证据：`SKILL.md` (169 行), `specifications/mcp-artifact-dashboard.md` (75 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：权威结构化数据；已发现的 artifact renderer/validator 或 HTML fallback；可选 Sites/BI 连接；共享 analytics runtime 依赖。；原相对资源链接待根任务统一解析：../../src/analytics-app-core.md
- 保留的真实产品/API/URL：OpenAI、ChatGPT、Canva、Render。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
