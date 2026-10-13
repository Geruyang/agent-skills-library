# 迁移记录

来源：`upstream/openai/skills`

原名称：`security-best-practices`

原始副本位于导出包 `original-skills/x-openai-security-best-practices-41b67ae`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Removed incidental reviewer-host branding; retained security guidance unchanged.
- Static evidence: read the complete SKILL.md (92 pre-review lines) and all 1 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Repository code and language/framework reference guidance
  - Project-appropriate verification tools; no dedicated agent-host API required
- Retained product/API references: OpenAI.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
