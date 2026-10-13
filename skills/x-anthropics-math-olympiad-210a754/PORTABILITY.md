# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`math-olympiad`

原始副本位于导出包 `original-skills/x-anthropics-math-olympiad-210a754`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review: batch 6 (2026-10-12)

- Result: `reviewed-unchanged`. Reviewed complete skill and relevant local resources; no current-host-only binding requiring a body rewrite was found. Preserved domain workflow and constraints.
- Static evidence: read the complete SKILL.md (406 pre-review lines) and all 0 manifest host matches; inspected files: `SKILL.md`.
- Remaining dependencies:
  - Task-relevant input files/evidence and the documented product/runtime capabilities
  - File access plus actual discovered tools for execution, inspection or delivery; unavailable steps must be explicit
  - Included scripts/references/assets remain local resources; their presence does not prove runtime dependencies are installed
- Retained product/API references: domain-specific terminology, code examples and source URLs.
- Limits: static portability review only. No source-skill workflow, installer, remote call, credential action, hardware operation or publication was run. Tool/CLI availability, permissions, installed versions and remote access must be verified at use time. If an equivalent capability is absent, report the missing step and provide a local handoff where the original workflow permits one; do not fabricate completion.
