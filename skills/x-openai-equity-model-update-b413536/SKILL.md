---
name: x-openai-equity-model-update-b413536
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Safely update public-company Excel model copies from source-to-model maps; emits XLSX as the hero artifact and CSV/log/manifest as support. Do not use for pure earnings notes or broad workbook audits.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Equity Model Update

## Skill Configuration

### Common Skill Instructions

MANDATORY: Before searching connectors, retrieving evidence, or drafting output, read and apply the shared runtime contract in `../public-equity-investing/SKILL.md## Cross-Skill Runtime Contract`. Then check the router skill map and `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/plugin-routing-playbook.md` for adjacent skills that should be sequenced with this workflow. Do not run user-context setup or inspection during ordinary workflow work; route only explicit saved-context, source-setup, onboarding, or automation-setup requests to `../x-openai-user-context-4975b4c/SKILL.md`.

### Source Resolution

Load `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/workflow-source-resolution.md`. Resolve only the categories needed for this workflow: `company_filings_ir`, `earnings_transcripts_presentations`, `internal_research`, `portfolio_models_trackers`, and `market_data_estimates`. Use the shared runtime contract to map each attempted category to an available app, connector, file, export, or user-provided input.

## Relevant Dependency Categories

These are the source categories most likely to matter for this workflow. Use the router contract to resolve only the categories the task actually needs, prefer user-named sources first, and state any material source limitation.

- `Portfolio Models & Trackers`
- `Company Filings & IR`
- `Market Data & Estimates`
- `Earnings Transcripts & Events`

## Deliverable Intake

Before source gathering or analysis for a new substantive hero deliverable, load `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/deliverable-intake-policy.md` and use its adaptive intake through the current host's available question capability (`request_user_input` only when actually exposed), or ordinary chat when that tool is absent for materially unresolved format, depth, audience/use, or focus choices. Reuse resolved preferences in downstream steps; when acting only as input to an owning workflow, do not re-prompt.

Use this skill when the real job is updating a listed-equity model from reported actuals, guidance, consensus, transcript/KPI disclosures, or user assumptions, then translating the changed lines into estimate revisions, valuation support, target-price implications, and PM action.

## Use When

Use this skill to refresh public-company model inputs as a controlled source-to-model process. It owns safe copied-workbook updates, source-to-model maps, change logs, stale/missing data flags, pre/post-print model update checklists, and support CSV artifacts.

When an Excel model is supplied, default to a copied updated workbook or workbook control pack as the primary human deliverable. CSV, run-log, JSON citations, and manifest outputs are support artifacts. The user-facing handoff should lead with the updated `.xlsx` package, model implication, estimate-revision path, valuation/target-price read-through, source posture, changed/blocked cells, and update dashboard; for substantial reusable update packages, render an HTML dashboard/report alongside the workbook or hand off to the relevant workbook builder so the workbook `Cover` carries the insight view.

For dashboard handoffs, use `references/DASHBOARD_PACK.md`. `equity-model-update` owns source-to-model mapping, changed-line interpretation, stale/missing flags, and model implication, valuation read-through, and PM action implication; `dashboard-builder` owns the shell/rendering/QA. Build a `public_equity_investing_dashboard.v1` payload as an internal renderer input, and keep JSON/Markdown/CSV/run-log support files behind the HTML dashboard unless explicitly requested.

## Do Not Use For

Use neighboring skills for pure earnings notes, post-print interpretation, formula audits, raw cleanup, trade pitches, and memo prose.

## When To Invoke Support

Load `shared/support-layer-routing-contract.md` when support services are needed. Use `financial-source-of-truth` for reported actuals, guidance, consensus, source timestamps, and claim labels. Use `financials-normalizer` before building the source-to-model map from messy release tables, transcript KPI tables, segment schedules, share-count support, net debt, or capital allocation data. Use `excel-data-cleaner` before relying on malformed model-update exports. Use `model-audit-tieout` for formula integrity, recalc/cache state, external links, circularity, and final tie-out. Support artifacts stay secondary to the copied workbook/control pack and update dashboard.

## Workflow

