---
name: x-openai-game-studio-c9c2649
description: Route early browser-game work. Use when the user needs stack selection and workflow planning across design, implementation, assets, and playtesting before moving to a specialist skill.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Game Studio

## Overview

Use this skill as the umbrella entrypoint for browser-game work. Default to a 2D Phaser path unless the user explicitly asks for 3D, Three.js, React Three Fiber, shader-heavy rendering, or another WebGL-first direction.

This plugin is intentionally asymmetric:

- 2D is the strongest execution path in v1.
- 3D has one opinionated default ecosystem: vanilla Three.js for plain TypeScript or Vite apps, React Three Fiber for React-hosted 3D apps, and GLB or glTF 2.0 as the default shipping asset format.
- Shared architecture, UI, and playtest practices apply to both.

## Use This Skill When

- the user is still choosing a stack
- the request spans multiple domains such as runtime, UI, asset pipeline, and QA
- the user says "help me build a game" without naming the implementation path

## Do Not Stay Here When

- the runtime is clearly plain Three.js
- the runtime is clearly React Three Fiber
- the task is clearly a shipped-asset problem
- the task is clearly frontend-only or QA-only

Once the intent is clear, route to the most specific specialist skill and continue from there.

## Routing Rules

1. Classify the request before designing or coding:
   - `2D default`: Phaser, sprites, tilemaps, top-down, side-view, grid tactics, action platformers.
   - `3D + plain TS/Vite`: imperative scene control, engine-like loops, non-React apps, direct Three.js work.
   - `3D + React`: React-hosted product surfaces, declarative scene composition, shared React state, UI-heavy 3D apps.
   - `3D asset pipeline`: GLB, glTF, texture packaging, compression, LOD, runtime asset size.
   - `Alternative engine`: Babylon.js or PlayCanvas requests, usually as comparison or ecosystem fit questions.
   - `Shared`: core loop design, frontend direction, save/debug/perf boundaries, browser QA.
2. Route to the specialist skills immediately after classification:
   - Shared architecture and engine choice: `../x-openai-web-game-foundations-594990b/SKILL.md`
   - Deep 2D implementation: `../x-openai-phaser-2d-game-f3df62d/SKILL.md`
   - Vanilla Three.js implementation: `../x-openai-three-webgl-game-d68b17c/SKILL.md`
   - React-hosted 3D implementation: `../x-openai-react-three-fiber-game-0b8ea0a/SKILL.md`
   - 3D asset shipping and optimization: `../x-openai-web-3d-asset-pipeline-17ece5b/SKILL.md`
   - HUD and menu direction: `../x-openai-game-ui-frontend-1cdc78a/SKILL.md`
   - 2D sprite generation and normalization: `../x-openai-sprite-pipeline-e1572e4/SKILL.md`
   - Browser QA and visual review: `../x-openai-game-playtest-848d89d/SKILL.md`
3. Keep one coherent plan across the routed skills. Do not let engine, UI, asset, and QA decisions drift apart.

## Default Workflow

1. Lock the game fantasy and player verbs.
2. Define the core loop, failure states, progression, and target play session length.
3. Choose the implementation track:
   - Default to Phaser for 2D browser games.
   - Choose vanilla Three.js when the project is explicitly 3D and wants direct render-loop control in a plain TypeScript or Vite app.
   - Choose React Three Fiber when the project already lives in React or wants declarative scene composition with shared React state.
   - Choose raw WebGL only when the user explicitly wants a custom renderer or shader-first surface.
4. Define the UI surface early. Browser games usually need a DOM HUD and menu layer even when the playfield is canvas or WebGL.
   - For 3D starter scaffolds, default to a low-chrome HUD that preserves the playfield and keeps secondary panels collapsed.
5. Decide the asset workflow:
   - 2D characters and effects: use `sprite-pipeline`.
   - 3D models, textures, and shipping format: use `web-3d-asset-pipeline`.
6. Close with a playtest loop before calling the work production-ready.

## Output Expectations

- For planning requests, return a game-specific plan with stack choice, gameplay loop, UI surface, asset workflow, and test approach.
- For implementation requests, keep the chosen stack obvious in the file structure and code boundaries.
- For mixed requests, preserve the plugin default: 2D Phaser first unless the user asks for something else.
- When the user asks about Babylon.js or PlayCanvas, compare them honestly but keep Three.js and R3F as the primary code-generation defaults unless the user explicitly chooses another engine.

## References

- Engine selection: `../../resources/plugins-6ebaff11/plugins/game-studio/references/engine-selection.md`
- Three.js stack: `../../resources/plugins-6ebaff11/plugins/game-studio/references/threejs-stack.md`
- React Three Fiber stack: `../../resources/plugins-6ebaff11/plugins/game-studio/references/react-three-fiber-stack.md`
- 3D asset pipeline: `../../resources/plugins-6ebaff11/plugins/game-studio/references/web-3d-asset-pipeline.md`
- Vanilla Three.js starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/threejs-vanilla-starter.md`
- React Three Fiber starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/react-three-fiber-starter.md`
- Frontend prompting patterns: `../../resources/plugins-6ebaff11/plugins/game-studio/references/frontend-prompts.md`
- Playtest checklist: `../../resources/plugins-6ebaff11/plugins/game-studio/references/playtest-checklist.md`

## Examples

- "Help me prototype a browser tactics game."
- "I need a Phaser-based action game loop with a HUD and menus."
- "I want a Three.js exploration demo with WebGL lighting and browser-safe UI."
- "I want a React-based 3D configurator with React Three Fiber."
- "Optimize my GLB assets for the web and keep the file sizes under control."
- "Set up the asset workflow for consistent 2D sprite animations."
