---
name: x-openai-ngs-dna-germline-variants-f59cc67
description: Run or plan deep germline WGS, WES, targeted-panel, cohort, or trio variant-calling workflows with reference-build, known-sites, QC, joint-calling, and annotation checks.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Germline DNA Variants

Use this skill for germline WGS, WES, or inherited-disease panel analysis from FASTQ, BAM, or CRAM. If the request is tumor-only, tumor-normal, or low-frequency molecular-barcode panel calling, use a somatic or UMI-panel skill instead.

## Essential Inputs

Confirm:

- data type: WGS, WES, or targeted panel
- sample model: singleton, cohort, duo, trio, family, or case/control
- input type: FASTQ, BAM, or CRAM
- organism, reference build, FASTA, indexes, and contig naming
- known-sites resources for BQSR, contamination, and annotation
- target BED and bait BED for WES/panel data
- sex/ploidy assumptions and mitochondrial/sex-chromosome requirements
- desired callers, annotation outputs, and final VCF/gVCF expectations

## Route

Prefer `nf-core/sarek` for full FASTQ/BAM-to-VCF workflows. Use direct GATK4, DeepVariant, samtools, or bcftools only for focused tasks or a custom workflow.

Preflight command:

```bash
python plugins/ngs-analysis/scripts/ngs_preflight.py --pipeline dna_germline_variants --emit-install-plan
```

For compact local checks from prepared BAM/CRAM files, use the shared DNA execution package:

```bash
python plugins/ngs-analysis/scripts/run_dna_variant_calling.py \
  --sample-sheet dna_samples.tsv \
  --reference-fasta reference.fa \
  --execute
```

Treat this as a focused samtools/bcftools run envelope, not as a substitute for full cohort, trio, gVCF, BQSR, or annotation workflows.

For a higher-fidelity local germline run that owns BQSR, per-sample gVCFs, and joint genotyping assumptions, use the germline-specific runner:

```bash
python plugins/ngs-analysis/scripts/run_dna_germline_variants.py \
  --sample-sheet dna_samples.tsv \
  --reference-fasta reference.fa \
  --known-sites dbsnp.vcf.gz \
  --known-sites mills.vcf.gz \
  --emit-gvcf \
  --joint-call \
  --execute
```

This runner still expects reference-matched resources and an available GATK toolchain. It packages the validation state and generated artifacts even when execution is blocked by missing tools or resources.

It also writes advisory `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md` artifacts by default. Add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when complete registered reference and known-sites bundles should be mandatory for readiness.

## Decision Points

- For cohorts or families, decide whether the endpoint is per-sample VCFs, gVCFs for joint genotyping, or a jointly called cohort VCF.
- For WES/panels, carry the target BED through alignment metrics, calling, and coverage reports; do not call off-target regions by accident.
- Use BQSR only when reference-matched known-sites resources exist. Do not mix GRCh37, hg19, GRCh38, or T2T resources.
- Check sample identity, sex concordance, contamination, coverage, duplication, insert size, and transition/transversion where feasible.
- For trios, preserve pedigree metadata and report Mendelian/QC checks separately from variant interpretation.

## Outputs

Produce:

- command or workflow profile and sample sheet
- reference/resource manifest with versions and checksums when available
- QC summary: coverage, duplication, insert size, contamination, sex/relatedness checks when run
- VCF/gVCF path, index path, and annotation path
- limitations: low coverage, missing known-sites, target design gaps, or build mismatches

Clinical interpretation, pathogenicity classification, and report signing are out of scope unless the user provides a validated clinical workflow.
