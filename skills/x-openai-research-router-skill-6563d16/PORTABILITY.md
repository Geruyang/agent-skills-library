# 迁移记录

来源：`upstream/openai/plugins`

原名称：`research-router-skill`

原始副本位于导出包 `original-skills/x-openai-research-router-skill-6563d16`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。研究分工依据实际 subagent 能力，保留独立 lane 和证据综合要求。
- 阅读证据：`SKILL.md` (151 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：相应研究数据源/检索能力；可选 subagent 工具，无多代理能力时顺序完成。
- 保留的真实产品/API/URL：OpenAI、Expo、React。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
