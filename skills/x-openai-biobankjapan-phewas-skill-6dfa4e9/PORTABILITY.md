# 迁移记录

来源：`upstream/openai/plugins`

原名称：`biobankjapan-phewas-skill`

原始副本位于导出包 `original-skills/x-openai-biobankjapan-phewas-skill-6dfa4e9`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：reviewed-unchanged。已静态复审 biobankjapan-phewas-skill 的完整主文档及清单命中文件；保留任务方法、真实产品协议和原约束，未发现需要替换的当前 Codex 宿主硬绑定。
- 阅读证据：`SKILL.md` (47 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：Python、随包查询脚本；BioBank Japan PheWAS 网络访问。
- 保留的真实产品/API/URL：OpenAI。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
