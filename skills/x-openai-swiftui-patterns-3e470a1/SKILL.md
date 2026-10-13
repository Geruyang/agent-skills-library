---
name: x-openai-swiftui-patterns-3e470a1
description: Build macOS SwiftUI scenes and components with desktop patterns. Use when shaping windows, commands, toolbars, settings, split views, or inspectors.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# SwiftUI Patterns

## Quick Start

Choose a track based on your goal:

### Existing project

- Identify the feature or scene and the primary interaction model: document, editor, sidebar-detail, utility window, settings, or menu bar extra.
- Read the nearest existing scene or root view before inventing a new desktop structure.
- Choose the relevant reference from `references/components-index.md`.
- If SwiftUI cannot express the required platform behavior cleanly, use the `appkit-interop` skill rather than forcing a shaky workaround.

### New app scaffolding

- Choose the scene model first: `WindowGroup`, `Window`, `Settings`, `MenuBarExtra`, or `DocumentGroup`.
- If the app combines a normal main window and a `MenuBarExtra`, use `WindowGroup(..., id:)` for the primary window when it should appear at launch. Treat `Window(...)` as a better fit for auxiliary/on-demand singleton windows; in menu-bar-heavy apps, a `Window(...)` scene may not present the main window automatically at launch.
- Before creating the scaffold, check whether the workspace is already inside a git repo with `git rev-parse --is-inside-work-tree`. If not, run `git init` at the project root so version control is available from the start. Do not initialize a nested repo inside an existing parent checkout.
- For a new app scaffold, create a project-local `script/build_and_run.sh` for reproducible builds. Configure an IDE Run action only when the current host exposes a documented mechanism. If using Codex specifically, `.codex/environments/environment.toml` and the `build-run-debug` run-button reference describe that product integration; do not create Codex configuration for other hosts.
- Decide which state is app-wide, scene-scoped, or window-scoped before writing views.
- Sketch file and module boundaries before writing the full UI. For any non-trivial app, create the folder structure first and split files by responsibility from the start.
- Use a single Swift file only for tiny throwaway examples or snippets: roughly under 50 lines, one screen, no persistence, no networking/process client, and no reusable models. Anything beyond that should be multi-file immediately.
- Use system-adaptive colors and materials by default (`Color.primary`, `Color.secondary`, semantic foreground styles, `.regularMaterial`, etc.) so the app follows Light/Dark mode automatically. Do not hardcode white or light backgrounds unless the user explicitly asks for a fixed theme, and do not reach for opaque `windowBackgroundColor` fills for root panes by default.
- Pick the references for the first feature surface you need: windowing, commands, split layouts, or settings.

## New App File Structure

For any non-trivial macOS app, start with this shape instead of putting the app,
all views, models, stores, services, and helpers in one Swift file:

- `App/<AppName>App.swift`: the `@main` app type and `AppDelegate` only.
- `Views/ContentView.swift`: root layout and high-level composition only.
- `Views/SidebarView.swift`, `Views/DetailView.swift`, `Views/ComposerView.swift`, etc.: feature views named after their primary type.
- `Models/*.swift`: value models, identifiers, and selection enums.
- `Stores/*.swift`: persistence and state stores.
- `Services/*.swift`: app-server, network, process, or platform clients.
- `Support/*.swift`: small formatters, resolvers, extensions, and glue helpers.

Keep files small and named after the primary type they contain. If a file starts
collecting unrelated views, models, stores, networking clients, and helper
extensions, split it before adding more behavior.

## Pre-Edit Checklist For New App Scaffolds

Before writing the full UI:

1. Choose the scene model.
2. Choose state ownership: app-wide, scene-scoped, window-scoped, or view-local.
3. Sketch file and module boundaries.
4. Create the folder structure before filling in the UI.
5. Keep `script/build_and_run.sh` and any verified host Run configuration separate from app source.

## General Rules To Follow

- Design for pointer, keyboard, menus, and multiple windows.
- Keep scenes explicit. A separate settings window, utility window, or menu bar extra should be modeled as its own scene, not hidden inside one monolithic `ContentView`.
- Prefer system desktop affordances: `commands`, toolbars, sidebars, inspectors, contextual menus, and `searchable`.
- For menu bar apps, keep `MenuBarExtra` item titles and action labels short and scannable. Cap visible menu item text at 30 characters; if source content is longer, truncate or summarize it before rendering and open the full content in a dedicated window or detail surface.
- If a `MenuBarExtra` app should still behave like a regular Dock app with a visible main window/process, install an `NSApplicationDelegate` via `@NSApplicationDelegateAdaptor`, call `NSApp.setActivationPolicy(.regular)` during launch, and activate the app with `NSApp.activate(ignoringOtherApps: true)`. If the app is intentionally menu-bar-only, document that `.accessory` / no-Dock behavior is a deliberate product choice.
- Prefer system-adaptive colors, materials, and semantic foreground styles. Avoid fixed white/light backgrounds in scaffolding and examples unless the requested design explicitly calls for a custom non-adaptive theme.
- Do not paint `NavigationSplitView` sidebars or root window panes with opaque custom `Color(...)` or `Color(nsColor: .windowBackgroundColor)` fills by default. Prefer native macOS sidebar/window materials and system-provided backgrounds unless the user explicitly asks for a custom opaque surface. In sidebar-detail-inspector layouts, let the sidebar keep the standard source-list/material appearance and reserve custom backgrounds for detail or inspector content cards where needed.
- Use `@SceneStorage` for per-window ephemeral state and `@AppStorage` for durable user preferences.
- Keep selection state explicit and stable. macOS layouts often pivot around sidebar selection rather than push navigation.
- Prefer `NavigationSplitView` or a deliberate manual split layout over iOS-style stacked flows when the app benefits from always-visible structure.
- For `List(...).listStyle(.sidebar)` and `NavigationSplitView` sidebars, prefer flat native rows with standard system selection/highlight behavior. Keep rows visually lightweight and Mail-like: at most one leading icon, one strong title line, and one optional secondary detail line in `.secondary`. Avoid stacked metadata rows, repeated inline utility icons, or dense multi-column status text in the sidebar. Reserve card-style and metadata-heavy surfaces for detail or inspector panes unless the user explicitly asks for a highly custom sidebar treatment.
- Keep primary actions discoverable from both UI chrome and keyboard shortcuts when appropriate.
- Use SwiftUI-native scenes and views first. If you need low-level window, responder-chain, text system, or panel control, switch to `appkit-interop`.

