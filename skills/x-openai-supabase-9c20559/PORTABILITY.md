# 迁移记录

来源：`upstream/openai/plugins`

原名称：`supabase`

原始副本位于导出包 `original-skills/x-openai-supabase-9c20559`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `adapted`. Replaced universal .mcp.json assumption with current-host MCP configuration/OAuth discovery and authenticated equivalent CLI/API fallback.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Supabase project access and appropriate credentials
  - Compatible Supabase MCP/OAuth host, Supabase CLI, psql or documented API
  - Network/documentation access; project database and test environment
- Retained product/API references: Supabase; PostgreSQL; https://mcp.supabase.com/mcp; OAuth 2.1; .mcp.json as a conditional host-supported format.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
