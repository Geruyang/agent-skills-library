---
name: x-openai-ngs-chip-cutrun-peaks-qc-70ea4a6
description: Run or plan ChIP-seq, CUT&RUN, or CUT&Tag QC, control handling, spike-in, peak calling, broad-vs-narrow target selection, replicate, bigWig, and differential binding workflows.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# ChIP/CUT&RUN Peaks QC

Use this skill for antibody-targeted enrichment workflows: ChIP-seq, CUT&RUN, or CUT&Tag. Use `ngs-atacseq-peaks-qc` for ATAC-seq.

## Essential Inputs

Confirm:

- assay: ChIP-seq, CUT&RUN, or CUT&Tag
- target class: transcription factor, histone mark, chromatin regulator, or custom target
- FASTQ/BAM inputs and paired-end status
- input DNA, IgG, no-antibody, or spike-in controls
- organism, genome build, blacklist, and spike-in genome if used
- biological replicates, conditions, batches, and sample metadata
- desired endpoint: QC, peaks, bigWigs, consensus peaks, or differential binding

## Route

Use `nf-core/chipseq` for ChIP-seq and `nf-core/cutandrun` for CUT&RUN/CUT&Tag when they fit the assay. Use direct MACS2 only for prepared BAMs with known control and duplicate policy.

Preflight command:

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline chip_cutrun_peaks_qc --emit-install-plan
```

For compact FASTQ intake/QC, use the shared epigenomics execution package:

```bash
python plugins/ngs-analysis/scripts/run_fastq_assay_package.py \
  --lane epigenomics_peaks \
  --sample-sheet chip_or_cutrun_samples.csv \
  --execute
```

It records FASTQ-level QC and peak-calling readiness.

For local-light alignment, control-aware MACS2 peak calling, FRiP, bigWig tracks, consensus peaks, and motif-handoff artifacts, use the dedicated ChIP/CUT&RUN runner:

```bash
python plugins/ngs-analysis/scripts/run_chip_cutrun_peaks_qc.py \
  --sample-sheet chip_or_cutrun_samples.csv \
  --assay chipseq \
  --target-class tf \
  --peak-mode narrow \
  --bowtie2-index /refs/GRCh38/bowtie2/genome \
  --genome-size hs \
  --blacklist-bed /refs/GRCh38/blacklists/encode_blacklist.bed \
  --execute
```

This runner emits `qc/chip_cutrun_qc_summary.{tsv,json}`, `qc/chip_cutrun_qc_dashboard.html`, native SVG FRiP/peak and insert-size plots, browser-track handoff files under `tracks/`, and `motifs/motif_summary.tsv`. Add `--run-motifs --motif-genome <genome>` when HOMER motif enrichment should be executed instead of only planned.

It also emits `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. The resource check is advisory by default for local-light runs; add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when missing registered reference bundles should block readiness.

For nf-core execution, use `plugins/ngs-analysis/scripts/run_nfcore_pipeline.py --pipeline chipseq` or `--pipeline cutandrun`.

## Decision Points

- Choose narrow versus broad peak mode from target biology, not from convenience.
- Preserve control pairing and spike-in metadata through sample sheets.
- For histone marks, expect broad or domain-like signal for many marks; for TFs, expect sharper peaks and stronger replicate checks.
- Review alignment rate, duplicate rate, fragment size, FRiP/peak signal, blacklist overlap, and replicate concordance.
- Keep consensus peak generation and differential binding design separate from raw peak calling.

## Outputs

Produce:

- assay/target/control manifest
- command/profile and sample sheet
- QC summary with replicate/control status
- peaks, bigWigs, browser-track manifests, browser-track preview HTML, native QC dashboard/SVG plots, consensus peaks, and count matrix when requested
- motif summary files when a motif backend is requested
- differential binding design and caveats for missing controls, weak enrichment, or poor replicate concordance
