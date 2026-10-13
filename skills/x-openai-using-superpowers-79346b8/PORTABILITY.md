# 迁移记录

来源：`upstream/openai/plugins`

原名称：`using-superpowers`

原始副本位于导出包 `original-skills/x-openai-using-superpowers-79346b8`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。按实际宿主选择平台参考；Codex 专章保留为产品教程，但配置/模型参数/应用控件须发现验证，避免其他宿主执行 Codex 配置。
- 阅读证据：`SKILL.md` (69 行), `references/codex-tools.md` (108 行), `references/gemini-tools.md` (63 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：技能发现/读取；可选真实多代理工具及其 schema；Git；Codex 特定配置仅在目标客户端明确且授权时执行。
- 保留的真实产品/API/URL：Codex、OpenAI、Claude。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
