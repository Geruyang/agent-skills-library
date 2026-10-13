# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ngs-amplicon-microbiome`

原始副本位于导出包 `original-skills/x-openai-ngs-amplicon-microbiome-096852b`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `reviewed-unchanged`. No host binding; preserved bioinformatics CLI workflow. Shared plugin scripts are external dependencies, not bundled assets.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Complete ngs-analysis plugin checkout for plugins/ngs-analysis/scripts and workflows/amplicon_microbiome/run_dada2_backend.R; these are absent from this skill directory
  - Python; QIIME2 or Rscript/DADA2 or Nextflow/nf-core/ampliseq; applicable container runtime
  - FASTQs, primer/metadata inputs and versioned taxonomy databases
- Retained product/API references: nf-core/ampliseq; QIIME2; DADA2; Cutadapt.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
- Missing shared runners: resolve the complete plugin root before using its example paths. If unavailable, use verified native nf-core/tool commands within the same scope or deliver a local plan; plugin-specific status/visualization files must not be claimed without actual runner outputs.
