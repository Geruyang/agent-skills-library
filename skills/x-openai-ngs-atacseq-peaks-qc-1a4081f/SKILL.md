---
name: x-openai-ngs-atacseq-peaks-qc-1a4081f
description: Run or plan ATAC-seq QC, alignment, TSS enrichment, fragment-size, blacklist, peak-calling, consensus peak, and differential accessibility workflows.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## Reviewed capability mapping (TRAE / Claude)

The commands below reference shared `plugins/ngs-analysis/scripts/` runners that are not bundled in this standalone skill. Locate the installed ngs-analysis package and resolve its scripts before executing. If absent, report runner execution as blocked and produce a workflow plan; use a documented equivalent pipeline only after validating its toolchain, reference resources, and the same QC gates. Do not mark biological outputs complete based only on a planned command.

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# ATAC-seq Peaks QC

Use this skill for ATAC-seq accessibility analysis from FASTQ or BAM. If the assay is ChIP-seq, CUT&RUN, CUT&Tag, or antibody-targeted enrichment, use `ngs-chip-cutrun-peaks-qc`.

## Essential Inputs

Confirm:

- FASTQ/BAM inputs and paired-end status
- organism, genome build, blacklist, and mitochondrial contig names
- biological replicates, conditions, batches, and sample metadata
- whether the target is QC only, peaks, consensus peaks, bigWigs, or differential accessibility
- whether Tn5 shifting is handled by the chosen workflow
- desired peak caller and downstream matrix generation

## Route

Prefer `nf-core/atacseq` for full reproducible processing. Use direct MACS2 only when BAMs are already aligned, duplicate/blacklist handling is known, and the user wants focused peak calling.

Preflight command:

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline atacseq_peaks_qc --emit-install-plan
```

For compact read-level intake/QC, use the shared epigenomics execution package:

```bash
python plugins/ngs-analysis/scripts/run_fastq_assay_package.py \
  --lane epigenomics_peaks \
  --sample-sheet atac_samples.csv \
  --execute
```

For local-light ATAC alignment, peaks, FRiP, TSS, bigWig tracks, and consensus peaks from FASTQ or prepared BAMs, use the dedicated ATAC runner:

```bash
python plugins/ngs-analysis/scripts/run_atacseq_peaks_qc.py \
  --sample-sheet atac_samples.csv \
  --bowtie2-index /refs/GRCh38/bowtie2/genome \
  --genome-size hs \
  --blacklist-bed /refs/GRCh38/blacklists/encode_blacklist.bed \
  --tss-bed /refs/GRCh38/tss.bed \
  --execute
```

This runner emits `qc/atacseq_qc_summary.{tsv,json}`, `qc/atacseq_qc_dashboard.html`, native SVG FRiP/peak and insert-size plots, browser-track handoff files under `tracks/`, and TSS profile/heatmap commands when `--tss-bed` is supplied. Add `--run-motifs --motif-genome <genome>` when HOMER motif enrichment should be part of the backend run.

It also emits `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. The resource check is advisory by default for local-light runs; add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when missing registered reference bundles should block readiness.

For nf-core execution, use `plugins/ngs-analysis/scripts/run_nfcore_pipeline.py --pipeline atacseq`.

## QC Gates

Review before biological interpretation:

- read depth, alignment rate, duplicate rate, and mitochondrial fraction
- insert-size periodicity/nucleosome pattern
- TSS enrichment and FRiP score when available
- blacklist overlap and peak count per sample
- replicate concordance and consensus peak support

Do not proceed to differential accessibility if replicate quality or metadata is insufficient.

## Outputs

Produce:

- sample sheet and workflow command/profile
- QC summary and failed-sample flags
- narrowPeak/BED peak sets, consensus peaks, bigWigs, browser-track manifests, browser-track preview HTML, native QC dashboard/SVG plots, TSS plots, and peak-count matrix when requested
- motif summary files when a motif backend is requested
- differential-accessibility design and contrasts if applicable
- caveats for low TSS enrichment, high mitochondrial reads, weak replicate concordance, or poor FRiP
