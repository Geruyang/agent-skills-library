# 迁移记录

来源：`upstream/openai/plugins`

原名称：`visualize-data`

原始副本位于导出包 `original-skills/x-openai-visualize-data-fe600a7`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `adapted`. Removed asserted native-renderer availability and private-host persistence paths; preserved output choices with verified rendering/local fallback.
- Static evidence: read the complete SKILL.md (174 pre-review lines) and all 0 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Reviewed data and visualization/runtime dependencies
  - Actually surfaced native/MCP renderer or static Matplotlib/local HTML fallback
- Retained product/API references: OpenAI, Temporal.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.

## Independent audit correction: AUDIT-007 (2026-10-12)

- Outside Work Mode, Data Analytics MCP widgets are preferred only after capability discovery confirms an available renderer that supports the chart. Unavailable, failed, or unsupported native/MCP rendering permits a reproducible static/local chart with visual inspection; a compact table is the last fallback when no visual renderer can be delivered.
- The delivery-path and implementation rules now share this fallback condition. An MCP success result alone does not establish that the chart rendered. Explicit output choices and the canonical artifact contract and packaged portable builder for HTML reports and dashboards remain required.
- Verification: re-read both routing sections and the MCP invocation rule, parsed the entry frontmatter, and confirmed the HTML builder and data/visual QA requirements remain present. No chart-generation workflow was executed during this documentation correction.