For concrete sidebar row and split-view background examples, read
`references/split-inspectors.md`.

## State Ownership Summary

Use the narrowest state tool that matches the ownership model:

| Scenario | Preferred pattern |
| --- | --- |
| Local view or control state | `@State` |
| Child mutates parent-owned value state | `@Binding` |
| Root-owned reference model on macOS 14+ | `@State` with an `@Observable` type |
| Child reads or mutates an injected `@Observable` model | Pass it explicitly as a stored property |
| Window-scoped ephemeral selection or expansion state | `@SceneStorage` when practical, otherwise scene-owned `@State` |
| Shared user preference | `@AppStorage` |
| Shared app service or configuration | `@Environment(Type.self)` |
| Legacy reference model on older targets | `@StateObject` at the owner and `@ObservedObject` when injected |

Choose the ownership location first, then the wrapper. Do not turn simple desktop state into a view model by reflex.

## Cross-Cutting References

- `references/components-index.md`: entry point for scene and component guidance.
- `references/windowing.md`: choosing between `WindowGroup`, `Window`, `DocumentGroup`, and window-opening patterns.
- `references/settings.md`: dedicated settings scenes, `SettingsLink`, and preference layouts.
- `references/commands-menus.md`: command menus, keyboard shortcuts, focused values, and desktop action routing.
- `references/split-inspectors.md`: sidebars, split views, selection-driven layout, and inspectors.
- `references/menu-bar-extra.md`: menu bar extra structure and when it fits.

## Anti-Patterns

- One huge `ContentView` pretending the whole app is a single screen.
- A single Swift file containing the `@main` app, all views, models, stores, networking/process clients, formatters, and extensions. This is acceptable only for tiny throwaway snippets under the new-app threshold above.
- Touch-first interaction models ported directly from iOS without desktop affordances.
- Hiding core actions behind gestures with no menu, toolbar, or keyboard path.
- Building a menu-bar-plus-window app around only a `Window(...)` scene and then expecting the main window to appear at launch. Use `WindowGroup(..., id:)` for the primary launch window and reserve `Window(...)` for auxiliary/on-demand windows.
- Rendering full unbounded document titles, prompts, or message text directly inside a menu bar extra. Menu item labels should stay at or below 30 characters, with longer content moved into a dedicated window or detail view.
- Treating settings as another navigation destination in the main content window.
- Hardcoding `.background(.white)`, `Color.white`, or a fixed light palette in a brand-new scaffold without an explicit design requirement.
- Wrapping each sidebar item in large rounded custom cards inside a `.sidebar` list, which fights native source-list density, alignment, and selection behavior unless the user explicitly asked for a bespoke visual sidebar.
- Building sidebar rows with multiple repeated icons, three or more text lines, or a dense strip of inline metadata counters/timestamps/models. Keep the sidebar row to one icon and one or two text lines, then move richer metadata into the detail pane.
- Painting `NavigationSplitView` sidebars or root window panes with opaque custom color fills by default, instead of letting the sidebar use native source-list/material appearance and reserving custom backgrounds for actual content cards.
- Using push navigation for layouts that want stable sidebar selection and detail panes.
- Reaching for AppKit before the SwiftUI scene and command APIs have been used properly.

## Workflow For A New macOS Scene Or View

1. Define the scene type and ownership model before writing child views.
2. Decide which actions live in content, toolbars, commands, inspectors, or settings.
3. Sketch the selection model and layout: sidebar-detail, editor-inspector, document window, or utility window.
4. Create the file/folder structure for app entrypoint, root layout, feature views, models, stores, services, and support helpers.
5. Build with small, focused subviews and explicit inputs rather than giant computed fragments.
6. Add keyboard shortcuts and menu or toolbar exposure for actions that matter on desktop.
7. Validate the flow with a build and a quick usability pass: multiwindow assumptions, settings entry points, and selection stability.

## Component References

Use `references/components-index.md` as the entry point. Each component reference should include:
- intent and best-fit scenarios
- minimal usage pattern with desktop conventions
- pitfalls and discoverability notes
- when to fall back to `appkit-interop`
