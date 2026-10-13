# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ideate`

原始副本位于导出包 `original-skills/x-openai-ideate-d6e955f`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。图像创意工作流将强制内置 Image Gen 改为实际可验证生成能力；无能力时只交付提示/规格，不声称图片完成。
- 阅读证据：`SKILL.md` (197 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：真实图像生成/编辑 MCP/API 和参考图；可用时的 Product Design 模板/显示能力；提供商权限及费用授权。；原相对资源链接待根任务统一解析：../../references/critical-overrides.md, ../index/SKILL.md, ../user-context/SKILL.md
- 保留的真实产品/API/URL：OpenAI、Figma、Canva、Google。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
