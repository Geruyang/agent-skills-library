# 迁移记录

来源：`upstream/openai/skills`

原名称：`openai-docs`

原始副本位于导出包 `original-skills/x-openai-openai-docs-265646d`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Made documentation MCP discovery/setup host-dependent while retaining Codex product documentation, model IDs and official URLs.
- Static evidence: read the complete SKILL.md (166 pre-review lines) and all 34 manifest host matches; inspected files: `SKILL.md`, `agents/openai.yaml`, `references/latest-model.md`, `references/upgrade-guide.md`.
- Remaining dependencies:
  - Node.js and optional curl for the bundled manual helper; approved writable cache
  - OpenAI documentation MCP or official-domain retrieval; current public documentation
- Retained product/API references: Codex, OpenAI, Notion.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
