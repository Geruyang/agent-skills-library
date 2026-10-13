---
name: x-openai-kpi-reporting-52b00a6
description: Prepare KPI readouts, scorecards, WBR/MBR/QBR updates, and executive summaries from quantitative business or product metrics; use when the task is to report status, compare against targets, explain validated drivers, and state operating implications.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# KPI Reporting

Use this skill to turn business or product metrics into decision-ready operating readouts for leaders and teams. The job is to define the KPI contract, report status against the right comparison and target, include validated driver context, and state the operating implication clearly.

Clarify with the user when a missing input would materially change the analytical frame or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

This skill owns the KPI readout: what should be reported, how metrics should be interpreted, whether driver context is validated, and what operating takeaway follows. It does not own metric-system design, new driver investigation, or final artifact polish.

Use x-openai-metric-diagnostics-99ec316 when the readout needs fresh driver investigation, then return here to package the validated finding.

## Skill Configuration

### Discover sources and delivery capabilities

The `~~structured_data`, `~~company_docs`, `~~team_communication`, and `~~dashboards_or_bi` labels below are source categories, not callable tools. Map them to the current host's verified connections, authorized APIs/CLIs, or user-provided local files. Search only sources actually available within the task's authorized scope; record missing categories and preserve the source-of-truth guardrail below.

Names such as `x-openai-metric-diagnostics-99ec316`, `x-openai-design-kpis-a4f142e`, `x-openai-validate-data-bc92034`, `x-openai-build-report-768bc8e`, `x-openai-visualize-data-fe600a7`, and `x-openai-report-to-google-slides-442261d` identify companion skill roles. Resolve them through the installed skill catalog or export manifest before use; do not assume the original command spelling or sibling path exists. If an analysis companion is missing, perform its stated analytical responsibility with available tools and document the method. For delivery, use a verified equivalent report/deck capability or create a local Markdown/HTML report (and local deck when supported). A local file does not imply upload or creation in Google Slides. If the requested delivery surface is unavailable, hand over the local artifact and name the remaining dependency.

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

## Workflow

### 1. Clarify The Readout Purpose

Understand who the readout is for, what conversation it supports, and what is being reported before drafting. Anchor the update in the period being evaluated, the comparison or target that makes performance interpretable, and the freshness cutoff.

Ask the user for missing context when it would help make the readout more accurate or useful.

### 2. Define The Metric Framework

Decide which metrics belong in the readout and what role each one plays before pulling numbers. If the framework already exists, confirm it and use it. If it is missing or weak, use x-openai-design-kpis-a4f142e before reporting.

Start with the primary KPI, then add the smallest set of supporting metrics needed to explain status. Supporting metrics can explain movement, guard against harmful tradeoffs, or show whether performance is pacing as expected.

Lead with the metric that matters most to the audience. Do not add every available cut or comparison; include the metrics and slices decision-makers actually use, plus any that materially explain this update.

When the primary KPI is top-line, composite, or otherwise not directly actionable, define its driver decomposition before interpreting it. Use an existing metric tree when available. Otherwise identify the smallest useful set of component drivers, such as numerator and denominator, volume and rate, mix, funnel stages, segments, cohorts, or operational inputs. Do not invent a causal hierarchy when source definitions do not support one.

### 3. Lock Metric Definitions And Sources

Confirm the KPI definition, source, time window, reporting cutoff, comparison period, and any target or pacing expectation before interpreting performance. If a target or pacing basis is missing, ask before treating one as authoritative. Use x-openai-analyze-data-quality-e271d0f when source quality issues could change the reported metrics.

For all KPI updates, make a focused source pass across `~~structured_data`, `~~company_docs`, `~~team_communication`, and `~~dashboards_or_bi` before drafting. Do not infer from a sparse prompt that source-backed actuals are unavailable. Use structured data for actuals, metric definitions, and comparison periods; use the other lanes for additional business context and source-of-truth guidance.

If any core definition is unclear, ask the user to clarify before making precise claims. When a metric definition changed, show comparable restated history when available; otherwise call out the break clearly.

### 4. Pull The Topline Actuals

Do not draft or render a WBR, MBR, scorecard, or KPI update from placeholders. Query or inspect connected structured-data sources for core actuals first. If actuals are blocked or insufficient, stop and say what source or access is needed unless the user explicitly asked for a template or mockup.

Reproduce the topline actual before explaining movement or driver context.

For each headline KPI, include the current value, the absolute and relative change versus the comparison period, and a short interpretation.

Call out anything that makes the current value hard to compare with the prior period before interpreting the movement, such as a tracking change, data backfill, partial outage, or missing day.

### 5. Put The Numbers In Context

Compare actuals against the context that makes performance interpretable. When a target, plan, pacing model, benchmark, historical range, or relevant peer group is defined, identify it and compare performance against it before judging status.

If the goal has a deadline, do not just report whether the metric is above or below target. Show whether it is on pace to hit the target by the end of the period. Use the provided pacing definition when available. If none is defined or found, ask the user; when proceeding with a calculated fallback, state that it was calculated and explain the method.

