---
name: x-openai-ngs-dna-variant-calling-a99e380
description: Dispatch WGS, WES, or targeted DNA variant requests to germline, somatic, or UMI-panel skills, then plan public nf-core/sarek, GATK4, DeepVariant, samtools, or bcftools workflows.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# DNA Variant Calling

Use this skill as the DNA variant-calling dispatcher for WGS, WES, or targeted DNA panel analysis from FASTQ, BAM, or CRAM. Once the sample model is clear, hand off to the narrow subtype skill.

## Essential Inputs

Confirm:

- data type: WGS, WES, or panel
- sample model: germline single sample, cohort, trio, tumor-only, or tumor-normal
- input type: FASTQ, BAM, or CRAM
- organism and reference genome
- known-sites resources for BQSR, if required
- target BED for WES or panels
- UMI or duplex handling
- desired callers and annotation outputs

## Dispatch

Route by biological/sample model:

- Germline singleton, cohort, family, trio, WGS, WES, or ordinary inherited panel: `ngs-dna-germline-variants`
- Tumor-normal, tumor-only, relapse-baseline, or other cancer somatic calling: `ngs-dna-somatic-variants`
- UMI, duplex, molecular-barcode, or low-frequency targeted panel calling: `ngs-dna-umi-panel-variants`

If the request is ambiguous, ask only for the missing sample model and assay design needed to choose among these three. Do not run one generic variant workflow when the request needs subtype-specific assumptions.

## Public Default

Prefer `nf-core/sarek` for an end-to-end public workflow. Use direct GATK4, DeepVariant, samtools, or bcftools commands only for smaller, focused tasks or when the user explicitly wants a custom pipeline.

## Preflight

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline dna_variant_calling --emit-install-plan
```

## Local Execution Package

For a compact BAM/CRAM-to-VCF run with a matching reference FASTA, use the plugin-owned samtools/bcftools runner:

```bash
python plugins/ngs-analysis/scripts/run_dna_variant_calling.py \
  --sample-sheet dna_samples.tsv \
  --reference-fasta reference.fa \
  --region chr20:1-100000 \
  --filter-min-qual 30 \
  --filter-min-site-dp 10 \
  --execute
```

The sample sheet should include `sample` and `bam` or `cram` columns. When `--region` is provided the runner also emits per-base depth plus a callable-loci summary for that interval, and when filter thresholds are provided it emits a soft-filtered VCF alongside the raw calls. This package is suitable for focused local checks and run-envelope generation; subtype skills still own germline, somatic, UMI, reference-resource, cohort, annotation, and workflow assumptions.

This compact runner now writes advisory `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md` artifacts for the selected genome bundle. Use `--require-resource-plan` when missing registered reference resources should block readiness; otherwise the explicit `--reference-fasta` remains enough for focused local checks.

## Kickoff Pattern

Preflight-first nf-core pattern:

```bash
nextflow run nf-core/sarek \
  -profile test,docker \
  --outdir results/sarek_test
```

Real run skeleton:

```bash
nextflow run nf-core/sarek \
  -profile docker \
  --input samplesheet.csv \
  --outdir results/sarek \
  --genome GRCh38 \
  --tools haplotypecaller,vep
```

For WES/panel data, include the target BED. For tumor-normal data, verify pair metadata before execution. For UMI panels, preserve barcode handling and molecule-level QC.

## Guardrails

- Do not mix genome builds across FASTA, GTF/BED, known sites, and VEP cache.
- Do not download large references without confirming disk space and target path.
- Treat clinical interpretation as out of scope unless the user has a validated clinical workflow.
