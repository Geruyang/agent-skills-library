# 迁移记录

来源：`upstream/openai/plugins`

原名称：`shopify-payments-apps`

原始副本位于导出包 `original-skills/x-openai-shopify-payments-apps-99d89d4`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `adapted`. Replaced assumed bash tool with discovered Node execution or verified Shopify MCP/API equivalents; unavailable search/validation is explicit.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Node.js supporting bundled scripts, or equivalent discovered Shopify search and schema-validation capabilities
  - Network access to Shopify documentation; bundled payments-apps schema asset
  - Payment-provider authentication/compliance for actual API operations; instrumentation privacy/opt-out rules remain
- Retained product/API references: Shopify Payments Apps API; shopify.dev/mcp/usage; Claude Code/Claude Desktop/Cursor in bundled validator catalog metadata.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
