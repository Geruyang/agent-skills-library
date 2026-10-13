# 迁移记录

来源：`upstream/obra/superpowers`

原名称：`writing-skills`

原始副本位于导出包 `original-skills/x-obra-writing-skills-bcb11ab`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 manifest 命中；把个人 skill 路径和孤立子代理测试改为当前宿主目录/能力发现，缺失 fresh-context 测试能力不得冒称测试通过。审阅附属命中区分真实 Anthropic 文档与历史 Claude 场景。
- 正文/支持文件改动：`SKILL.md`。
- 剩余依赖：当前宿主技能目录读取/写入能力；独立上下文子代理或已授权模型 API/CLI 以运行行为测试；Superpowers 配套技能按当前清单定位；Graphviz/Node 为可选渲染依赖。
- 保留引用：Claude Code、Codex、Copilot CLI、Gemini CLI 路径作为条件性产品例子保留；Anthropic 官方指南、Claude 模型及历史 CLAUDE.md 测试材料保留。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
