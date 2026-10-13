---
name: x-openai-react-three-fiber-game-0b8ea0a
description: Build React-hosted 3D browser games with React Three Fiber. Use when the user wants pmndrs-based scene composition, shared React state, and 3D HUD integration inside a React app.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# React Three Fiber Game

## Overview

Use this skill when the 3D runtime lives inside a React application. This is the default React-native 3D path in the plugin and should be preferred over vanilla Three.js when the app shell, settings, storefront, editor surface, or surrounding product already uses React.

Recommended stack:

- `@react-three/fiber`
- `three`
- `@react-three/drei`
- `@react-three/rapier`
- `@react-three/postprocessing`
- `@react-three/a11y` when accessibility-sensitive interaction matters
- DOM overlays in the normal React tree

## Use This Skill When

- the project already uses React
- the 3D scene must share state with the rest of the app
- declarative scene composition is a net gain
- the team wants pmndrs helpers instead of building every helper layer by hand

## Do Not Use This Skill When

- the app is not React-based
- the project wants a cleaner imperative runtime with minimal React coordination
- the problem is asset packaging rather than runtime composition

## Best Fit Scenarios

- 3D configurators and tool-rich browser products
- React apps with embedded game or scene surfaces
- 3D menus, editors, or world maps in an existing React app
- 3D game UIs that depend on shared app state and non-canvas shells

## Core Rules

1. Keep simulation state outside render components.
   - React components should describe scene composition, not become the source of truth for gameplay rules.
2. Use React state and scene state deliberately.
   - Shared UI state can live in app state.
   - High-frequency simulation should not force the whole app through unnecessary React churn.
3. Use pmndrs helpers intentionally.
   - Drei for controls, loaders, helpers, environments, and common scene primitives.
   - `@react-three/rapier` for physics integration.
   - `@react-three/postprocessing` for optional effects.
   - `@react-three/a11y` when the interaction model benefits from accessible scene semantics.
4. Keep HUD, settings, and menus in DOM by default.
5. Keep starter scaffolds visually restrained.
   - Start with one compact objective or status surface and transient prompts.
   - Keep notes, maps, and multi-step checklists collapsed until opened.
   - Do not surround the `Canvas` with equally weighted glass cards.

## Architectural Guidance

- Use a dedicated scene root component that owns the `Canvas`.
- Keep camera rigs and control components isolated from gameplay systems.
- Keep loader and asset wrappers predictable.
- Keep DOM overlays and the 3D scene coordinated through explicit state boundaries.
- If a system needs tight imperative control, isolate it rather than forcing everything into declarative patterns.
- If the scene is immediately playable, keep the initial overlay budget low and let the world do more of the onboarding.

## Anti-Patterns

- Treating React components as the gameplay state store
- Pushing heavy per-frame mutation through broad app state
- Using R3F only because React is available, even when the project needs a cleaner imperative runtime
- Building HUD or inventory UI inside the 3D scene by default
- Shipping an initial scaffold with large cards occupying every side of the viewport

## References

The paths below describe the upstream plugin layout and are not bundled at those locations. Resolve companion skills through the host catalog and shared documents through an installed source package. If unavailable, state the missing reference and use the core rules above or verified official package documentation; do not claim to have read a missing file. Runtime validation also requires the project package manager and a browser/WebGL-capable environment.

- Shared architecture: `../x-openai-web-game-foundations-594990b/SKILL.md`
- Frontend direction: `../x-openai-game-ui-frontend-1cdc78a/SKILL.md`
- 3D HUD layout patterns: `../../resources/plugins-6ebaff11/plugins/game-studio/references/three-hud-layout-patterns.md`
- React Three Fiber stack: `../../resources/plugins-6ebaff11/plugins/game-studio/references/react-three-fiber-stack.md`
- React starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/react-three-fiber-starter.md`
- GLB loader starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/gltf-loading-starter.md`
- Rapier starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/rapier-integration-starter.md`
- 3D asset pipeline: `../../resources/plugins-6ebaff11/plugins/game-studio/references/web-3d-asset-pipeline.md`
- WebGL debugging and perf: `../../resources/plugins-6ebaff11/plugins/game-studio/references/webgl-debugging-and-performance.md`
