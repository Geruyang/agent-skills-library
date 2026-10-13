---
name: x-openai-ngs-dna-somatic-variants-7c4f044
description: Run or plan tumor-normal, tumor-only, WGS, WES, or cancer-panel somatic variant workflows with pairing, contamination, panel-of-normals, purity, QC, and annotation checks.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Somatic DNA Variants

Use this skill for tumor-normal or tumor-only somatic SNV/indel calling from FASTQ, BAM, or CRAM. If the request is inherited germline calling or family analysis, resolve the installed `ngs-dna-germline-variants` skill or report that dependency unavailable.

## Essential Inputs

Confirm:

- tumor-normal, tumor-only, relapse-baseline, or multi-tumor design
- WGS, WES, or panel assay and target BED when applicable
- input type and whether reads are already aligned
- tumor/normal pairing table and sample identifiers
- reference build, known-sites, germline resource, and annotation cache
- panel-of-normals availability and matched-normal availability
- tumor purity, contamination expectations, and minimum allele fraction goals
- desired outputs: raw calls, filtered calls, VEP/SnpEff annotation, MAF, CNV/SV handoff

## Route

Prefer `nf-core/sarek` for an end-to-end public workflow when its supported callers fit the request. Use direct GATK Mutect2 or bcftools/samtools utilities for focused validation or prepared BAMs.


Resolve a verified installed NGS support package through the host catalog or user-provided source. This standalone export lacks the shared NGS scripts and intake/registry resources. Set `NGS_SCRIPT_DIR` to the absolute support-package scripts directory. The examples use Bash syntax; adapt variables and quoting to the actual shell. If the package is unavailable, return a provisional plan and explicitly block scripted preflight/execution. A documented nf-core/GATK CLI equivalent is acceptable only after verifying its actual options and reproducing the pairing, reference, QC, and output checks; never claim unavailable runner outputs were generated.

Preflight command:

```bash
python "$NGS_SCRIPT_DIR/ngs_preflight.py" --pipeline dna_somatic_variants --emit-install-plan
```

For compact local checks from prepared tumor/normal BAM/CRAM files, use the dedicated Mutect2 runner:

```bash
python "$NGS_SCRIPT_DIR/run_dna_somatic_variants.py" \
  --sample-sheet somatic_pairs.tsv \
  --reference-fasta reference.fa \
  --germline-resource af-only-gnomad.vcf.gz \
  --panel-of-normals pon.vcf.gz \
  --execute
```

This produces a tumor-normal/tumor-only pairing table, Mutect2 command plan, contamination/filtering artifacts, somatic QC summary, `qc/somatic_pair_review.{tsv,json}`, visualization index, and filtered VCF outputs when the local GATK resources are available. For nf-core execution, use the located `run_nfcore_pipeline.py --pipeline sarek` runner.

The direct runner also emits `resources/resource_plan.json`, `resource_manifest.tsv`, `resource_env.sh`, and `resource_readiness.md`. The resource check is advisory by default so custom or reduced references can still be planned; add `--genome-build`, `--bundle-root <bundle>=<path>`, and `--require-resource-plan` when missing registered reference bundles should block readiness.

## Decision Points

- Verify tumor-normal pair metadata before execution. A swapped or missing normal changes the biological meaning of the calls.
- For tumor-only analysis, explicitly state the false-positive risk and require a germline resource plus careful filtering.
- Use panel-of-normals when available and reference-matched; do not reuse a PON across incompatible capture kits or genome builds.
- Track contamination, orientation bias, strand artifacts, mapping quality, coverage, tumor purity, and allele-fraction filters.
- Keep germline filtering separate from somatic interpretation; avoid presenting tumor-only calls as confirmed somatic without supporting evidence.

## Outputs

Produce:

- validated pairing/sample sheet
- caller/filter settings and reference/resource manifest
- QC summary: tumor/normal depth, contamination, duplication, insert size, on-target rate for panels/WES
- per-pair review table covering matched-normal state, PON/germline-resource availability, contamination-table status, filtered VCF status, and parsed variant counts
- VCF/MAF/annotation paths and a filtered-vs-raw call count summary
- caveats for tumor-only calls, low-purity tumors, low-depth regions, or missing matched normals

Clinical actionability and treatment recommendations are out of scope unless the user supplies a validated clinical interpretation workflow.
