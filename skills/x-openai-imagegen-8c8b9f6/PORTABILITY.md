# 迁移记录

来源：`upstream/openai/skills`

原名称：`imagegen`

原始副本位于导出包 `original-skills/x-openai-imagegen-8c8b9f6`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Replaced image tool/path assumptions with capability and returned-artifact discovery; retained explicit-only CLI fallback and OpenAI Image API dependency.
- Static evidence: read the complete SKILL.md (285 pre-review lines) and all 18 manifest host matches; inspected files: `SKILL.md`, `references/cli.md`, `references/codex-network.md`.
- Remaining dependencies:
  - Verified native image-generation/editing and image inspection/export capability
  - Explicitly requested CLI fallback requires Python, OpenAI Image API credentials and network permission
- Retained product/API references: Codex, OpenAI.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
