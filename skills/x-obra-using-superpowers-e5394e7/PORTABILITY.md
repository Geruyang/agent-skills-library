# 迁移记录

来源：`upstream/obra/superpowers`

原名称：`using-superpowers`

原始副本位于导出包 `original-skills/x-obra-using-superpowers-e5394e7`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Scoped runtime mapping to discovered host tools and corrected unconditional fork/model assumptions without removing genuine Codex configuration examples.
- Static evidence: read the complete SKILL.md (71 pre-review lines) and all 11 manifest host matches; inspected files: `SKILL.md`, `references/codex-tools.md`, `references/gemini-tools.md`, `references/muse-tools.md`.
- Remaining dependencies:
  - Current host skill discovery and file access
  - Verified subagent lifecycle/model schemas where selected workflows require agents; runtime reference tables may be version-specific
- Retained product/API references: Codex, Claude Code, Claude, Gemini, Pi, Copilot.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
