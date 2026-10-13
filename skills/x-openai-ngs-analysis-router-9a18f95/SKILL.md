---
name: x-openai-ngs-analysis-router-9a18f95
description: Route BCL, FASTQ, BAM/CRAM, count-matrix, or VCF sequencing requests to the right public NGS analysis skill and ask only the missing assay-specific setup questions.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Life Sciences NGS Analysis Router

Use this skill as the top-level entrypoint for ambiguous or broad sequencing-analysis requests.

## Start Here

Inspect the available inputs before asking the user questions. Look for:

- Illumina run-folder files: `RunInfo.xml`, `RunParameters.xml`, `SampleSheet.csv`, `Data/Intensities/BaseCalls`
- FASTQs: `*.fastq`, `*.fq`, `*.fastq.gz`, `*.fq.gz`
- BAM/CRAM/VCF: `*.bam`, `*.cram`, `*.vcf`, `*.vcf.gz`
- count matrices: `matrix.mtx`, `features.tsv`, `barcodes.tsv`, `*.h5`, `*.h5ad`, `*.rds`
- metadata: sample sheets, design files, target BEDs, reference FASTA/GTF, primer files

Read the NGS support package intake schema and pipeline registry after locating them as described in Preflight. If unavailable, use the intake questions below and label the route provisional.

## Intake Rules

Ask the smallest set of missing questions needed to choose a defensible pipeline. Do not ask the full questionnaire if file inspection already answers a field.

Always resolve:

- input type
- assay type
- desired output
- organism/reference
- paired-end vs single-end when FASTQs are involved
- any assay-specific design file or metadata required for the requested result
- runtime constraints: local/HPC/cloud, container availability, and whether installs are allowed

For human data, ask whether cloud upload is allowed before suggesting BaseSpace, Terra, DNAnexus, or any cloud path.

## Routing

Resolve the appropriate leaf skill by declared name/capability in the host catalog; exported IDs may differ. If absent, report the missing dependency and provide a route plan without claiming a handoff. Route to one leaf skill:

- BCL run folder or demultiplexing: `ngs-bcl-to-fastq`
- QC/trimming only: `ngs-fastq-qc`
- WGS/WES/panel variants: `ngs-dna-variant-calling`, then a subtype skill when the analysis model is clear
- germline WGS/WES/panel variants: `ngs-dna-germline-variants`
- tumor-normal or tumor-only somatic variants: `ngs-dna-somatic-variants`
- UMI, duplex, or low-frequency targeted panels: `ngs-dna-umi-panel-variants`
- bulk RNA-seq kickoff: `ngs-bulk-rnaseq`
- bulk RNA-seq FASTQ-to-count QC: `ngs-bulk-rnaseq-counts-qc`
- bulk RNA-seq differential expression from counts: `ngs-bulk-rnaseq-differential-expression`
- single-cell or single-nucleus FASTQ-to-matrix kickoff: `ngs-scrna-seq`
- single-cell or single-nucleus post-count QC/annotation/UMAP: `scrna-seq-qc`
- epigenomics kickoff: `ngs-epigenomics-peaks`
- ATAC-seq QC/peaks/accessibility: `ngs-atacseq-peaks-qc`
- ChIP-seq, CUT&RUN, or CUT&Tag QC/peaks: `ngs-chip-cutrun-peaks-qc`
- 16S/18S/ITS/COI amplicons: `ngs-amplicon-microbiome`
- shotgun metagenomics: `ngs-shotgun-metagenomics`
- runtime/package setup only: `ngs-runtime-env`

Prefer public, runtime-installable packages and nf-core workflows. Surface license/EULA/account boundaries before using proprietary or cloud tools.

## Preflight

Resolve a verified installed NGS support package through the host catalog or user-provided source. This standalone export lacks the shared NGS scripts and intake/registry resources. Set `NGS_SCRIPT_DIR` to the absolute support-package scripts directory. The examples use Bash syntax; adapt variables and quoting to the actual shell. If the package is unavailable, return a provisional plan and explicitly block scripted preflight/execution. A documented nf-core/GATK CLI equivalent is acceptable only after verifying its actual options and reproducing the pairing, reference, QC, and output checks; never claim unavailable runner outputs were generated.


Before installation or execution, run the verified available preflight from the user project root:

```bash
python "$NGS_SCRIPT_DIR/ngs_preflight.py" --pipeline <pipeline_key> --emit-install-plan
```

When the user needs an approval-ready install handoff, write persistent install artifacts:

```bash
python "$NGS_SCRIPT_DIR/ngs_preflight.py" --pipeline <pipeline_key> --manager micromamba --install-plan-outdir runtime_readiness/<pipeline_key>_install
```

Treat `install_plan.json` as the canonical review artifact. `install_commands.sh` is generated from the same plan and stays review-only unless the user explicitly approves execution with `NGS_RUN_INSTALL_COMMANDS=1`.

For reference- or database-heavy pipelines, also create a resource plan before saying the workflow is runnable:

```bash
python "$NGS_SCRIPT_DIR/ngs_reference_manager.py" plan --pipeline <pipeline_key> --genome-build <build> --outdir resource_readiness/<pipeline_key>
```

Use `--include-optional` for shotgun, amplicon, or motif-enabled epigenomics runs when optional databases materially affect the requested output.

Use `--network-checks` only when the user allows network checks. Use `--install-missing --yes` only when the user explicitly asks to install.

## Output Contract

Return:

1. the routed analysis type and confidence
2. missing essential parameters, if any
3. recommended public pipeline or package family
4. local tool preflight summary
5. preflight-first command or next concrete action
6. caveats around licenses, cloud upload, database size, and reference data
