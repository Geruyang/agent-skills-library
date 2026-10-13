---
name: x-openai-ngs-amplicon-microbiome-096852b
description: Kick off public 16S, 18S, ITS, COI, or other marker-gene amplicon microbiome workflows using nf-core/ampliseq, QIIME2, DADA2, and Cutadapt.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Amplicon Microbiome

Use this skill for marker-gene microbiome analysis from amplicon FASTQs.

## Essential Inputs

Confirm:

- marker region: 16S, 18S, ITS, COI, or custom
- primer sequences and orientation
- paired-end or single-end reads
- whether reads should be merged
- taxonomy database and version
- sample metadata
- endpoint: ASV table, taxonomy, diversity, differential abundance, or plots

## Public Defaults

Prefer `nf-core/ampliseq` for reproducible end-to-end runs. Use QIIME2 or DADA2 directly when the user wants notebook-level control or an existing lab protocol requires it.

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline amplicon_microbiome --emit-install-plan
```

## Local Execution Package

For FASTQ intake/QC before primer, ASV, and taxonomy decisions, use:

```bash
python plugins/ngs-analysis/scripts/run_fastq_assay_package.py \
  --lane amplicon_microbiome \
  --sample-sheet amplicon_samples.tsv \
  --execute
```

This validates read paths and structure, runs seqkit stats and FastQC/MultiQC when available, and writes `amplicon_analysis_status.json`. The runner now also emits `methods/amplicon_methods.json` plus a concrete backend handoff bundle under `workflow/` so primer, denoiser, truncation, normalization, and taxonomy choices are machine-readable even before a full backend is run.

If the user asks for a full amplicon analysis rather than QC/readiness, do not treat FASTQs alone as sufficient. Require primer sequences, primer orientation, taxonomy database plus version, and sample metadata before presenting the run as analysis-ready. Without that context, run the local execution package and describe the result as a read-QC/readiness bundle only.

For backend ASV/taxonomy/diversity execution when primers, metadata, and taxonomy resources are available, use:

```bash
python plugins/ngs-analysis/scripts/run_amplicon_microbiome.py \
  --sample-sheet amplicon_samples.tsv \
  --backend qiime2 \
  --primer-forward GTGYCAGCMGCCGCGGTAA \
  --primer-reverse GGACTACNVGGGTWTCTAAT \
  --taxonomy-classifier silva-138-classifier.qza \
  --metadata sample_metadata.tsv \
  --execute
```

Use `--backend dada2` for a direct R/Bioconductor ASV path. The plugin includes `workflows/amplicon_microbiome/run_dada2_backend.R`; the runner checks for `Rscript` and the `dada2` R package before execution, then writes normalized ASV, representative-sequence, read-retention, and optional taxonomy tables under `tables/`.

For nf-core execution, use `plugins/ngs-analysis/scripts/run_nfcore_pipeline.py --pipeline ampliseq`.

The direct backend runner also emits `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. The resource check is advisory by default when a QIIME classifier is supplied directly; add `--bundle-root silva_138_amplicon=<path>`, `--include-optional-resources`, and `--require-resource-plan` when missing registered taxonomy databases should block readiness.

The backend runner writes native normalized tables when QIIME2/DADA2/nf-core outputs are present:

- `tables/asv_table.tsv`
- `tables/representative_sequences.fasta` for direct DADA2 runs
- `tables/taxonomy.tsv`
- `tables/read_retention.tsv`
- `tables/amplicon_backend_summary.json`
- `tables/alpha_diversity.tsv`, `tables/bray_curtis_distance.tsv`, and `tables/top_taxa_or_features.tsv` when a normalized ASV/feature table is available

QIIME2 BIOM-only feature-table exports are recorded as requiring conversion, with a `biom convert` command in the backend summary. Do not claim diversity or taxonomy interpretation unless these normalized tables or equivalent supplied inputs exist.

## Kickoff Pattern

nf-core preflight run:

```bash
nextflow run nf-core/ampliseq \
  -profile test,docker \
  --outdir results/ampliseq_test
```

Before a real run, verify primer trimming and truncation choices from read-quality profiles.

## Visualization Outputs

The local FASTQ package always writes `visualizations/index.html` and `visualizations/visualization_manifest.json`. With only FASTQs, this is a read-QC/readiness bundle. If an ASV/feature table is available, pass it to the runner with `--asv-table` to generate alpha diversity, Bray-Curtis PCoA, and rarefaction artifacts. If a feature taxonomy table is available, pass `--taxonomy-table` to generate taxa barplots. When downstream tables are labeled synthetic or contain sample columns that are not present in the real sample sheet, the runner marks the run review-only and blocks beta-diversity/PCoA unless `--allow-synthetic-diversity` is set explicitly.

The run also emits `qc_verdict.json` and, for amplicon runs, `qc_interpretation.json` with machine-readable reason codes, a readiness verdict, and follow-on command templates for generating ASV/taxonomy tables and re-rendering plugin-native plots. Backend runs additionally write `tables/amplicon_backend_summary.json` so exported ASV, taxonomy, read-retention, and BIOM-conversion status are auditable. When a normalized ASV/feature table is available, the backend runner also writes `tables/amplicon_diversity_summary.json`, `visualizations/amplicon_backend_dashboard.html`, and SVG plots for sample depth, Shannon diversity, and top taxa/features. If the ASV table is absent, these outputs remain explicitly unavailable rather than inferred from FASTQ QC.

## Guardrails

- Do not choose truncation lengths before looking at quality distributions.
- Do not mix taxonomy database versions without recording them.
- Preserve negative controls and extraction blanks in metadata.
