---
name: x-openai-user-context-4975b4c
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Initialize, inspect, save, update, forget, export, or explicitly reset the Public Equity Investing plugin's local user context, source setup, or optional automation setup. Use only when the user explicitly asks to manage Public Equity Investing saved preferences, source pointers, context storage, or recurring automation.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Public Equity Investing User Context

This skill owns the Public Equity Investing plugin's local user-context storage foundation and explicit-only onboarding contract. It is intentionally narrow: it can initialize, inspect, save, update, forget, export, or explicitly reset local context, interpret the next onboarding action, guide the four-step intro/defaults -> connectors/plugins -> automation -> hero-workflow flow, and configure user-approved automations. Ordinary Public Equity Investing workflows do not invoke this skill by default; saved context and source setup are optional accelerators, not a pre-answer gate.

## State Files

Store Public Equity Investing state only in the user-approved directory passed through `--state-dir` or `PUBLIC_EQUITY_STATE_DIR`. No default host home is assumed. For example:

```text
<confirmed-state-directory>/
```

The storage foundation owns only:

```text
user-context.md
onboarding-state.json
```

Do not create `category-state.json`.

## Initialize

When the user explicitly asks to initialize Public Equity Investing user context, run `python3 scripts/init_user_context_state.py --state-dir "<confirmed-state-directory>"` with the shell working directory set to this skill's directory. Set the working directory before the first attempt; do not probe alternate relative paths.

The initializer creates missing state files from bundled templates and preserves existing files unless the user explicitly requests overwrite behavior.

## Inspect

When the user explicitly asks to inspect saved Public Equity Investing context, run `python3 scripts/user_context_preflight.py --state-dir "<confirmed-state-directory>"` with the shell working directory set to this skill's directory. Set the working directory before the first attempt; do not probe alternate relative paths.

Use the returned read-only JSON envelope to summarize initialization status, onboarding status, the deterministic `next_action`, the lightweight `onboarding_progress`, and empty memory categories. Treat `user-context.md` as user-editable durable context and `onboarding-state.json` as operational scaffolding.

## Save Update Or Forget

When the user explicitly asks to remember, save, update, forget, export, or apply durable Public Equity Investing preferences or source pointers, follow `references/plugin-memory.md` from this skill's directory. Store reusable user-approved context in `user-context.md`; keep live company updates and operational connector state out. Initialize missing state only when a save needs persistence.

## Onboarding

When the user explicitly asks to set up, resume, defer, quiet, or complete Public Equity Investing onboarding, follow `references/onboarding.md` from this skill's directory. Use the inspection helper's `next_action` as the current step and render its `copy_ref` template substantially verbatim. Keep the visible flow to four steps: intro and lightweight defaults, connectors and plugins, one optional automation, then a three-option hero-workflow chooser. Capture broader durable preferences only when the user explicitly asks or supplies them naturally.

## Source Category Vocabulary

`plugin-author-config/source-category-config.json` reserves static Public Equity Investing source category ids, labels, and preference hints for explicit setup/status work. The inspection helper exposes those categories as `source_category_plan` and echoes any setup-owned routes already saved under `onboarding-state.json` `connector_confirmation`. Ordinary workflow skills use the router's cross-skill runtime contract and `.app.json` categories instead of reading this helper first. Use `references/source-category-runtime.md` from this skill's directory for the source-setup boundary. Inspection does not prove source readiness, select routes, inspect connectors, or create `category-state.json`.

## Optional Automations

`plugin-author-config/automation-config.md` defines the small author-owned automation menu. When the user explicitly asks for a recurring Public Equity Investing workflow or accepts the optional onboarding automation step, follow `references/automation.md` from this skill's directory. Do not create, update, pause, resume, or remove automations during ordinary workflow work.

## Reset

When the user explicitly asks to reset Public Equity Investing user context, run `python3 scripts/reset_user_context_state.py --state-dir "<confirmed-state-directory>"` with the shell working directory set to this skill's directory. Set the working directory before the first attempt; do not probe alternate relative paths.

The reset helper moves active state files into a timestamped sibling backup directory before clearing them from the active state directory.

## Current Boundary

- The Public Equity Investing router and focused workflow skills do not run `scripts/user_context_preflight.py` during ordinary workflow work.
- Do not initialize state merely because another Public Equity Investing skill runs.
- Do not mutate state when running the read-only inspection helper.
- Do not inspect apps, connectors, plugins, `.app.json`, or source readiness during saved-context inspection.
- During user-approved explicit Source Setup, follow `references/source-category-runtime.md` from this skill's directory.
- During user-approved explicit automation setup or maintenance, follow `references/automation.md` from this skill's directory.
- Do not invoke onboarding unless the user explicitly asks for saved-context setup or management.
- Do not create or modify automations unless the user explicitly asks or accepts the optional automation setup step.
- Do not add, read, or migrate `category-state.json`. The reset helper may back up and clear an older copy during an explicit reset.