1. Identify company, period, event, user model status, and decision.
2. Use user files first, company primary sources next, connected consensus/market data when available, then public fallback.
3. Label numbers as reported actual, guidance, consensus, user estimate, agent estimate, market-implied, inferred, or judgment.
4. Map each source metric to a model line and assign `mapping_treatment` before calculating a delta: `safe_update` for true input updates, `reference_only` for facts that inform the review but cannot replace a model input, `missing_model_architecture` when the workbook lacks the required schedule, `assumption_required` when an investor judgment is needed, or `rebuild_required` when the model cannot express the update safely. Only `safe_update` rows may populate proposed model values or estimate-change deltas.
5. For EPS model lines, separate reported GAAP EPS, adjusted/operating EPS, recurring EPS drivers, tax/share-count effects, and below-the-line/non-recurring items before updating forward EPS.
6. If a workbook is supplied, run a preflight and write only to a copied workbook. Never mutate the original workbook. Update mapped non-formula input cells only when sheet/cell, prior value, new value, source ID, freshness, and confidence are sufficient.
7. If workbook editing is unsafe, under-mapped, protected, formula-targeted, stale, or ambiguous, create a workbook-based control pack with `Update_Cover`, `Source_Map`, `Rebuild_Requirements`, `Change_Log`, `Tie_Out`, and `Stale_Data` review tabs instead of editing model cells.
8. When the supplied workbook lacks the operating schedules required for an estimate refresh, state that refreshed estimates and valuation are unavailable, retain cached legacy valuation only as a stale reference, and identify the missing architecture or rebuild requirements. Do not present reported quarterly metrics or net-cash reference facts as changes to an annual DCF output formula.
9. Surface recalc/cache warnings: formula workbook versus cached values, stale workbook calculation state, external links, formula overwrite risk, source timestamp, and whether Excel/Sheets recalculation is still required. Require recalculation after copied input edits that affect formulas; do not require recalculation merely because an unchanged control-pack workbook contains cached formula values. Never imply formulas were recalculated if the runtime only inspected cached values or edited copied input cells.
10. Route formula integrity, external-link checks, circularity, final tie-out, and rebuilt model work to `model-audit-tieout`, DCF, three-statement, comps, or public-model builders as appropriate.
11. When a final presentation workbook is restyled, renamed, or exported after materialization, make that final `.xlsx` the only user-facing primary workbook. Update `run_log.json`, `manifest.json`, and `model_update_citations.json` to point to the final workbook and its final sheet names before handoff; do not lead with an unstyled intermediate control pack.

## Sub-agent decomposition

For complex medium/large requests, use sub-agents where available; otherwise emulate the split as named workstreams. Suggested lanes: new source extraction, estimate/guidance deltas, model input changes, source labels, and change-log QA. Keep this skill as the lead: reconcile conflicts, source labels, assumptions, open items, final QA, and the user-facing answer.


## Executable Contract

Safe copied-workbook helper:

```bash
python scripts/materialize_workbook_update.py input.csv --workbook uploaded_model.xlsx --out output
```

Default workbook modes:

- `xlsx_update_copy`: updates safe mapped input cells in `updated_model.xlsx`.
- `xlsx_control_pack`: preserves model cells, opens on the `Update_Cover` review tab, and adds review tabs in `model_update_control_pack.xlsx`.
- `csv_update_map_export`: mapping/log fallback when no workbook is supplied or the user explicitly asks for support artifacts only.

Support-only helper:

```bash
python scripts/materialize_model_update.py input.csv --out output
```

Workbook outputs: `updated_model.xlsx` or `model_update_control_pack.xlsx`, plus `source_to_model.csv`, `change_log.csv`, `tieout_checklist.csv`, `model_update_citations.json`, `run_log.json`, and `manifest.json`. The manifest marks the workbook as `primary_human_deliverable`; if a polished successor workbook is exported, promote that successor consistently across the manifest, run log, and model citations.

The workbook helper reports `calc_chain_present`, `formula_cell_count`, `cached_formula_value_count`, `calc_mode`, and `recalc_required` in the run log and cover tab. It separately labels artifact readiness and model readiness: a completed control pack may be ready for review while the model remains not updated and requires mapping or rebuild. If mapped inputs are changed and formulas exist, treat downstream formula outputs as stale until Excel/Sheets recalculation and `model-audit-tieout` are complete.

Support-only outputs: `source_to_model.csv`, `change_log.csv`, `tieout_checklist.csv`, `run_log.json`, and `manifest.json`. The run log includes `status`, `model_status`, source basis, warnings, hard failures, output paths, and output manifest. Hard failures: missing `source_id`, missing `model_line`, malformed/empty input. Stale data is flagged.

## Output Standard

Lead with the workbook artifact when a model was supplied. Include model implication, changed cells, blocked cells, source/data-quality note, comparison table when available, KPI/model-driver dashboard, source map, change log, tie-out checklist, and post-print actions.

References: `references/workflow.md`, `references/templates.md`, `references/sector-kpis.md`, `references/executable-contract.md`.

## Equity Valuation PM Standard

Load `shared/equity-valuation-pm-standard.md` and `shared/pm-judgment-heuristics.md` for substantial model, valuation, scenario, model-update, or audit work.

The output must state what the current stock price implies, the variant estimate path, whether upside is driven by fundamentals, multiple expansion, mix, capital return, sentiment, or event probability, what breaks first in downside, what changes target, rating, sizing, hedge, trim, exit, or watchlist status, and what evidence is missing.

Keep equity valuation as the center of gravity. Debt is allowed only as an input to common-equity value through net debt, cost of debt, leverage, liquidity, refinancing risk, or downside equity impairment. Use Credit Markets for bond comps, loan comps, CDS, spread/yield relative value, covenant-package analysis, debt-security valuation, recovery waterfall, restructuring valuation, creditworthiness, private-credit / public-credit instrument underwriting, or distressed claim valuation.
