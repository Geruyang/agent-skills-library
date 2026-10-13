---
name: x-openai-sprite-pipeline-e1572e4
description: Generate and normalize 2D sprite animations. Use when the user asks for full-strip generation from approved source frames, consistent anchor and scale normalization, or preview assets for browser-game animation.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## Reviewed capability mapping (TRAE / Claude)

This export does not include the shared game-studio scripts referenced as `../../scripts/` or the shared game-studio reference tree. Locate that installed package before running the recipes and pass absolute script paths from its verified root. If the scripts cannot be found, report normalization/preview execution as blocked; provide a plan or use a separately verified equivalent image-processing pipeline that preserves all quality gates. Discover an image generation/editing skill and authenticated provider separately; no host-bundled image tool is assumed.

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Sprite Pipeline

## Overview

Use this skill for 2D sprite generation and normalization. This workflow is intentionally anchored around one approved frame and a whole-strip generation pass because frame-by-frame generation drifts too easily.

This skill is 2D-specific. If the request is for 3D characters, meshes, or materials, route back through `../x-openai-game-studio-c9c2649/SKILL.md`.

## Core Workflow

1. Start from an approved in-game seed frame.
   - The seed frame should already reflect the right silhouette, palette, costume, and proportions.
2. Build a larger transparent reference canvas around that frame.
   - Use `../../resources/plugins-6ebaff11/plugins/game-studio/scripts/build_sprite_edit_canvas.py`.
3. Ask for the full animation strip in one edit request.
   - Do not generate each frame independently unless the user explicitly accepts lower consistency.
4. Normalize the result into fixed-size game frames.
   - Use `../../resources/plugins-6ebaff11/plugins/game-studio/scripts/normalize_sprite_strip.py`.
   - Use one shared scale across the whole strip.
   - Align frames with one shared anchor, typically bottom-center.
5. Optionally lock frame 01 back to the shipped seed frame.
   - Do this when the animation should begin from the exact idle or base pose already in game.
6. Render a preview sheet and inspect the animation in-engine before approving it.
   - Use `../../resources/plugins-6ebaff11/plugins/game-studio/scripts/render_sprite_preview_sheet.py`.

## Prompting Rules

Always preserve these invariants in the prompt:

- same character
- same facing direction
- same palette family
- same silhouette family
- same readable face or key features
- same outfit proportions
- transparent background
- exact frame count and slot layout

Always ask for:

- one strip at once
- a transparent canvas
- no scenery, labels, or poster composition
- crisp pixel-art clusters for pixel work
- production asset tone, not concept art

## Using Image Generation

For live asset generation or edits, use the installed `imagegen` skill in this workspace. This skill defines the game-specific process; `imagegen` handles the API-backed generation or edit execution.

## Script Recipes

Create a reference canvas:

```bash
python3 scripts/build_sprite_edit_canvas.py \
  --seed output/sprites/idle-01.png \
  --out output/sprites/hurt-edit-canvas.png \
  --frames 4 \
  --slot-size 256 \
  --canvas-size 1024
```

Normalize a raw strip:

```bash
python3 scripts/normalize_sprite_strip.py \
  --input output/sprites/hurt-raw.png \
  --out-dir output/sprites/hurt \
  --frames 4 \
  --frame-size 64 \
  --anchor output/sprites/idle-01.png \
  --lock-frame1
```

Render a preview sheet:

```bash
python3 scripts/render_sprite_preview_sheet.py \
  --frames-dir output/sprites/hurt \
  --out output/sprites/hurt-preview.png \
  --columns 4
```

## Quality Gates

- proportions stay stable across frames
- frame-to-frame size does not drift
- action reads clearly at game scale
- transparency is preserved
- frame 01 matches the shipped sprite when lockback is enabled
- preview looks correct before any in-engine asset index update

## References

- Detailed workflow: `../../resources/plugins-6ebaff11/plugins/game-studio/references/sprite-pipeline.md`
- Shared frontend context: `../x-openai-game-ui-frontend-1cdc78a/SKILL.md`
