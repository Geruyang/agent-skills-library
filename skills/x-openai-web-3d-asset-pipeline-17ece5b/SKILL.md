---
name: x-openai-web-3d-asset-pipeline-17ece5b
description: Prepare and optimize browser-game 3D assets. Use when the user asks for GLB or glTF shipping work, including Blender cleanup and export, collision or LOD setup, compression, texture packaging, and runtime validation.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Web 3D Asset Pipeline

## Overview

Use this skill for shipped 3D assets, not runtime scene code. The default output format for browser 3D work in this plugin is GLB or glTF 2.0. The goal is predictable runtime assets, not whatever the DCC tool happened to export first.

This guidance is engine-agnostic and can serve Three.js, React Three Fiber, Babylon.js, or PlayCanvas.

## Use This Skill When

- the task is about GLB or glTF shipping format
- the task is about model cleanup, texture packaging, compression, LOD, or collision proxies
- the runtime stack is already chosen and the remaining problem is asset quality or size

## Do Not Use This Skill When

- the task is about scene, camera, renderer, or game-loop structure
- the task is purely about React versus vanilla Three.js routing
- the user is still deciding between runtime engines

## Default Pipeline

1. Author and clean the source asset in a DCC tool such as Blender.
2. Export to GLB or glTF 2.0.
3. Optimize with glTF Transform.
4. Validate naming, pivots, transforms, material reuse, and texture budgets.
5. Add collision proxies, LOD strategy, and baked-lighting assumptions as needed.
6. Ship the optimized asset and load it with engine-native GLTF support.

## Format Rules

- Default shipping format: GLB or glTF 2.0.
- Do not treat FBX, OBJ, or DCC-native formats as the long-term runtime contract.
- Apply or normalize transforms before shipping.
- Keep units, pivots, and orientation conventions consistent across the whole asset set.

## Optimization Rules

- Use glTF Transform for pruning, deduplication, simplification, and packaging.
- Use geometry compression intentionally.
  - Draco is a valid option when decode cost and compatibility fit the runtime.
  - Meshopt is often a strong default for web delivery.
- Compress textures deliberately.
  - Use KTX2 or BasisU when the runtime stack supports it.
  - Use WebP or AVIF where they make sense in the broader asset pipeline.
- Reuse materials and textures where possible to cut memory and draw-call cost.

## Runtime-Ready Asset Rules

- Keep model hierarchy names stable and meaningful.
- Set pivots and origins for gameplay interaction, not just for DCC convenience.
- Author explicit collision proxies for physics-heavy scenes.
- Decide whether lighting is dynamic, baked, or hybrid before final export.
- Plan LODs for large environments or repeated props.
- Keep texture resolution proportional to on-screen use, not source-art ambition.

## Common Failure Modes

- Shipping raw DCC exports without cleanup
- Too many unique materials
- Texture sizes far above visible need
- Missing collision proxies
- Scale or pivot mismatches between assets
- Runtime code compensating for asset mistakes that should be fixed upstream

## References

- Three.js stack: `../../resources/plugins-6ebaff11/plugins/game-studio/references/threejs-stack.md`
- React Three Fiber stack: `../../resources/plugins-6ebaff11/plugins/game-studio/references/react-three-fiber-stack.md`
- GLB loader starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/gltf-loading-starter.md`
- Rapier starter: `../../resources/plugins-6ebaff11/plugins/game-studio/references/rapier-integration-starter.md`
- 3D asset pipeline reference: `../../resources/plugins-6ebaff11/plugins/game-studio/references/web-3d-asset-pipeline.md`
- Alternative engines: `../../resources/plugins-6ebaff11/plugins/game-studio/references/alternative-3d-engines.md`
