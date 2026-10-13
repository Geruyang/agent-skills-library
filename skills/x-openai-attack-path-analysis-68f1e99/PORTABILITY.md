# 迁移记录

来源：`upstream/openai/plugins`

原名称：`attack-path-analysis`

原始副本位于导出包 `original-skills/x-openai-attack-path-analysis-68f1e99`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。移除分析执行者 Codex 身份限制；对真实 Codex Security workbench API 增加 schema/原子持久化发现，缺少能力不伪造候选提交。
- 阅读证据：`SKILL.md` (123 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：原始 findings、每 scan threat model、仓库和共享存储规范；workbench 模式需候选读取及原子 attack-path 写入 API。；原相对资源链接待根任务统一解析：../../references/artifact-storage.md, ../../references/scan-artifacts.md
- 保留的真实产品/API/URL：Codex、OpenAI、Cursor、Expo、Render。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
