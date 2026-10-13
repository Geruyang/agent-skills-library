---
name: x-openai-dcf-model-builder-5d6c650
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Use when building public-equity DCF valuation workbooks. Default to the banker formula workbook path for new model builds; use deterministic exports only for controlled support calculations or explicit lightweight runs. Do not use for standalone workbook audits; use model-audit-tieout.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# DCF Model Builder

## Skill Configuration

### Common Skill Instructions

MANDATORY: Before searching connectors, retrieving evidence, or drafting output, read and apply the shared runtime contract in `../public-equity-investing/SKILL.md## Cross-Skill Runtime Contract`. Then check the router skill map and `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/plugin-routing-playbook.md` for adjacent skills that should be sequenced with this workflow. Do not run user-context setup or inspection during ordinary workflow work; route only explicit saved-context, source-setup, onboarding, or automation-setup requests to `../x-openai-user-context-4975b4c/SKILL.md`.

## Relevant Dependency Categories

These are the source categories most likely to matter for this workflow. Use the router contract to resolve only the categories the task actually needs, prefer user-named sources first, and state any material source limitation.

- `Company Filings & IR`
- `Market Data & Estimates`
- `Portfolio Models & Trackers`

## Deliverable Intake

Before source gathering or analysis for a new substantive hero deliverable, load `../../resources/plugins-6ebaff11/plugins/public-equity-investing/shared/deliverable-intake-policy.md` and use its adaptive clarification preflight through the current host's available question tool (or direct conversation when unavailable) for materially unresolved format, depth, audience/use, or focus choices. Reuse resolved preferences in downstream steps; when acting only as input to an owning workflow, do not re-prompt.

Own DCF-specific valuation builds: FCFF/FCFE method choice, WACC or cost of equity, terminal value, EV-to-equity bridge, per-share value, valuation sensitivities, QA checks, and a formula-first XLSX workbook.

## Hard Contract

- Default model-build artifact level is `banker_formula_workbook`; use the formula workbook path for normal public-equity DCF build, refresh, valuation, and model-package requests.
- Formula mode is executed through `scripts/build_banker_formula_workbook.py` and must be labeled `banker_formula_workbook` only when its run log, workbook inspection, and `model_citations.json` prove the formula builder ran successfully.
- Deterministic scripts remain available for controlled computed values, smoke tests, or explicit lightweight support exports. They produce `output/model.xlsx`, `output/plan.json`, `output/run_log.json`, optional support note `output/support_note.md`, and `output/manifest.json`. Legacy `output/report.md` is written only with `--write-report-md`.
- Formula scripts produce `banker_formula_workbook.xlsx`, `banker_formula_workbook_run_log.json`, `model_citations.json`, and `manifest.json` in the selected output directory. The workbook is the hero deliverable; citation JSON, run logs, and manifests are support artifacts.
- Formula and deterministic workbooks must start with a `Cover` tab that functions as an investment landing page: issuer, current price versus implied value, valuation range, case outputs, DCF bridge, WACC/terminal assumptions, sensitivity drivers, source posture, warnings/hard failures, and workbook map.
- `run_log.json` and `manifest.json` are required reliability artifacts; hard failures force `not-decision-ready`.
- Never delete, overwrite, or mutate source data unless explicitly requested. Write new outputs under `output/` or a clearly named copy.
- Keep material inputs source-labeled: `reported`, `company_guidance`, `consensus`, `management_case`, `user_provided`, `connected_app`, `web_research`, `analyst_estimate`, `placeholder`, or `derived`.
- If placeholders, stale data, unsupported WACC, missing share count/net debt, or weak analyst estimates drive value, mark the output no higher than `screen-grade`.

## Routing

Use this skill when the deliverable is a DCF build, refresh, rerun, valuation sensitivity, reverse DCF, or DCF model package. Route away when the primary ask is workbook audit/debug (`model-audit-tieout`), source hierarchy (`financial-source-of-truth`), raw financial normalization (`financials-normalizer`), raw spreadsheet cleanup (`excel-data-cleaner`), expanded stress architecture (`scenario-sensitivity-generator`), trading comps (`comps-valuation`), or memo/deck polish.

For complex tasks, split the work into source-of-truth, accounting normalization, operating forecast, cost of capital, terminal value/ROIC, scenario valuation, and audit workstreams. If sub-agents are unavailable, emulate those workstreams explicitly before running the pipeline.

