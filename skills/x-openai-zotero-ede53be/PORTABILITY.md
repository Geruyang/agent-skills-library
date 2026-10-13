# 迁移记录

来源：`upstream/openai/plugins`

原名称：`Zotero`

原始副本位于导出包 `original-skills/x-openai-zotero-ede53be`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Resolved Zotero helper from the installed skill directory and removed irrelevant Codex wording; retained benign internal session label in script.
- Static evidence: read the complete SKILL.md (108 pre-review lines) and all 4 manifest host matches; inspected files: `SKILL.md`, `scripts/zotero.py`.
- Remaining dependencies:
  - Python 3, Zotero Desktop and reachable local API/connector on port 23119
  - Local file access and explicit authorization for library writes
- Retained product/API references: OpenAI, Zotero, Codex.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