When useful, include absolute and percent variance to target and a red/yellow/green status. Make clear what comparison or pacing basis the status label uses.

### 6. Explain Validated Drivers

KPI updates need driver context, but driver claims must be validated before they are presented as explanations. A plausible story is not enough.

When the readout needs to explain drivers, use x-openai-metric-diagnostics-99ec316 to identify and validate them. If trusted reporting or prior analysis already validates the drivers, use that evidence instead of re-running the diagnostic.

### 7. Add Business Context And Operating Implications

After identifying the likely drivers, use x-openai-gather-business-context-c6dd24a to look for business context that helps explain what happened and what it means for the readout. Let the driver analysis guide what context to look for, and connect context to the metric only when evidence supports the link.

Translate the evidence, driver analysis, and business context into the operating implication for the business. State whether the movement is concerning, what next step or action is warranted, and whether the main KPI is on track, at risk, or ahead of plan. Recommend action only when the evidence supports it; otherwise name the next validation step.

### 8. Validate The Readout

After the analysis is assembled and before shaping the final readout, use x-openai-validate-data-bc92034 to review whether the numbers, methodology, caveats, and evidence support the claimed status, drivers, and implications. Resolve material issues before sharing; carry remaining limitations into the readout.

### 9. Hand Off The Readout

End by handing the validated KPI readout to the discovered report-building capability (the original role is x-openai-build-report-768bc8e) unless the user explicitly requests an inline, chat-only, brief/no-artifact answer, asks not to create a report/file/artifact, or selects another primary artifact. A quick status update, brief readout, or findings-in-chat request is an inline output choice unless the user also asks for a report, document, deck, or durable artifact. Otherwise produce the report through that capability or the local fallback above; do not fabricate a handoff to an unavailable skill.

Before handoff, make the readout explicit:

- headline status and operating implication
- actuals, targets, pacing basis, and comparison periods
- validated drivers and unresolved uncertainty
- audience, cadence, and requested delivery surface when known
- charts or figures that would clarify the readout

Load `references/report-templates.md` before handing off and use the matching pattern as source notes for x-openai-build-report-768bc8e. Tell x-openai-build-report-768bc8e this is a KPI readout and pass the status, pacing, driver, uncertainty, audience, cadence, surface, and visual guidance above. Do not render charts directly from this skill; pass visual intent and supporting evidence to x-openai-build-report-768bc8e so x-openai-visualize-data-fe600a7 owns chart selection and QA.

For native slide or deck requests, discover the actual converter and verify its input requirements. The original `x-openai-report-to-google-slides-442261d` route consumes a local HTML analytics report rather than a live MCP app report; when that route is available, create HTML from the same source evidence first, then convert it. For another verified converter, follow its documented contract. When cloud delivery is unavailable, deliver the local report or deck and state that the requested cloud artifact has not been created.

## Standards

### Metric Standards

- Never present a KPI as precise when its definition, source, time window, or comparison basis is unclear.
- Make calculation logic, inclusion or exclusion rules, grain, and time treatment explicit when they affect interpretation.
- Reconcile totals and compare against prior reporting when possible.
- Do not compare periods, cuts, or targets that are not definitionally compatible. Call out definition changes, backfills, denominator shifts, or calendar effects when they affect the movement.

### Status And Pacing Standards

- Include the headline takeaway, current actual, relevant comparison, target or pacing context, driver summary, and implication unless the user asks for a narrower readout.
- Put actuals next to the target, plan, benchmark, or baseline when available so the reader can judge performance immediately.
- If a target is time-bound, show whether current performance is on pace using the provided pacing definition or a clearly stated calculated fallback.
- Keep recurring metric sections consistent across runs. If a requested section is missing because data, definitions, or validation are unavailable, explain the omission briefly.
- Use traffic-signal status only when it helps prioritize action. Pair color with text and state the basis for the status.
- Round numbers consistently, label units, and surface caveats when they change interpretation.

### Driver Standards

- Quantify drivers whenever the evidence supports it; do not use descriptive prose as a substitute for sizing the effect.
- Report the few drivers, contributors, or known non-drivers that matter for interpreting the KPI movement.
- For top-line KPI movement, structure validated drivers as a compact decomposition: top-line actual, component drivers, largest contributors or non-drivers, and residual or unresolved movement. Use an additive bridge only when the components reconcile cleanly; otherwise explain the relationship and uncertainty.
- Separate validated drivers from business context or hypotheses.
- Do not elevate business events into causes unless the timing, affected population, and measured change support the link.
- State whether the movement is broad-based or concentrated when that changes the operating implication.
- If driver evidence remains unresolved, name the uncertainty or diagnostic follow-up instead of inventing an explanation.

### Presentation Standards

- Write for executives and operators who skim: lead with the answer, then the evidence.
- Use business-readable numbers and compact formats such as `123k (+8% w/w, +19% m/m)`.
- Replace generic adjectives like `strong`, `healthy`, or `soft` with the metric evidence that justifies them.
- Keep caveats close to the claim they affect, and omit caveats that do not change interpretation.
- Use charts, tables, scorecards, or KPI cards only when they make the takeaway easier to understand and remain readable in the final delivery context.
