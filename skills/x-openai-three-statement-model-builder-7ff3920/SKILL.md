---
name: x-openai-three-statement-model-builder-7ff3920
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Use when building public-equity three-statement operating model workbooks. Default to the banker formula workbook path for new model builds; use deterministic exports only for controlled support calculations or explicit lightweight runs. Do not use for standalone workbook audits.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Three Statement Model Builder

## Skill Configuration

### Common Skill Instructions

MANDATORY: Before searching connectors, retrieving evidence, or drafting output, read and apply the shared runtime contract in `../public-equity-investing/SKILL.md## Cross-Skill Runtime Contract`. Then check the router skill map and `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/plugin-routing-playbook.md` for adjacent skills that should be sequenced with this workflow. Do not run user-context setup or inspection during ordinary workflow work; route only explicit saved-context, source-setup, onboarding, or automation-setup requests to `../x-openai-user-context-4975b4c/SKILL.md`.

## Relevant Dependency Categories

These are the source categories most likely to matter for this workflow. Use the router contract to resolve only the categories the task actually needs, prefer user-named sources first, and state any material source limitation.

- `Company Filings & IR`
- `Portfolio Models & Trackers`
- `Market Data & Estimates`

## Deliverable Intake

Before source gathering or analysis for a new substantive hero deliverable, load `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/deliverable-intake-policy.md` and use its adaptive preference preflight using the current host's available question tool or plain conversation for materially unresolved format, depth, audience/use, or focus choices. Reuse resolved preferences in downstream steps; when acting only as input to an owning workflow, do not re-prompt.

Own formula-first public-company operating model builds: integrated IS/BS/CF, working capital, PP&E and D&A, retained earnings, debt, revolver-style draws, cash sweep, equity-relevant liquidity/headroom metrics, scenarios, sensitivities, machine checks, and senior-review reporting.

## Hard Contract

- Default model-build artifact level is `banker_formula_workbook`; use the formula workbook path for normal public-equity 3-statement build, refresh, forecast, and operating-model-package requests.
- Formula mode is executed through `scripts/build_banker_formula_workbook.py` and must be labeled `banker_formula_workbook` only when its run log, workbook inspection, and `model_citations.json` prove the formula builder ran successfully.
- Deterministic scripts remain available for controlled computed values, smoke tests, or explicit lightweight support exports. They produce `output/model.xlsx`, `output/plan.json`, `output/run_log.json`, `output/manifest.json`, and optionally `output/support_note.md`. Legacy `output/report.md` is written only with `--write-report-md`.
- Formula scripts produce `banker_formula_workbook.xlsx`, `banker_formula_workbook_run_log.json`, `model_citations.json`, and `manifest.json` in the selected output directory. The workbook is the hero deliverable; citation JSON, run logs, and manifests are support artifacts.
- `output/model.xlsx` must start with a `Cover` tab that functions as a dashboard: model status, scenario outputs, revenue/EBITDA/FCF/cash, liquidity trough, leverage/headroom, source posture, warnings/hard failures, workbook map.
- `run_log.json` and `manifest.json` are required reliability artifacts; hard failures force `not-decision-ready`.
- Never delete, overwrite, or mutate source data unless explicitly requested. Preserve raw tabs/files and write new outputs under `output/` or a clearly named copy.
- Material inputs must be evidence-labeled: `source_reported`, `company_provided`, `connector_sourced`, `public_filing`, `web_verified`, `management_guidance`, `analyst_estimate`, `benchmark`, `assumption`, or `placeholder`.
- If placeholders, stale data, unsupported assumptions, or failed tie-outs remain active, mark the model no higher than `screen-grade`; hard failures mean `not-decision-ready`.

## Routing

Use this skill when the deliverable is a 3-statement build, refresh, rerun, operating model package, or integrated forecast rebuild. Route away when the primary ask is workbook audit/debug (`model-audit-tieout`), source hierarchy (`financial-source-of-truth`), raw financial normalization (`financials-normalizer`), spreadsheet cleanup (`excel-data-cleaner`), valuation (`dcf-model-builder`, `comps-valuation`), public estimate update (`equity-model-update`), Credit Markets research, or memo/deck polish.

