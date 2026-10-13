# 迁移记录

来源：`upstream/openai/skills`

原名称：`notion-knowledge-capture`

原始副本位于导出包 `original-skills/x-openai-notion-knowledge-capture-13db9c0`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：Notion MCP 连接与 OAuth 使用当前宿主文档流程；移除必须运行 codex CLI 和重启 Codex 的要求，并明确未连接时只交付草稿。
- 审阅文件：`SKILL.md`、`evaluations/README.md`
- 实际依赖：官方 Notion MCP 与 OAuth、目标工作区权限；Notion 工具名称需从实时 schema 映射。
- 保留的产品/历史名称：Notion、Haiku、Sonnet、Opus 为产品和评测模型名。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
