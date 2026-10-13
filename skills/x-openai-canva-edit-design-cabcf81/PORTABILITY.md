# 迁移记录

来源：`upstream/openai/plugins`

原名称：`canva-edit-design`

原始副本位于导出包 `original-skills/x-openai-canva-edit-design-cabcf81`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：adapted。补充 Canva 编辑能力发现、事务语义核验及无写入能力时的本地编辑规格交付；保留提交审批。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：已授权 Canva 连接及支持草稿、预览、提交、取消的 MCP/API；无该能力时只能交付本地修改规格。
- 保留的真实产品/API/名称：Canva、Canva transaction operation names。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
