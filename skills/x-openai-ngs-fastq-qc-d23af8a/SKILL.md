---
name: x-openai-ngs-fastq-qc-d23af8a
description: Validate FASTQ inputs, run local FastQC/MultiQC QC, interpret QC signals, and optionally execute fastp or Cutadapt trimming branches without overwriting raw reads.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# FASTQ QC

Use this skill for QC-only, trimming-first, or FASTQ quality interpretation workflows. This skill can execute the plugin-owned local FastQ QC runner when the user approves a local run. It should decide whether trimming or additional investigation is warranted; it should not blindly trim by default.

## Essential Inputs

Confirm:

- FASTQ paths and pairing convention
- whether output should be QC-only or trimmed FASTQs
- known adapter or primer sequences
- organism if contamination screening or host depletion is requested
- output directory
- whether FASTQs are raw, demultiplexed, previously trimmed, or downloaded from an archive
- whether downstream analysis expects original read lengths, UMIs, or inline barcodes

## Public Tools

Default tool set:

- `FastQC` for raw read QC
- `MultiQC` for project-level summary
- `fastp` for all-in-one QC/trimming when acceptable
- `Cutadapt` when primer/adapter handling needs explicit sequences
- `seqkit` for quick counts, stats, and subsampling

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline fastq_qc --emit-install-plan
```

## Local Execution

Use the plugin-owned runner for local artifact-producing FASTQ QC:

```bash
python plugins/ngs-analysis/scripts/run_fastq_qc.py \
  --sample-sheet samplesheet.csv \
  --execute
```

Single paired sample:

```bash
python plugins/ngs-analysis/scripts/run_fastq_qc.py \
  --sample sampleA \
  --r1 sampleA_R1.fastq.gz \
  --r2 sampleA_R2.fastq.gz \
  --execute
```

Optional trimming branch:

```bash
python plugins/ngs-analysis/scripts/run_fastq_qc.py \
  --sample-sheet samplesheet.csv \
  --trim-mode fastp \
  --execute
```

For explicit adapters:

```bash
python plugins/ngs-analysis/scripts/run_fastq_qc.py \
  --sample-sheet samplesheet.csv \
  --trim-mode cutadapt \
  --adapter-r1 AGATCGGAAGAGC \
  --adapter-r2 AGATCGGAAGAGC \
  --execute
```

The runner performs pre-execution validation before Snakemake execution. It writes a timestamped run directory with `run_manifest.json`, `config.json`, `validation/`, `workflow/Snakefile`, logs, `artifact_index.json`, `summary.md`, FastQC/MultiQC outputs, and `qc_interpretation.json` after successful execution.

## Interpretation Rules

Inspect raw QC before recommending trimming:

- Per-base quality drop at the read end: consider quality trimming, but preserve enough length for alignment or amplicon merging.
- Adapter or primer signal: use `cutadapt` when explicit sequences matter; use `fastp` only when automatic handling is acceptable.
- Poly-G or patterned-flowcell artifacts: handle with a tool that explicitly supports the artifact and report the assumption.
- Overrepresented sequences: classify adapters, primers, rRNA, PhiX, host contamination, or true biology before filtering.
- Per-tile failures or severe quality shifts: flag possible run-level issues and avoid treating them as ordinary adapter contamination.
- High duplication: interpret by assay; it may be expected for amplicons, targeted panels, or low-input libraries.
- Pairing issues: verify R1/R2 file counts and read-name pairing before any downstream workflow.

Do not overwrite input FASTQs. Preserve the raw QC reports even when trimmed FASTQs are created.

## Kickoff Pattern

QC-only:

```bash
mkdir -p results/fastqc results/multiqc
fastqc -t 4 -o results/fastqc *.fastq.gz
multiqc results/fastqc -o results/multiqc
```

QC plus trimming:

```bash
fastp \
  -i sample_R1.fastq.gz \
  -I sample_R2.fastq.gz \
  -o results/trimmed/sample_R1.fastq.gz \
  -O results/trimmed/sample_R2.fastq.gz \
  --html results/fastp/sample.html \
  --json results/fastp/sample.json
multiqc results -o results/multiqc
```

## Output Review

Return a short QC interpretation with:

1. sample/read-pair inventory
2. QC modules that look normal
3. QC modules that require action or user confirmation
4. trimming or no-trimming recommendation with rationale
5. downstream caveats such as short reads, contaminated libraries, or failed pairs

When using the local runner, ground the response in the generated `qc_interpretation.json`, `summary.md`, and MultiQC report instead of relying only on expected artifacts.
