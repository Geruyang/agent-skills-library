---
name: x-openai-ios-app-intents-ee07221
description: Design App Intents, app entities, and App Shortcuts for iOS system surfaces. Use when exposing app actions or content to Shortcuts, Siri, Spotlight, widgets, or controls.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# iOS App Intents

## Overview
Expose the smallest useful action and entity surface to the system. Start with the verbs and objects people would actually want outside the app, then implement a narrow App Intents layer that can deep-link or hand off cleanly into the main app when needed.

Read these references as needed:

- `references/first-pass-checklist.md` for choosing the first intent and entity surface
- `references/example-patterns.md` for concrete example shapes to copy and adapt
- `references/code-templates.md` for generalized App Intents code templates
- `references/system-surfaces.md` for how to think about Shortcuts, Siri, Spotlight, widgets, and other system entry points

## Core workflow

### 1) Start with actions, not screens
- Identify the 1-3 highest-value actions that should work outside the app UI.
- Prefer verbs like compose, open, find, filter, continue, inspect, or start.
- Do not mirror the entire app navigation tree as intents.

### 2) Define a small entity surface
- Add `AppEntity` types only for the objects the system needs to understand or route.
- Keep the entity shape narrower than the app's persistence model.
- Add `EntityQuery` or other query types only where disambiguation or suggestions are genuinely useful.

### 3) Decide whether the action completes in place or opens the app
- Use non-opening intents for actions that can complete directly from the system surface.
- Use `openAppWhenRun` or open-style intents when the user should land in a specific in-app workflow.
- When the app must react inside the main scene, add one clear runtime handoff path instead of scattering ad hoc routing logic.
- If the action can work in both modes, consider shipping both an inline version and an open-app version rather than forcing one compromise.

### 4) Make the actions discoverable
- Add `AppShortcutsProvider` entries for the first set of high-value intents.
- Choose titles, phrases, and symbols that make sense in Shortcuts, Siri, and Spotlight.
- Keep shortcut phrases direct and task-oriented.
- Reuse the same action model for widgets and controls when a widget configuration or intent-driven control already needs the same parameters.

### 5) Validate the runtime handoff
- Build the app and confirm the intents target compiles cleanly.
- Verify the app opens or routes to the expected place when an intent runs.
- Summarize which actions are now exposed, which entities back them, and how the app handles invocation.

## Strong defaults

- Prefer a dedicated intents target or module for the system-facing layer.
- Keep intent types thin; business logic should stay in app services or domain models.
- Keep app entities small and display-friendly.
- Use `AppEnum` for fixed app choices such as tabs, modes, or visibility levels before reaching for a full entity type.
- Prefer one predictable app-intent routing surface in the main app scene or root router.
- Treat App Intents as system integration infrastructure, not only as a Shortcuts feature.

## Anti-patterns

- Exposing every screen or tab as its own intent without a real user value.
- Mirroring the entire model graph as `AppEntity` types.
- Hiding runtime handoff in global side effects with no clear app entry path.
- Adding App Shortcuts with vague phrases or generic titles.
- Treating the first App Intents pass as a broad taxonomy project instead of a small useful release.

## Notes

- Apple documentation to use as primary references:
  - `https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available`
  - `https://developer.apple.com/documentation/appintents/creating-your-first-app-intent`
  - `https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences`
- In addition to the links above, use web search to consult current Apple Developer documentation when App Intents APIs or platform behavior may have changed.
- A good first pass often includes one open-app intent, one action intent, one or two entity types, and a small `AppShortcutsProvider`.
- Good example families to cover are:
  - open a destination or editor in the app
  - perform a lightweight action inline without opening the app
  - choose from a fixed enum such as a tab or mode
  - resolve one or more entities through `EntityQuery`
  - power widget configuration or controls from the same entity surface
