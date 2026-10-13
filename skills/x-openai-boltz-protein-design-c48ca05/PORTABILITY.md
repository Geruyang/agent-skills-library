# 迁移记录

来源：`upstream/openai/plugins`

原名称：`boltz-protein-design`

原始副本位于导出包 `original-skills/x-openai-boltz-protein-design-c48ca05`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Mapped long-lived download, status and optional scheduled follow-ups to discovered executor capabilities; retained Boltz API and spending gates.
- Static evidence: read the complete SKILL.md (112 pre-review lines) and all 5 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - boltz-api CLI, authentication, network and explicit per-start spending approval
  - Persistent managed process facility or local downloader handoff; optional authorized scheduler
- Retained product/API references: OpenAI, Claude Code, Claude, Boltz.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
