# 迁移记录

来源：`upstream/openai/plugins`

原名称：`shopify-polaris-admin-extensions`

原始副本位于导出包 `original-skills/x-openai-shopify-polaris-admin-extensions-f065ad5`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-adapted。
- Removed guaranteed Bash and source-host identity; retained actual Shopify scaffolding and target-aware validation requirements.
- 剩余依赖：Node.js scripts or equivalent Shopify docs/validator;Shopify CLI for scaffolding。
- 保留产品/API引用：Shopify;Polaris;Preact;Claude/Cursor in upstream validator catalog metadata。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流。详情见 `PORTABILITY_REVIEW.json`。
