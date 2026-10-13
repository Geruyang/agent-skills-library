---
name: x-openai-metric-diagnostics-99ec316
description: Diagnose why a metric changed or differs from expectation. Use when the task is to identify likely drivers of a metric movement, anomaly, gap, or discrepancy.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## Reviewed capability mapping (TRAE / Claude)

Resolve related skill names through the installed skill catalog; the `$name` notation is a source reference, not a guaranteed command. For the required report handoff, use an installed report skill or create an equivalent local HTML/Markdown report and inspectable notebook with available file tools. An MCP app is optional and must be discovered before use. If data access or artifact-writing capability is missing, identify the unavailable step and provide only evidence-backed findings; never claim a report or live query exists.

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Related Skills

Use x-openai-gather-business-context-c6dd24a when business context is needed to understand the metric, analysis period, ownership, or plausible explanations.

Use x-openai-product-business-analysis-02bad41 when the task asks for a recommendation or tradeoff decision after diagnosing the movement.

Use x-openai-analyze-data-quality-e271d0f when dashboard trust, grain, freshness, or source disagreement could affect the metric.

# Metric Diagnostics

Use this skill to diagnose why a metric changed or differs from expectation. Reproduce the metric, define the comparison, quantify the movement, validate likely drivers, and state what is verified, likely, unresolved, and useful to do next.

Clarify with the user when a missing input would materially change the analytical frame or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

## Skill Configuration

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

## Workflow

### 1. Define The Diagnostic Question

Frame the diagnostic so it is clear what changed and what comparison would prove it.

Define:

- what the metric means in business terms
- the time window and comparison that make the change measurable
- the population and grain that determine what counts
- the source that owns the metric definition
- the diagnostic question being answered, for example movement, concentration, or reconciliation

Use x-openai-gather-business-context-c6dd24a when business context is needed to understand what the metric means, what changed around the analysis period, or which explanations are plausible.

### 2. Validate The Metric Definition And Source

Before explaining the movement, confirm that the metric is defined correctly and that the source data can measure it reliably.

Confirm the metric definition, grain, aggregation logic, filters, joins, exclusions, freshness, lineage, and any disagreement between trusted surfaces. Keep this source check focused on issues that could change the answer.

Treat current context, named semantic layers, and familiar table names as source candidates, not source selection. For broad metric questions, run live source discovery against available tables, dashboards, metric docs, semantic layers, or other source-of-truth surfaces before choosing the controlling source. When both are available, inspect at least one business-facing or top-line surface and one lower-level source surface, then state why the selected source owns the answer.

Use x-openai-analyze-data-quality-e271d0f when freshness, grain, joins, missingness, schema drift, outliers, unexpected categories, or distribution shifts could affect trust.

Use x-openai-jupyter-notebooks-a1a32af when fresh SQL, Python, statistical modeling, reusable calculations, or multi-step decomposition need an inspectable analytical record.

### 3. Establish The Metric Pattern

Before looking for drivers, establish the metric pattern the diagnostic needs to explain. Quantify the metric over the relevant period and scope. If the question includes a comparison, reproduce that comparison.

Do not search for causes until the size, timing, and scope of the pattern are verified or explicitly marked uncertain.

### 4. Choose The Diagnostic Plan

Choose the smallest set of cuts and checks likely to explain the pattern or strengthen confidence.

Choose driver dimensions from the metric's operating logic, business context, and source shape. Prioritize drivers the business usually monitors or can act on, not every field available in the source. If the relevant drivers are unclear, use current context, a named semantic layer, or x-openai-gather-business-context-c6dd24a to understand how the business explains the metric and what changed around the analysis period.

When using a lower-level table, do not limit the driver analysis to fields surfaced by the first query. Recreate or join the business grouping needed to answer the question, such as model family, model superfamily, segment, region, cohort, product taxonomy, or customer hierarchy. If the grouping cannot be reconstructed, say so before simplifying the analysis.

Use the explanation mode that fits the question. Common examples:

- **Metric change**: compare the focal window with a baseline, rank segment contributions, check peer or historical context, and test mix shift versus within-segment movement.
- **Spike, regression, or incident**: pin down onset, peak, recovery,
  distribution shape rather than only averages, affected slices, broad versus localized degradation, and whether traffic or failure behavior changed.
- **Largest contributors or concentration**: define "largest", rank entities,
  compare total share and change, and look for major movers, entrants, and exits.
- **Reconciliation or difference analysis**: align definitions, filters, grain,
  numerator, denominator, and exclusions; quantify the components explaining the gap and state any residual.

### 5. Decompose And Validate Drivers

Quantify the main drivers and validate whether they explain the pattern.

Size each major driver with the strongest readily available evidence. Show whether it explains the pattern, how large it is relative to the relevant base, trend, or gap, whether it is broad or concentrated, and whether it holds under the right comparison or scope.

Iterate on driver hypotheses until the explanation answers why in a way that is relevant to the business. Follow promising cross-cuts and drill-downs when they could reveal the key explanation, and stop when additional cuts are unlikely to change the conclusion or materially improve confidence.

Interpret driver results in context:

- Use the relevant base, comparison, or share of total to make the driver meaningful.
- For rates, check whether the numerator, denominator, or both explain the change.
- For additive metrics, calculate contribution share when it sharpens the story.
- Separate composition effects from within-segment performance effects when that distinction changes the explanation.
- Prefer mutually exclusive driver buckets when additive contributions need to be interpreted; reconcile the decomposition exactly or size and explain the residual.

Treat measurement issues as possible explanations, not just cleanup details. For example, the pattern may come from logging changes, incomplete recent data, duplicated rows, or a shifted denominator rather than an underlying business change.

Calibrate the explanation to the evidence, and make important uncertainty visible. Use context when it changes interpretation, such as whether the pattern is ordinary, unusual, expected, or tied to a known change.

Use x-openai-visualize-data-fe600a7 when a chart would make the diagnostic claim easier to understand or verify.

### 6. State Implications And Follow-Up

Lead with the answer to the diagnostic question, then state the practical implications when the evidence supports them.

The answer should make clear:

- the pattern being explained
- the strongest driver explanation and supporting evidence
- why it matters for the business
- how much confidence to place in the explanation
- the implication, next action, or follow-up that matters most

Use x-openai-product-business-analysis-02bad41 when the user needs a recommendation or tradeoff decision, not just the diagnostic implication.

Keep implications distinguishable from verified factual reporting so a reader can tell where evidence ends and interpretation begins. Do not claim causality from timing alone; state when an explanation is only a plausible hypothesis.

Use x-openai-gather-business-context-c6dd24a when the metric result is clear but business context is needed to interpret the `so what` or identify realistic next actions.

Use x-openai-validate-data-bc92034 when methodology, calculations, caveats, or the evidentiary support for the diagnostic conclusion need review before sharing.

Do not treat artifact or report validation as analytical validation. Before handing off, confirm the analysis has the headline metric movement, driver contribution shares or effect sizes, source/window reconciliation, exact executed SQL or query references when queries were used, and caveats that would change interpretation.

Pass the diagnostic substance and supporting evidence to x-openai-build-report-768bc8e unless the user explicitly requests an inline, chat-only, brief/no-artifact answer, asks not to create a report/file/artifact, or selects another primary artifact. This handoff is mandatory when no explicit human waiver was given; do not infer a waiver because the user asked a direct diagnostic question or did not use the word "report". Let x-openai-build-report-768bc8e own the report surface, presentation polish, reproducibility treatment, and sharing handoff.
