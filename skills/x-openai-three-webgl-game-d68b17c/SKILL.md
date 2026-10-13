---
name: x-openai-three-webgl-game-d68b17c
description: Implement browser-game runtimes with plain Three.js. Use when the user wants imperative scene control in TypeScript or Vite with GLB assets, loaders, physics, and low-level WebGL debugging.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Three WebGL Game

## Overview

Use this skill for the default non-React 3D path in the plugin. This is not generic WebGL advice. It is an opinionated stack for browser 3D work:

- `three`
- TypeScript
- Vite
- GLB or glTF 2.0 assets
- Three.js loaders such as `GLTFLoader`, `DRACOLoader`, and `KTX2Loader`
- Rapier JS for physics
- SpectorJS for GPU and frame debugging
- DOM overlays for HUD, menus, and settings

Use this skill when the project wants direct scene, camera, renderer, and game-loop control. If the app already lives in React, route to `../x-openai-react-three-fiber-game-0b8ea0a/SKILL.md` instead.

## Use This Skill When

- the app is plain TypeScript or Vite rather than React-first
- the project wants direct imperative control over the render loop
- the user asks for Three.js specifically
- the runtime needs engine-like control over scene, camera, loaders, and physics

## Do Not Use This Skill When

- the 3D scene lives inside an existing React app
- the main problem is shipped-asset optimization rather than runtime code
- the user explicitly chose Babylon.js or PlayCanvas

## Core Rules

1. Keep simulation state outside Three.js objects.
   - Game rules, AI, quest state, timers, and progression should not live inside meshes or materials.
2. Treat the render graph as an adapter.
   - Scene graph, cameras, materials, loaders, and post-processing are view concerns layered over simulation state.
3. Keep camera behavior explicit.
   - Orbit, follow, chase, rail, and first-person styles each need their own control boundary.
4. Keep UI out of WebGL unless the presentation absolutely depends on it.
   - Menus, HUD, inventories, and settings should default to DOM.
5. Use GLB or glTF 2.0 as the default shipping model format.
   - Do not build the runtime around DCC-native formats.
6. Use Rapier instead of ad hoc collision code when the game has meaningful 3D physics or collision response.
7. Keep the first playable view low-chrome.
   - Default to one compact objective or status cluster plus transient prompts.
   - Long notes, lore, and controls references should be collapsed until asked for.
   - Do not frame the scene with multiple equal-weight cards during normal play.

## Initial Scaffold UX

For exploration, traversal, and character-control prototypes, start with a sparse shell:

- one edge-aligned objective chip
- one transient controls hint
- one optional compact status strip

Only add larger UI surfaces when the game loop truly requires them. Journal, quest log, codex, map, and settings surfaces should open on demand, not occupy the viewport by default.

## Recommended Structure

Use the module shape in `../../resources/plugins-6ebaff11/plugins/game-studio/references/three-webgl-architecture.md`, then keep these boundaries clean:

- `simulation/`: rules, progression, state, and AI
- `render/app/`: renderer, scene, camera, resize, context lifecycle
- `render/loaders/`: GLTF, Draco, KTX2, texture, and environment loading
- `render/objects/`: mesh instantiation and disposal
- `render/materials/`: material setup and shader boundaries
- `physics/`: Rapier world, bodies, colliders, and simulation bridge
- `ui/`: DOM overlays and menus
- `diagnostics/`: debug toggles, perf probes, and capture hooks

## Good Fit Scenarios

- Exploration demos
- Lightweight 3D combat prototypes
- Vehicle or traversal prototypes
- Scene-driven product or world showcases with gameplay
- Material, lighting, or post-process-led experiences
- 3D games where camera movement and depth readability are central

## Loaders, Assets, and Post-Processing

- Start with `GLTFLoader` for shipped 3D content.
- Add `DRACOLoader` or Meshopt-compatible optimization as part of the asset pipeline, not as a random runtime patch.
- Use `KTX2Loader` for compressed textures when the asset pipeline provides them.
- Prefer built-in Three.js render and post-processing utilities first. Add heavier abstraction only when the project actually needs it.
- Keep post-processing optional and measurable. Bloom and color effects should not hide gameplay readability.

## Shader and Material Guidance

- Start with standard Three.js materials and correct lighting before reaching for custom shaders.
- Use custom shaders only when the visual target genuinely needs them.
- Keep shader parameters driven by game state, not by incidental scene mutations.
- If a material stack gets complex, isolate it behind material factories instead of scattering shader setup across scene code.

## Browser Safety

- Handle resize explicitly.
- Expect WebGL context loss and recovery.
- Keep a fallback or degraded mode in mind for fragile GPU paths.
- Watch texture size, geometry count, draw-call growth, and post-processing cost.
- Use SpectorJS when the scene behaves incorrectly or frame cost is unclear.

## Scope Warning

Do not claim that this plugin offers equal 3D depth to the Phaser track. It supports serious 3D implementation, but the plugin is still 2D-first overall.

## References

- Shared architecture: `../x-openai-web-game-foundations-594990b/SKILL.md`
- Frontend direction: `../x-openai-game-ui-frontend-1cdc78a/SKILL.md`
- 3D HUD layout patterns: `../../resources/plugins-6ebaff11/plugins/game-studio/references/three-hud-layout-patterns.md`
- Three.js ecosystem: `../../resources/plugins-6ebaff11/plugins/game-studio/references/threejs-stack.md`
- Three.js structure: `../../resources/plugins-6ebaff11/plugins/game-studio/references/three-webgl-architecture.md`
- Vanilla starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/threejs-vanilla-starter.md`
- GLB loader starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/gltf-loading-starter.md`
- Rapier starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/rapier-integration-starter.md`
- 3D asset pipeline: `../../resources/plugins-6ebaff11/plugins/game-studio/references/web-3d-asset-pipeline.md`
- WebGL debugging and perf: `../../resources/plugins-6ebaff11/plugins/game-studio/references/webgl-debugging-and-performance.md`
