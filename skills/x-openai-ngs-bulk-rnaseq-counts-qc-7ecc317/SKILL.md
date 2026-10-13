---
name: x-openai-ngs-bulk-rnaseq-counts-qc-7ecc317
description: Run or plan bulk RNA-seq FASTQ-to-count processing with sample-sheet, strandedness, genome annotation, alignment or pseudoalignment, MultiQC, and count-matrix QC checks.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Bulk RNA-seq Counts QC

Use this skill for bulk RNA-seq read processing, quantification, and count-matrix generation. If the user already has a count matrix and wants contrasts or statistics, use `ngs-bulk-rnaseq-differential-expression`.

## Essential Inputs

Confirm:

- FASTQ or aligned-read inputs and paired-end/single-end status
- organism, genome build, FASTA, GTF, and gene ID convention
- strandedness or permission to infer strandedness
- sample sheet with biological condition, replicate, batch, and library metadata
- desired quantification: gene counts, transcript estimates, or both
- alignment strategy: `STAR/Salmon`, Salmon-only, featureCounts from BAMs, or existing lab protocol

## Route

Prefer `nf-core/rnaseq` for standard processing when a stable container or HPC runtime is available. Use the `local_light` Snakemake/Salmon path for small local/devbox feasibility runs when Docker, registry egress, or Nextflow process containers are the blocker.

The plugin-owned local runner is:

```bash
python plugins/ngs-analysis/scripts/run_bulk_rnaseq_counts_qc.py \
  --sample-sheet samplesheet.csv \
  --fastq-root path/to/fastqs \
  --transcriptome-fasta reference/transcriptome.fasta \
  --genome-fasta reference/genome.fa \
  --annotation-gtf reference/genes.gtf \
  --execute
```

Omit `--execute` for validation plus Snakemake workflow validation only. Use `--no-dry-run` only when the user wants input validation and run-envelope preparation without workflow graph validation.

The runner emits a run-local `resources/` readiness bundle with `resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. Resource checks are advisory by default for custom or reduced references; add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when a registered genome bundle must be complete before the run is considered ready.

Preflight command:

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline bulk_rnaseq_counts_qc --emit-install-plan
python plugins/ngs-analysis/scripts/ngs_preflight.py --profile local_light --emit-install-plan
```

## Decision Points

- If strandedness is unknown, infer it before final counting; do not lock in a design based on library guesses.
- If strandedness is provided, carry it into the quantification command and flag any disagreement between the configured library type and Salmon's inferred format.
- Keep genome FASTA, GTF, transcriptome, and aligner indexes from the same build/release.
- Inspect per-sample reads, mapping rate, rRNA/mitochondrial fraction when available, duplication, insert size, gene-body bias, and assignment rate.
- Preserve raw counts separately from normalized expression.
- Carry sample metadata forward exactly; downstream DE depends on this table.

## Outputs

Produce:

- sample sheet and command/profile
- reference manifest with genome and GTF release
- MultiQC or equivalent processing summary
- Salmon `quant.sf` outputs, TPM/NumReads/effective-length matrices, and carried-forward sample metadata
- Gene-level expected-count and TPM matrices derived from transcript-level Salmon outputs, plus a `tx2gene` provenance table
- Compact QC verdict JSON covering mapping rate, duplication, library-type agreement, and outlier samples
- Browser-safe MultiQC helper HTML pages and a localhost launch hint for reliable in-app review
- Run-local reference readiness artifacts under `resources/`, including the resource plan, manifest, environment exports, and Markdown readiness summary
- issues that block differential expression, such as missing replicates, mislabeled groups, or severe batch/library failures
- standard run envelope: `run_manifest.json`, `config.json`, `validation/`, `logs/`, `versions/`, `artifact_index.json`, and `summary.md`
