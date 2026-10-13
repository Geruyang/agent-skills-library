# 迁移记录

来源：`upstream/openai/plugins`

原名称：`index`

原始副本位于导出包 `original-skills/x-openai-index-ad54b55`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Removed asserted native-renderer availability and private-host persistence paths; preserved output choices with verified rendering/local fallback. Mapped analytics plugin listing/install/suppression to actual capabilities with manual/data fallback instead of assumed functions tools.
- Static evidence: read the complete SKILL.md (393 pre-review lines) and all 5 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Analytics source connectors or provided records; companion analysis/reporting skills
  - Verified renderer/structured input/persistence capabilities or portable HTML/static output
- Retained product/API references: Codex, OpenAI, Notion.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.

- Final focused check: Mapped analytics plugin listing/install/suppression to actual capabilities with manual/data fallback instead of assumed functions tools.
