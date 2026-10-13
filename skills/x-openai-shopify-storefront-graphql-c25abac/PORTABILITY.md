# 迁移记录

来源：`upstream/openai/plugins`

原名称：`shopify-storefront-graphql`

原始副本位于导出包 `original-skills/x-openai-shopify-storefront-graphql-c25abac`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Replaced assumed Bash tool with Node process or verified Shopify MCP/API discovery; made missing validation capability explicit.
- Static evidence: read the complete SKILL.md (86 pre-review lines) and all 0 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Node.js and bundled storefront schema or equivalent Shopify search/validation capability
  - shopify.dev network access; preserve instrumentation disclosure/opt-out
- Retained product/API references: OpenAI, Shopify.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
