# 迁移记录

来源：`upstream/openai/plugins`

原名称：`subagent-driven-development`

原始副本位于导出包 `original-skills/x-openai-subagent-driven-development-776947c`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `reviewed-unchanged`. Reviewed complete skill and relevant local resources; no current-host-only binding requiring a body rewrite was found. Preserved domain workflow and constraints.
- Static evidence: read the complete SKILL.md (574 pre-review lines) and all 0 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Verified subagent dispatch/lifecycle and independent reviewer capabilities
  - Repository worktrees, test tools and original authorization/review gates
- Retained product/API references: OpenAI.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
