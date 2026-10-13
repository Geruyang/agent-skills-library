---
name: x-openai-ngs-scrna-seq-4ab7647
description: Route single-cell or single-nucleus RNA-seq FASTQs to public count-generation workflows and defer post-count matrix QC, annotation, clustering, and UMAP analysis to the embedded scrna-seq-qc skill.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Single-cell RNA-seq

Use this skill for scRNA-seq or snRNA-seq kickoff from FASTQs, Cell Ranger-style outputs, matrices, `.h5`, `.h5ad`, or `.rds`. This skill owns upstream intake and FASTQ-to-count routing; post-count QC, annotation, clustering, and UMAPs must route to the embedded `scrna-seq-qc` skill.

## Essential Inputs

Confirm:

- input type: FASTQ, count matrix, `.h5`, `.h5ad`, or `.rds`
- assay: single-cell or single-nucleus
- chemistry or barcode/UMI layout
- organism and reference
- expected cells per sample when available
- sample, donor, batch, and channel metadata
- desired endpoint: count matrix only, QC, clustering, annotation, UMAP, or differential abundance/expression

## Public Default

For FASTQs, prefer public alternatives:

- `nf-core/scrnaseq`
- STARsolo
- kallisto-bustools via `kb-python`
- alevin-fry

Use 10x Cell Ranger only when the user explicitly wants vendor-standard output and has accepted the 10x EULA.

## Implementation Sequence

Treat scRNA as three ordered rows in the plugin state and execute them sequentially:

1. FASTQ-to-count:
   count matrix generation, barcode and feature tables, chemistry or whitelist choice, and a backend summary.
2. Post-count QC and annotation:
   raw-count-preserving objects, QC metrics, threshold plots, doublet and ambient-RNA outputs, clustering, UMAPs, and annotation confidence.
3. Downstream stats:
   pseudobulk matrices, differential expression or abundance tables, and per-condition plots.

Cell Ranger is an optional backend when vendor-standard output is explicitly required. It is not a standalone roadmap row and it is not the default execution target.

For post-count QC/annotation, use the embedded `skills/scrna-seq-qc` guidance. Route to that skill whenever the requested endpoint starts from a matrix, `.h5`, `.h5ad`, `.rds`, Cell Ranger output, or asks for QC, doublets, ambient RNA, annotation, clustering, UMAPs, or post-count differential summaries.

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline scrnaseq --emit-install-plan
```

## Kickoff Pattern

nf-core preflight run:

```bash
python plugins/ngs-analysis/scripts/run_nfcore_pipeline.py \
  --pipeline scrnaseq \
  --sample-sheet samplesheet.csv \
  --profile docker \
  --genome GRCh38 \
  --bundle-root grch38_core=/refs/GRCh38
```

This adapter captures the generated params, pinned Nextflow command, resource gate, trace/report paths, run manifest, and visualization index in the standard plugin envelope. Add `--revision <tag>` for pinned nf-core execution and `--execute` only when Nextflow plus a container/HPC profile are ready.

Plugin-owned local execution:

```bash
python plugins/ngs-analysis/scripts/run_scrnaseq_fastq_to_count.py \
  --sample-sheet samplesheet.csv \
  --genome-fasta reference/genome.fa \
  --annotation-gtf reference/genes.gtf \
  --cb-whitelist reference/whitelist.txt \
  --execute
```

The FASTQ-to-count runner emits advisory `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md` outputs by default. Add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when STARsolo reference bundle completeness should block readiness.

Matrix-level QC should be handled by `scrna-seq-qc` and must preserve raw counts, per-sample metadata, filter decisions, doublet calls, ambient-RNA handling, and plot outputs.

## Guardrails

- Do not assume 10x chemistry from filenames alone.
- Do not silently skip doublet or ambient-RNA assessment when doing QC.
- Do not over-annotate clusters without matched references or clear markers.
