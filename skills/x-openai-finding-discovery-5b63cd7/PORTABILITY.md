# 迁移记录

来源：`upstream/openai/plugins`

原名称：`finding-discovery`

原始副本位于导出包 `original-skills/x-openai-finding-discovery-5b63cd7`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Removed irrelevant host restriction while retaining real Codex Security helper/API names and gated live tool use.
- Static evidence: read the complete SKILL.md (165 pre-review lines) and all 3 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Repository evidence and Codex Security plugin helpers or discovered scan tools
  - External plugin helpers are not implied to be bundled in this standalone skill
- Retained product/API references: Codex, OpenAI.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
