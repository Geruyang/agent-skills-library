# 迁移记录

来源：`upstream/openai/plugins`

原名称：`airtable-filters`

原始副本位于导出包 `original-skills/x-openai-airtable-filters-5bed075`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-adapted`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：明确filters为Airtable连接器schema，检查实际工具；REST回退需语义正确的filterByFormula转换。
- 尚需能力/资源：认证Airtable连接器或REST；字段及choice元数据。
- 保留产品引用：Airtable filters和filterByFormula协议。
- 文件清单：`SKILL.md`、`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
