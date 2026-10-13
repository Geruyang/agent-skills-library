---
name: x-openai-ngs-epigenomics-peaks-ab23467
description: Dispatch ATAC-seq, ChIP-seq, CUT&RUN, or CUT&Tag requests to assay-specific QC, alignment, signal-track, peak-calling, consensus, and differential peak workflows.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Epigenomics Peaks

Use this skill as the epigenomics dispatcher for ATAC-seq, ChIP-seq, CUT&RUN, or CUT&Tag analysis. Hand off to the assay-specific deep skill once the assay type is known.

## Essential Inputs

Confirm:

- assay type
- FASTQ or BAM input
- organism and genome build
- blacklist file, if available
- control samples: input DNA, IgG, or spike-in
- biological replicates
- peak type: narrow, broad, accessibility, or protocol-specific
- desired outputs: QC report, peaks, consensus peaks, bigWigs, differential peaks

## Public Defaults

Choose the workflow by assay:

- ATAC-seq: `ngs-atacseq-peaks-qc` using `nf-core/atacseq` by default
- ChIP-seq: `ngs-chip-cutrun-peaks-qc` using `nf-core/chipseq` by default
- CUT&RUN or CUT&Tag: `ngs-chip-cutrun-peaks-qc` using `nf-core/cutandrun` by default

Use direct MACS2 only for focused peak-calling tasks from prepared BAMs.

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline epigenomics_peaks --emit-install-plan
```

## Local Execution Package

For FASTQ intake/QC over ATAC-seq, ChIP-seq, CUT&RUN, or CUT&Tag data, use the shared FASTQ assay package:

```bash
python plugins/ngs-analysis/scripts/run_fastq_assay_package.py \
  --lane epigenomics_peaks \
  --sample-sheet assay_samples.csv \
  --execute
```

This validates sample-sheet paths and read structure, runs seqkit stats and FastQC/MultiQC when available, and writes `peak_calling_readiness.json`. Full alignment, signal tracks, TSS/FRiP, consensus peaks, and differential analyses still route through the assay-specific workflow.

Assay-specific ATAC and ChIP/CUT&RUN runners now also emit native review files alongside TSV/JSON summaries: `qc/*_dashboard.html`, FRiP/peak SVG plots, insert-size SVG plots, browser-track preview HTML, UCSC track lines, and IGV session files.

## Kickoff Pattern

ATAC-seq preflight run:

```bash
nextflow run nf-core/atacseq \
  -profile test,docker \
  --outdir results/atacseq_test
```

ChIP-seq preflight run:

```bash
nextflow run nf-core/chipseq \
  -profile test,docker \
  --outdir results/chipseq_test
```

CUT&RUN/CUT&Tag preflight run:

```bash
nextflow run nf-core/cutandrun \
  -profile test,docker \
  --outdir results/cutandrun_test
```

Carry replicate and control metadata through the sample sheet before running real analysis.
