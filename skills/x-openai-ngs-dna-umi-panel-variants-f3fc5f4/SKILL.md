---
name: x-openai-ngs-dna-umi-panel-variants-f3fc5f4
description: Run or plan targeted DNA panel variant workflows that use UMIs, duplex consensus reads, molecular barcodes, low-frequency calling, target coverage, and panel-specific QC.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## Reviewed capability mapping (TRAE / Claude)

The commands below reference shared `plugins/ngs-analysis/scripts/` runners that are not bundled in this standalone skill. Locate the installed ngs-analysis package and resolve its scripts before executing. If absent, report runner execution as blocked and produce a workflow plan; use a documented equivalent pipeline only after validating its toolchain, reference resources, and the same QC gates. Do not mark biological outputs complete based only on a planned command.

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# UMI Panel DNA Variants

Use this skill for targeted DNA panels where molecular barcodes, UMIs, duplex consensus, or low-frequency allele detection are central to the analysis. If the panel is ordinary germline calling without molecular consensus, use `ngs-dna-germline-variants`.

## Essential Inputs

Confirm:

- panel/capture kit name and target BED
- UMI layout: inline read, index read, single UMI, duplex UMI, or unknown
- whether consensus reads have already been generated
- FASTQ/BAM input and pairing convention
- reference build and panel-specific annotation requirements
- minimum allele fraction goal and intended use: screening, research, validation, or exploratory
- positive/negative controls and expected spike-ins when available

## Route

Use a lab-validated panel workflow when provided. For public-tool planning, combine FASTQ QC, UMI extraction/consensus generation, alignment, target coverage QC, and variant calling as separate audited stages.

Preflight command:

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline dna_umi_panel_variants --emit-install-plan
```

For compact local checks from prepared consensus or alignment BAM/CRAM files, use the dedicated UMI panel runner:

```bash
python plugins/ngs-analysis/scripts/run_dna_umi_panel_variants.py \
  --sample-sheet umi_panel_samples.tsv \
  --reference-fasta reference.fa \
  --target-bed panel_targets.bed \
  --umi-mode duplex \
  --umi-tag RX \
  --execute
```

This writes the consensus/variant command plan, molecular-consensus state, low-frequency calling settings, visualization index, `qc/umi_postrun_summary.{tsv,json}`, `qc/umi_molecular_evidence_contract.{tsv,json}`, and consensus-BAM VCF outputs when the local fgbio/samtools/bcftools backend is available. The post-run summary parses consensus flagstat, target coverage, bcftools stats, and family-size/duplex files when present; missing metrics stay explicit in the notes column. The molecular evidence contract keeps the low-AF review requirements visible per sample: consensus BAM, family-size or molecule-support metrics, variant stats, hotspot review, and duplex review.

The direct runner also emits `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. The resource check is advisory by default so custom or reduced references can still be planned; add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when missing registered reference bundles should block readiness.

## Decision Points

- Do not trim or discard UMI bases until their layout and destination are known.
- Separate raw read depth from unique molecular depth and consensus depth.
- Track on-target rate, coverage uniformity, family size distribution, strand/duplex support, and per-target dropout.
- Low allele fraction calls require stronger artifact review than ordinary germline calls.
- Use panel-specific hotspot/blacklist rules only when their provenance is known.

## Outputs

Produce:

- UMI layout and consensus strategy
- target BED/resource manifest
- raw-depth, molecular-depth, and consensus-depth QC summary
- `qc/umi_postrun_summary.tsv` for consensus reads, target coverage, variant counts, family size, and duplex fraction
- `qc/umi_molecular_evidence_contract.tsv` for low-AF evidence readiness, hotspot review, and duplex review expectations
- variant calls with allele fraction, depth, strand/duplex support, and filtering rationale
- limitations around sensitivity, panel dropout, molecule count, and non-validated interpretation
