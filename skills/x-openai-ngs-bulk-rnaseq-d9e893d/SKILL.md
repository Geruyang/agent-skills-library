---
name: x-openai-ngs-bulk-rnaseq-d9e893d
description: Dispatch bulk RNA-seq requests to FASTQ-to-count QC or count-matrix differential-expression skills using nf-core/rnaseq, STAR, Salmon, featureCounts, MultiQC, and R/Bioconductor workflows.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Bulk RNA-seq

Use this skill as the bulk RNA-seq dispatcher. Route FASTQ/BAM processing to count-generation QC, and route count-matrix statistical analysis to differential-expression guidance.

## Essential Inputs

Confirm:

- organism and genome build
- FASTA and GTF, or supported nf-core genome key
- paired-end or single-end reads
- strandedness, or whether to infer strandedness
- sample sheet and metadata
- counts-only vs differential expression
- contrasts, covariates, and batch terms for differential expression

## Dispatch

- FASTQ or aligned reads to raw counts, transcript estimates, or MultiQC summaries: `ngs-bulk-rnaseq-counts-qc`
- Raw count matrix plus sample metadata to contrasts, plots, and DE result tables: `ngs-bulk-rnaseq-differential-expression`

If the user asks for both, run count-generation planning first and start differential expression only after the raw count matrix, sample metadata, replicates, design formula, and contrasts are confirmed.

## Public Default

Prefer `nf-core/rnaseq` for standardized processing when a stable container or HPC runtime is available. Use the `local_light` Snakemake/Salmon path when Docker, registry egress, or Nextflow process containers are unavailable and a compact local run is appropriate.

## Plugin-Owned Local Paths

Use the counts/QC runner for local FASTQ-to-matrix execution:

```bash
python plugins/ngs-analysis/scripts/run_bulk_rnaseq_counts_qc.py \
  --sample-sheet samplesheet.csv \
  --fastq-root path/to/fastqs \
  --transcriptome-fasta reference/transcriptome.fasta \
  --genome-fasta reference/genome.fa \
  --annotation-gtf reference/genes.gtf \
  --execute
```

Use the differential-expression runner when the user already has a count or expression matrix:

```bash
python plugins/ngs-analysis/scripts/run_bulk_rnaseq_de.py \
  --count-matrix count_matrix.tsv \
  --sample-metadata sample_metadata.tsv \
  --contrasts contrasts.tsv \
  --execute
```

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline bulk_rnaseq --emit-install-plan
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline bulk_rnaseq_counts_qc --emit-install-plan
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline bulk_rnaseq_differential_expression --emit-install-plan
python plugins/ngs-analysis/scripts/ngs_preflight.py --profile local_light --emit-install-plan
```

## Kickoff Pattern

Preflight run:

```bash
nextflow run nf-core/rnaseq \
  -profile test,docker \
  --outdir results/rnaseq_test
```

Real run skeleton:

```bash
nextflow run nf-core/rnaseq \
  -profile docker \
  --input samplesheet.csv \
  --outdir results/rnaseq \
  --genome GRCh38 \
  --aligner star_salmon
```

If strandedness is unknown, run inference or use the pipeline's strandedness detection before committing to final counts.

Local execution run:

```bash
python plugins/ngs-analysis/scripts/run_bulk_rnaseq_counts_qc.py \
  --sample-sheet samplesheet.csv \
  --fastq-root path/to/fastqs \
  --transcriptome-fasta reference/transcriptome.fasta
```

The local runners create a standard run envelope with `run_manifest.json`, `config.json`, `validation/`, `logs/`, `versions/`, `artifact_index.json`, and `summary.md`. Do not depend on development-only eval harness paths in a shared package.

## Downstream

Only start DESeq2/edgeR/limma analysis after confirming biological replicates, design formula, and contrasts. Preserve the raw count matrix and sample metadata.