For complex builds, split the work into source/evidence, historical normalization, operating drivers, balance sheet and cash, QA, and executive output workstreams. If sub-agents are unavailable, emulate those workstreams and reconcile them into one plan before running scripts.

## When To Invoke Support

Load `shared/support-layer-routing-contract.md` when support services are needed. Use `financial-source-of-truth` for filings, releases, guidance, consensus, market data, and assumption labels; use `financials-normalizer` before building the plan from messy financials, KPI schedules, segment tables, share count, net debt, capital allocation, or provider exports; use `excel-data-cleaner` before relying on malformed workbook tables; use `model-audit-tieout` for workbook logic, external links, recalc/cache posture, and final tie-out. Support artifacts stay secondary to the formula workbook or owning dashboard/report.

## Input Handling

- Preferred input is a `plan.json` matching the schema.
- No context: run `assets/plan_template.json` as illustrative, label placeholders, and cap status at `screen-grade`.
- Partial context: preserve user facts, retain template defaults only when necessary, and label unsupported inputs.
- Full financial package: normalize IS/BS/CF, reconcile the balance sheet, preserve source data, fill the plan, validate, run, then report checks and caveats.

## Required Workflow

1. Build or receive a valid `plan.json`.
2. Validate with `python3 scripts/validate_plan.py path/to/plan.json`.
3. Fix validation errors before running; do not silently default conclusion-changing assumptions.
4. Default path: run `python3 scripts/build_banker_formula_workbook.py path/to/plan.json --output-dir output` and inspect `banker_formula_workbook_run_log.json`.
5. Use `python3 scripts/run_pipeline.py path/to/plan.json` only for controlled computed values, smoke tests, explicit lightweight support exports, or when formula mode fails and the fallback is clearly labeled `deterministic_export`.
6. Verify the relevant workbook, run log, manifest, and, in formula mode, `model_citations.json`.
7. Read the run log; hard failures require `not-decision-ready`.
8. Present the workbook as the hero artifact, with the `Cover` tab carrying the decision read-through, and link the normalized plan, run log, manifest, citation ledger, and optional support note as audit files.

Smoke test:

```bash
python3 scripts/validate_plan.py assets/plan_template.json
python3 scripts/build_banker_formula_workbook.py assets/plan_template.json --output-dir /tmp/public-equity-investing-3s-formula
python3 scripts/run_pipeline.py assets/plan_template.json
```

## Formula Mode Guardrail

Load `references/banker-formula-workbook-contract.md` before using formula mode. If the formula builder fails, the template is missing, required tabs/formulas/styles are not present, external links appear, or `model_citations.json` is absent, do not describe any fallback artifact as a banker formula workbook.

## Status Labels

Use exactly: `decision-grade`, `senior-review-ready`, `screen-grade`, `not-decision-ready`, `blocked`. Use `blocked` only when no reasonable run can be produced before execution.

## Senior Standard

Explain what drives the forecast, what must be true, where cash is consumed, what breaks first in downside, whether EBITDA converts to cash, and which assumptions deserve diligence. Balance-sheet integrity, retained earnings, cash flow linkage, debt roll-forward, PP&E roll-forward, and working-capital roll-forward are non-negotiable.

## Deferred Reference Router

Load `references/reference-router.md` only when deeper schema, math, QA, integration, industry, or forecast judgment guidance is needed. The router preserves the detailed reference map without loading every reference during invocation.

## Equity Valuation PM Standard

Load `shared/equity-valuation-pm-standard.md` and `shared/pm-judgment-heuristics.md` for substantial model, valuation, scenario, model-update, or audit work.

The output must state what the current stock price implies, the variant estimate path, whether upside is driven by fundamentals, multiple expansion, mix, capital return, sentiment, or event probability, what breaks first in downside, what changes target, rating, sizing, hedge, trim, exit, or watchlist status, and what evidence is missing.

Keep equity valuation as the center of gravity. Debt is allowed only as an input to common-equity value through net debt, cost of debt, leverage, liquidity, refinancing risk, or downside equity impairment. Use Credit Markets for bond comps, loan comps, CDS, spread/yield relative value, covenant-package analysis, debt-security valuation, recovery waterfall, restructuring valuation, creditworthiness, private-credit / public-credit instrument underwriting, or distressed claim valuation.
