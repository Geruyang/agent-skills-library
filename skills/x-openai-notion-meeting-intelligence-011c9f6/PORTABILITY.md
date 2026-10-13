# 迁移记录

来源：`upstream/openai/skills`

原名称：`notion-meeting-intelligence`

原始副本位于导出包 `original-skills/x-openai-notion-meeting-intelligence-011c9f6`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Removed Codex-only Notion setup and research branding; added actual connector/API discovery and local agenda fallback.
- Static evidence: read the complete SKILL.md (66 pre-review lines) and all 33 manifest host matches; inspected files: `SKILL.md`, `evaluations/README.md`, `evaluations/decision-meeting-prep.json`, `evaluations/status-meeting-prep.json`, `examples/customer-meeting.md`, `examples/executive-review.md`, `reference/template-selection-guide.md`.
- Remaining dependencies:
  - Authenticated Notion MCP/API with correct workspace read/write permissions
  - Research retrieval or user-provided evidence; local Markdown output fallback
- Retained product/API references: Codex, OpenAI, Notion.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
