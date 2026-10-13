---
name: x-openai-posthog-ccb5fde
description: Analyze product data and manage product tooling in PostHog. Use when the user wants product analytics or insights, HogQL/SQL queries, feature flags, experiments and A/B tests, error tracking, session replay, surveys, LLM analytics, dashboards, data warehouse, or PostHog documentation.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# PostHog

## Overview

This skill provides a structured workflow for working with PostHog from an agent host. First verify that a PostHog MCP connector or official API client is authenticated so the PostHog tools are available for analytics, feature flags, experiments, error tracking, and more.

PostHog is an all-in-one product platform. The same project's data backs every surface below, so most questions can be answered by querying analytics or running HogQL, and most product changes (flags, experiments, surveys) can be made directly.

**Prefer live tools over pre-trained knowledge.** Your baked-in knowledge of PostHog's API, HogQL functions, and tool shapes may be outdated. The connected PostHog app advertises its own skills and tools at runtime and asks clients to *prioritize its skills over raw tools* — discover and follow those rather than guessing. When in doubt about syntax, limits, or product behavior, use the documentation-search tool.

## Prerequisites
- The PostHog app must be connected and accessible via OAuth.
- Confirm which PostHog organization and project the request targets before reading or writing.
- Self-hosted users connect against their own instance during the app's OAuth flow.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

### Step 0: Connect the PostHog app (if not already configured)

If PostHog tools are unavailable, pause and ask the user to connect the PostHog app:

1. Enable the bundled PostHog app for this plugin or session.
2. Complete the PostHog OAuth flow if prompted, and select the correct organization/project.
3. Refresh or restart the current host only if its documented tool-discovery flow requires it. If no connector or authorized API access is available, report the blocked capability.

After the app is connected, finish your answer and tell the user to retry so they can continue with Step 1.

### Step 1
Clarify the user's goal and scope (e.g., a metric over a time range, a funnel, a new feature flag, an experiment readout, an error investigation). Confirm the target project, date range, event/property names, and any filters or cohorts.

### Step 2
Discover the available PostHog skills/tools the connected app exposes and pick the right one for the task. Resolve identifiers (project ID, flag key, experiment ID, insight/dashboard ID, error issue ID) before calling tools. For anything involving syntax, function names, or product behavior, search the docs first.

### Step 3
Execute PostHog tool calls in logical batches:
- **Read first** — list/get/query (insights, events, HogQL/SQL, error issues) to build context.
- **Write next** — create or update flags, experiments, surveys, dashboards, or insights with all required fields.
- For destructive or broad changes (e.g., toggling a flag in production, ending an experiment), state the impact and confirm before applying.

### Step 4
Summarize results with concrete numbers and links to the PostHog UI where available, call out caveats (sampling, person-on-events timing, date ranges), and propose next actions.

## Capability Map

Use this to route a request to the right PostHog surface, then discover the exact tool the app exposes for it.

| If the user wants to… | PostHog surface |
| --- | --- |
| Answer a metric/trend/funnel/retention/path question | Insights & queries (trends, funnels, retention, paths, lifecycle, stickiness) |
| Run arbitrary SQL over events/persons | HogQL / SQL execution |
| Create, toggle, or audit a feature flag | Feature flags |
| Launch or read out an A/B test | Experiments |
| Investigate a bug or exception | Error tracking (issues + events) |
| Watch how users actually behave | Session replay |
| Gather qualitative feedback (NPS, surveys) | Surveys |
| Track LLM cost/latency/usage | LLM analytics |
| Build or update a dashboard | Dashboards & insights |
| Connect or query external data | Data warehouse |
| Look up how something works in PostHog | Documentation search |

## HogQL & Querying Tips
- HogQL is PostHog's SQL dialect over the events/persons schema. Read the data schema before writing queries, and confirm event and property names exist.
- With person-on-events enabled, `person.properties.*` on the events table reflect the value at ingestion time, not the person's current value — the same person can show different values across events. Don't build workarounds for "query-time" person properties.
- Respect the project timezone when bucketing by day.
- Start narrow (small date range, limited rows), validate, then widen.

## Tips for Maximum Productivity
- Batch related reads before writes; confirm identifiers up front.
- Use natural-language asks where the app supports them ("signups by week this quarter").
- Reference prior insights/dashboards instead of rebuilding from scratch.
- For experiments and flags, double-check rollout conditions and targeting before enabling.

## Troubleshooting
- **Tools missing**: re-run the app connection/OAuth flow (Step 0); verify org/project access.
- **Empty or surprising results**: re-check event/property names, date range, filters, and timezone; confirm the events exist via a small query.
- **Permission errors**: confirm the connected account has access to the target project and the action (some changes require elevated roles).
- **Unsure about syntax or limits**: search the PostHog docs rather than guessing.
