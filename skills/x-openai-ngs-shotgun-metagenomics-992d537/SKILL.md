---
name: x-openai-ngs-shotgun-metagenomics-992d537
description: Kick off public shotgun metagenomics QC, host-depletion, taxonomic profiling, and functional profiling workflows using nf-core/taxprofiler, Kraken2, Bracken, MetaPhlAn, and HUMAnN.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Shotgun Metagenomics

Use this skill for shotgun metagenomic FASTQs.

## Essential Inputs

Confirm:

- paired-end or single-end reads
- host organism and host-depletion requirement
- target outputs: taxonomic profile, functional profile, assembly, binning, or QC only
- preferred database family, if any
- database paths or permission to download large databases
- sample metadata, batches, and negative controls

## Public Defaults

Prefer `nf-core/taxprofiler` for reproducible taxonomic profiling. Use direct Kraken2/Bracken, MetaPhlAn, or HUMAnN when the user wants a focused path or already has databases installed.

For direct backend execution, prefer the plugin runner over handwritten shell when possible because it validates database bundle contents and records `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. `--run-bracken` and `--run-humann` make those database bundles blocking, not merely optional.

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline shotgun_metagenomics --emit-install-plan
```

## Local Execution Package

For FASTQ intake/QC before host-depletion, taxonomic profiling, or functional profiling, use:

```bash
python plugins/ngs-analysis/scripts/run_fastq_assay_package.py \
  --lane shotgun_metagenomics \
  --sample-sheet shotgun_samples.csv \
  --execute
```

This validates read paths and structure, runs seqkit stats and FastQC/MultiQC when available, and writes `taxonomic_classification_status.json`. Add `--kraken-db /path/to/db` only when a local Kraken2 database is available; otherwise the package records the database/tool blocker explicitly.

For backend taxonomic and functional profiling when databases are available, use:

```bash
python plugins/ngs-analysis/scripts/run_shotgun_metagenomics.py \
  --sample-sheet shotgun_samples.csv \
  --kraken-db /db/kraken2/standard \
  --host-reference /refs/human_kneaddata_db \
  --run-bracken \
  --run-humann \
  --humann-db /db/humann \
  --metadata sample_metadata.tsv \
  --execute
```

For nf-core execution, use `plugins/ngs-analysis/scripts/run_nfcore_pipeline.py --pipeline taxprofiler`.

When `--host-reference` is supplied, the backend runner adds a KneadData host-depletion step, requires `kneaddata` in tool preflight, writes cleaned FASTQs under `host_depletion/`, and uses those cleaned reads for downstream Kraken2 and HUMAnN steps. Keep the host reference path and host-depletion decision visible because it can change taxonomic and functional abundance conclusions.

The backend runner writes native matrix artifacts when database tools produce outputs:

- `tables/bracken_est_reads_matrix.tsv`
- `tables/bracken_relative_abundance_matrix.tsv`
- `tables/humann_pathabundance_matrix.tsv`
- `tables/humann_genefamilies_matrix.tsv`
- `tables/bracken_summary.json` and `tables/humann_summary.json`
- `tables/top_bracken_taxa.tsv`, `tables/top_humann_pathways.tsv`, `tables/top_humann_gene_families.tsv`, and `tables/metagenomics_backend_review.json` when normalized backend matrices are available

If Kraken2/Bracken/HUMAnN outputs are absent, the summaries and visualization manifest keep those layers `not_available` instead of implying taxonomic or functional interpretation succeeded.

## Kickoff Pattern

nf-core preflight run:

```bash
nextflow run nf-core/taxprofiler \
  -profile test,docker \
  --outdir results/taxprofiler_test
```

Direct Kraken2 skeleton:

```bash
kraken2 \
  --db /path/to/kraken2_db \
  --paired sample_R1.fastq.gz sample_R2.fastq.gz \
  --report results/kraken2/sample.report \
  --output results/kraken2/sample.kraken
```

## Visualization Outputs

The local FASTQ package always writes `visualizations/index.html` and `visualizations/visualization_manifest.json`. With only FASTQs, this is a read-QC/readiness bundle. Provide existing `--kraken-report`, `--bracken-table`, `--humann-pathabundance`, or `--humann-genefamilies` files to generate native taxonomy and functional-profile plots without requiring a Marimo notebook. For full backend runs, `run_shotgun_metagenomics.py` now also merges generated Bracken/HUMAnN outputs into plugin-native tables for the review bundle and writes `visualizations/shotgun_backend_dashboard.html` plus SVG plots for top Bracken taxa, HUMAnN pathways, and HUMAnN gene families when the corresponding matrices are present.

## Guardrails

- Do not auto-download large databases without confirming size and destination.
- Host depletion choices can change biological conclusions; document the reference and parameters.
- Negative controls should stay visible in QC and interpretation.
