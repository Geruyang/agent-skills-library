# 迁移记录

来源：`upstream/openai/plugins`

原名称：`omniverse-usd-performance-tuning`

原始副本位于导出包 `original-skills/x-openai-omniverse-usd-performance-tuning-85bd106`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
tools:
- Read
- Shell
- Write
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `reviewed-unchanged`. Retained historical host metadata and conditional invocation examples; USD workflow is independent of the executing agent host.
- Static evidence: read the complete SKILL.md (272 pre-review lines) and all 2 manifest host matches; inspected files: `SKILL.md`, `references/upstreams/usd-optimize.md`, `references/usd-structure-assessment/references/apply-restructure/README.md`.
- Remaining dependencies:
  - OpenUSD/Omniverse and referenced optimization tooling/assets
  - Version-compatible Python/native USD environment and authorized scene access
- Retained product/API references: OpenAI, Claude Code, Claude, OpenUSD, Omniverse, NVIDIA, Codex.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
