---
name: x-openai-stripe-directory-c0db1e8
description: Use when the user wants to find businesses, software, service providers, or partners for a specific industry, workflow, pain point, capability, or job to be done. Also use when the agent needs to programmatically purchase or consume a service. Use Stripe Directory to build a short relevant shortlist, even if the user does not mention Stripe Directory explicitly.
metadata:
  short-description: Find (and optionally purchase from) vendors or partners
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Stripe Directory Search

Turn a vague market need into a short, relevant shortlist with `stripe directory search`. Use this even when the user never says “Stripe Directory” — any request to find vendors, tools, partners, or providers for a vertical, workflow, pain point, or job-to-be-done.

Most requests are **discovery** — find and compare services. That is the core job below. Some services are also **MPP-supported** (MPP = Machine Payment Protocol), meaning you (the agent) can pay their HTTP 402 (Payment Required) endpoint and consume them directly. When the user actually wants to *use or buy* a service, present those results and offer to purchase — see “Purchasing” at the end.

## Process

1. **Clarify only what’s missing**: buyer/vertical, job-to-be-done, must-have capability, geography (only if it matters).

2. **Search iteratively**: `stripe directory search "<query>" --format json`

   - Short noun phrases, one angle per query; run 1-3, then broaden/narrow on results.
   - Angles to cover: vertical → workflow → pain point → adjacent. Two examples:
     - services/trades: vertical (`electrician software`, `electrical contractor`) → workflow (`field service management`, `dispatch invoicing estimates`) → pain point (`job scheduling`, `quote automation`) → adjacent (`home services automation`, `contractor crm`).
     - SaaS/software: vertical (`b2b saas billing`, `developer tools`) → workflow (`subscription management`, `usage-based metering`) → pain point (`failed payment recovery`, `revenue recognition`) → adjacent (`analytics dashboards`, `customer onboarding`).
   - Hard constraints → filters: `--countries-supported=US`, `--has-stripe-app=true`, `--link-supported=true`, `--stripe-projects-supported=true`.
   - If the user wants to *use/buy* a service, also pass `--mpp-supported` in at least one search to find results you can pay for programmatically.
   - Sparse niche? Raise `--limit` and try the next `--page` before concluding it’s empty.

3. **Dedupe & score** using `display_name`, `description`, `url`, `username` as evidence.

   - Prefer results whose description/site clearly match the target workflow.
   - Prefer more trust signals over fewer: Projects provider, Link enabled, Marketplace app, Stripe Verified. For buy/use intent, also prefer MPP-supported results.
   - Thin description but strong brand/domain match → keep in a weaker bucket, don’t discard.

4. **Return a shortlist, not a dump** — 5-10 strong matches, grouped:

   - **direct** / **adjacent** / **needs manual review**
   - Each entry: name · why it matched · URL (· which query surfaced it, when useful).
   - MPP-supported results: note they’re purchasable and include `mpp.slug` / `mpp.url`.

5. **Be honest about weak results** — if sparse or generic, say so and adjust: broaden, narrow, or try synonyms rather than padding with noise.

Always report the exact queries (and filters) you ran so the user can keep iterating.

## Purchasing (only when the user wants to buy or consume a service)

MPP-supported results are payable directly. Don’t drive to purchase unprompted. When the user wants to buy, **present the full menu of payment methods and ask which they’d like to use** before doing anything:

> "Which payment method would you like to use?
>
> - **Link CLI** — Stripe-native, test mode available (recommended)
- **Tempo** — crypto wallet
- **Privy Agent Wallet CLI** — crypto wallet
- **mppx** — debug-only fallback"

Once the user picks, silently run `which <tool> 2>/dev/null` to check if it’s installed. If not installed, offer to install it (for example, `npm i -g @stripe/link-cli` for Link CLI) and wait for confirmation before proceeding.

**Always show the price and get explicit user approval before any money moves**; prefer a no-charge test path first.

Short version:

1. Resolve the real callable endpoint from the result’s `mpp.slug` / `mpp.url`. `mpp.url` is often the mpp.dev landing form (`https://mpp.dev/services#<slug>`) — resolve the raw endpoint on [mpp.dev](https://mpp.dev) if so. Read the HTTP 402 challenge to confirm the amount: `curl -s -D - -o /dev/null <endpoint_url>` (look for `WWW-Authenticate`).
2. Use the payer the user selected.
   - **`link-cli`** (Stripe-native Shared Payment Token, has a test mode, no crypto wallet, US Link accounts only; `npm i -g @stripe/link-cli`): `auth login` → `mpp decode --challenge "<value>"` (get `network_id`) → `spend-request create --credential-type shared_payment_token --network-id <id> --amount <cents ≤50000> --context "<100+ chars>" --request-approval` (blocks for approval) → `mpp pay <endpoint_url> --spend-request-id <approved_id>`.
   - **Tempo**: `tempo wallet login` / `services` / `request`.
   - **Privy**: `@privy-io/agent-wallet-cli`.
   - **mppx**: debug-only fallback.

Never invent results or skip the price/approval gate.