## When To Invoke Support

Load `shared/support-layer-routing-contract.md` when source/data/QC/style support is needed. Use `financial-source-of-truth` before relying on load-bearing market data, filings, guidance, consensus, share count, net debt, WACC, or terminal assumptions. Use `financials-normalizer` before plan creation when historical financials, KPI schedules, segment data, guidance, consensus/provider exports, share count, net debt, or capital allocation inputs are messy. Use `excel-data-cleaner` before importing malformed tables. Use `model-audit-tieout` for formula integrity, external links, recalc/cache posture, and final tie-out; use `deck-report-qc` only for circulation packs. Support artifacts stay secondary to the formula workbook or HTML report.

## Input Handling

- Preferred input is a `plan.json` matching the schema.
- No context: run `assets/plan_template.json` only as illustrative and label placeholders.
- Named company with no data: gather connected/public data when allowed; otherwise ask targeted questions or build a caveated screen-grade plan.
- Partial context: preserve user assumptions, fill only non-economic structure when obvious, and label gaps.
- Full plan: validate first; do not silently change conclusion-driving assumptions.
- When the investment question turns on an operating KPI such as bookings, GBV, take rate, volumes, users, units, or retention, load `references/industry-playbooks.md` and build from the sector-relevant driver where the workbook supports it. If formula mode cannot represent that driver schedule, disclose the proxy prominently on the Cover or Executive Summary and in Source Notes, and keep the model no higher than `screen-grade`; do not silently substitute a generic revenue CAGR.

## Required Workflow

1. Create or identify a valid `plan.json`.
2. Validate with `python3 scripts/validate_plan.py path/to/plan.json`.
3. Default path: execute `python3 scripts/build_banker_formula_workbook.py path/to/plan.json --output-dir output` and inspect `banker_formula_workbook_run_log.json`.
4. Use `python3 scripts/run_pipeline.py path/to/plan.json` only for controlled computed values, smoke tests, explicit lightweight support exports, or when formula mode fails and the fallback is clearly labeled `deterministic_export`.
5. Review the relevant run log for hard failures, warnings, checks, source basis, workbook inspection, and P0/model handoff.
6. Render and visually inspect the generated workbook before delivery. Confirm that template example data is absent from a named-company model, actual/estimate periods align across tabs, core outputs and sources are legible, and checks disclose any unsupported driver or roll-forward.
7. Deliver the workbook as the hero artifact and link the normalized plan, run log, manifest, citation ledger, and optional support note as audit files.

Smoke test:

```bash
python3 scripts/validate_plan.py assets/plan_template.json
python3 scripts/build_banker_formula_workbook.py assets/plan_template.json --output-dir /tmp/public-equity-investing-dcf-formula
python3 scripts/run_pipeline.py assets/plan_template.json
```

## Formula Mode Guardrail

Load `references/banker-formula-workbook-contract.md` before using formula mode. If the formula builder fails, the template is missing, required tabs/formulas/styles are not present, external links appear, or `model_citations.json` is absent, do not describe any fallback artifact as a banker formula workbook.

## Status Labels

Use exactly: `decision-grade`, `senior-review-ready`, `screen-grade`, `not-decision-ready`, `blocked`. Use `blocked` only before a run log exists; after execution, hard failures mean `not-decision-ready`.

## Deferred Reference Router

Load `references/reference-router.md` only when deeper schema, math, QA, integration, sector, or senior valuation judgment guidance is needed. The router preserves the detailed reference map without loading every reference during invocation.

## Equity Valuation PM Standard

Load `shared/equity-valuation-pm-standard.md` and `shared/pm-judgment-heuristics.md` for substantial model, valuation, scenario, model-update, or audit work.

The output must state what the current stock price implies, the variant estimate path, whether upside is driven by fundamentals, multiple expansion, mix, capital return, sentiment, or event probability, what breaks first in downside, what changes target, rating, sizing, hedge, trim, exit, or watchlist status, and what evidence is missing.

Keep equity valuation as the center of gravity. Debt is allowed only as an input to common-equity value through net debt, cost of debt, leverage, liquidity, refinancing risk, or downside equity impairment. Use Credit Markets for bond comps, loan comps, CDS, spread/yield relative value, covenant-package analysis, debt-security valuation, recovery waterfall, restructuring valuation, creditworthiness, private-credit / public-credit instrument underwriting, or distressed claim valuation.
