---
name: x-openai-view-refactor-7fc3b20
description: Refactor macOS SwiftUI views and scenes into stable structure. Use when splitting large views, tightening scene state, or narrowing AppKit escapes.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# View Refactor

## Overview

Refactor macOS views toward small, explicit, stable scene and view types. Default
to native SwiftUI for layout, selection, commands, and settings. Reach for AppKit
only at the narrow edges where desktop behavior truly requires it.

## Core Guidelines

### 1) Model scenes explicitly

- Break the app into meaningful scene roots: main window, settings, utility windows, inspectors, or menu bar extras.
- Do not let one giant root view silently own every desktop surface.

### 2) Keep a predictable file shape

- Follow this ordering unless the file already has a stronger local convention:
- Environment
- `private`/`public` `let`
- `@State` / other stored properties
- computed `var` (non-view)
- `init`
- `body`
- computed view builders / other view helpers
- helper / async functions

### 2b) Split files by responsibility

- For non-trivial apps, do not keep the full app, all views, models, stores, networking clients, process clients, and helpers in one Swift file.
- Accept a single Swift file only for tiny throwaway examples or snippets: roughly under 50 lines, one screen, no persistence, no networking/process client, and no reusable models.
- Use `App/<AppName>App.swift` for the `@main` app and `AppDelegate` only.
- Keep `Views/ContentView.swift` focused on root layout and composition; move feature UI into files such as `Views/SidebarView.swift`, `Views/DetailView.swift`, and `Views/ComposerView.swift`.
- Move value types and selection enums into `Models/*.swift`, stores into `Stores/*.swift`, app-server/network/process clients into `Services/*.swift`, and small formatters/resolvers/extensions into `Support/*.swift`.
- Keep files small and named after the primary type they contain.

### 3) Prefer dedicated subview types over many computed `some View` fragments

- Extract meaningful desktop sections like sidebar rows, detail panels, inspectors, or toolbar content into focused subviews.
- Keep computed `some View` helpers small and rare.
- Pass explicit data, bindings, and actions into subviews instead of handing down the whole scene model.

### 4) Keep selection and layout stable

- Prefer one stable split or window layout with local conditionals inside it.
- Avoid top-level branch swapping between radically different roots when selection changes.
- Let the layout be constant; let state drive the content inside it.

### 5) Extract commands, toolbars, and actions out of `body`

- Do not bury non-trivial button logic inline.
- Do not mix command routing, menu state, and layout in the same block if they can be named clearly.
- Keep `body` readable as UI, not as a desktop view controller.

### 6) Use scene and app storage intentionally

- Use `@SceneStorage` for per-window ephemeral state when it truly helps restore the scene.
- Use `@AppStorage` for durable preferences, not transient UI toggles that only matter in one window.
- Keep scene-owned state close to the scene root.

### 7) Keep AppKit escape hatches narrow

- If a representable or `NSWindow` bridge exists, isolate it behind a small wrapper or helper.
- Do not let AppKit references spread through unrelated SwiftUI views.
- If the bridge starts owning the feature, re-evaluate the architecture.

### 8) Observation usage

- For `@Observable` reference types on modern macOS targets, store them as `@State` in the owning view.
- Pass observables explicitly to children.
- On older deployment targets, fall back to `@StateObject` and `@ObservedObject` where needed.

## Workflow

1. Identify the current scene boundary and whether the file is trying to do too much.
2. Reorder the file into a predictable top-to-bottom structure.
3. Extract desktop-specific sections into dedicated subview types.
4. Stabilize the root layout around selection, scenes, and commands rather than top-level branching.
5. Move action logic, command routing, and toolbar behavior into named helpers or separate types.
6. Tighten any AppKit bridge so the imperative edge is small and explicit.
7. Keep behavior intact unless the request explicitly asks for structural and behavioral changes together.

## Refactor Checklist

- Split oversized view files before adding more UI.
- Move pure models, identifiers, and selection enums out of view files.
- Move `Process`, `URLSession`, app-server, and platform client code out of SwiftUI views into `Services/`.
- Keep `AppDelegate` and the `@main` app entrypoint minimal.
- Build after each major split so compile errors stay local.

## Common Smells

- A root view that mixes window scaffolding, settings, toolbar code, command handling, and detail layout.
- A single app file that mixes app entrypoint, root layout, feature views, models, stores, service clients, and support extensions.
- iOS-style push navigation forced into a Mac sidebar-detail problem.
- Several booleans for mutually exclusive inspectors, sheets, or utility windows.
- AppKit objects passed through many SwiftUI layers without a clear ownership reason.
- Large computed view fragments standing in for real subviews.

## Notes

- A good macOS refactor should make scene structure, selection flow, and command ownership obvious.
- When the problem is fundamentally a missing desktop pattern, use `swiftui-patterns`.
- When the problem is fundamentally a boundary with AppKit, use `appkit-interop`.
