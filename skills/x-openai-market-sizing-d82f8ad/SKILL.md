---
name: x-openai-market-sizing-d82f8ad
description: Estimate market, segment, or opportunity size with transparent assumptions and uncertainty. Use for TAM/SAM/SOM, sizing scenarios, or comparing the scale of possible opportunities.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Related Skills

Resolve a visualization skill (upstream name: `visualize-data`), plotting library, or artifact API when the sizing result needs a chart or figure. Verify the actual capability and apply visual QA.

Use an installed report-building skill (upstream name: `build-report`) or an available document/file API to package the final estimate, assumptions, sensitivity, caveats, and source context whenever this skill is selected, unless the user explicitly requests an inline, chat-only, brief/no-artifact answer, asks not to create a report/file/artifact, or selects another primary artifact.

# Market Sizing

Use this skill to produce a defensible estimate of a market or opportunity from connected context, public sources, transparent assumptions, and auditable calculations. The job is to define the market, choose a sound sizing method, distinguish evidence from assumptions, test sensitivity, and state what would most improve confidence.

## Skill Configuration

### Source Discovery And Verification

Use the relevant semantic layer as a starting map, not a boundary.

1. **Explore all possible sources.** Search every connected or provided source that could contain task-relevant data or change the interpretation. Within each structured-data source, run fresh catalog or metadata discovery for relevant schemas, datasets, tables, views, models, and metrics. Known sources, tables, dashboards, and semantic mappings are starting points, not stopping points.
2. **Compare duplicates and conflicts.** When sources overlap or disagree, compare ownership, freshness, definition, grain, coverage, and directness. Use the best authoritative source, or combine complementary sources when needed. Note material conflicts, explain why the selected source or sources control the answer, and verify selected data through live reads before concluding.

### Source Access Guardrail

Before querying sources, building artifacts, or drawing conclusions, determine whether the answer requires a specific source of truth.

If a required source is unavailable, stop that path. Tell the user what source is needed, ask them to make it available or provide a reviewed fallback, and do not treat weaker substitutes as equivalent.

If the missing source is only optional enrichment, continue with the strongest available evidence and label the gap when it materially affects the answer.

Clarify with the user when a missing input would materially change the estimate or recommendation. Otherwise make a reasonable assumption, state it, and proceed.

## Workflow

### 1. Frame The Market Or Opportunity

Define the market or opportunity boundary before estimating:

- What is being sized, for example a product category, workflow, problem, use case, or category of activity.
- Where and when it applies, for example geography, segment scope, time horizon, or market maturity.
- Who or what counts as part of the market, for example the relevant population, unit of demand, transaction type, or included activity.
- How the opportunity is measured, for example spend, revenue, volume, value created, or another unit that fits the question.
- What kind of sizing answer the user needs, for example TAM/SAM/SOM, market entry, expansion upside, spend pool, revenue pool, population count, or unit volume.

### 2. Choose A Starting Sizing Approach And Inputs

Pick the simplest sound sizing approach for the question, then sketch the calculation chain and the major inputs the estimate will depend on.

A top-down model works when reliable aggregate market data exists; a bottom-up model works when the market can be built from observable units and assumptions; a value-based model works when the estimate should start from the value created rather than a published market total. Use a mixed approach only when cross-checking would materially improve confidence. If more than one approach fits, briefly explain which one you trust most and why.

Expect the first approach to change if source checks show that another model would be more defensible.

### 3. Gather Sources For The Inputs

Choose sources based on the inputs the estimate depends on most.

Start with user-named sources when provided. Then use the strongest available evidence for each major input from the starting approach. Discover authenticated database/SQL connectors for structured data and authorized document, communication, or BI connectors for business context. The upstream labels `~~structured_data`, `~~company_docs`, `~~team_communication`, and `~~dashboards_or_bi` describe source categories; they are not executable tools or guaranteed connections. When an input depends on the outside market, use public sources for benchmarks, population estimates, comparable markets, or proxy assumptions.

Use an installed business-context skill when available; otherwise inspect discovered source catalogs and supplied context to resolve the source of truth, business meaning, and assumptions.

If the strongest source is unavailable or thin, continue with a transparent proxy assumption only when the estimate is still useful. Label the gap and explain how it affects confidence.

### 4. Separate Facts From Assumptions

Keep sourced facts, inferred estimates, and judgment calls distinct in the model. When exact data is unavailable, use a defensible proxy, explain why it is reasonable, and note the confidence level. Ground assumptions in evidence about how the market actually behaves, what can realistically change, and what determines the size of the opportunity.

### 5. Build The Model

Make the model easy to inspect and adjust.

The model should make these elements easy to audit or revise:

- market definition and measurement unit
- assumptions and source context
- calculation chain and derived values
- base case, material ranges, and sensitivity logic
- validation priorities

For each major input, make the source path visible: structured data, context lane, public source, user-provided input, or proxy assumption.

Keep derived values traceable to formulas or code rather than hardcoded outputs.

Use an installed notebook skill or a verified Python/R/notebook runtime when code is needed for harmonization, calculations, sensitivity analysis, or reusable modeling. If no runtime exists, report execution as blocked and retain an unexecuted model plan. Keep formulas, inputs, intermediate calculations, and sensitivity logic inspectable.

Use an installed spreadsheet skill or verified workbook API when the user requests a spreadsheet, workbook, or Google Sheets deliverable, or when a market-sizing model would materially benefit from editable assumptions, sensitivity tables, charts, or polished workbook formatting.

### 6. Test Sensitivity

Identify the assumptions that move the estimate most.

Show how the estimate changes when those assumptions move up or down. Prefer simple, decision-useful sensitivity analysis over exhaustive scenario sprawl.

Use ranges when uncertainty is material. Do not hide uncertainty behind a single point estimate when the inputs are thin.

### 7. State The Estimate And Validation Priorities

End by handing the estimate, method, key assumptions, uncertainty, and next validation priorities to the resolved report-building capability unless the user explicitly waives report creation or selects another primary artifact. This handoff is mandatory when no explicit human waiver was given; do not infer a waiver because the user asked for an estimate or did not use the word "report". This workflow owns the sizing model and conclusion; the resolved report capability owns structure, visuals, evidence placement, and delivery. If artifact creation is unavailable, report blocked delivery and provide the completed model content without claiming an artifact was created.

Before handoff, make the market-sizing conclusion explicit:

- market definition and measurement unit
- estimate or range
- method and calculation chain
- key assumptions and source support
- main uncertainty drivers and sensitivity takeaways
- validation priorities and practical interpretation for the user's decision

If source coverage is thin, say which major inputs rely on proxy assumptions and what source would most improve them.

Use an installed validation skill or independently check formulas, assumptions, caveats, and source support before sharing.

Pass visual intent and evidence to the resolved report/visualization capability. Verify chart selection, labels, source support, and output; if no capability is available, report the blocked visual rather than claiming it was rendered.
