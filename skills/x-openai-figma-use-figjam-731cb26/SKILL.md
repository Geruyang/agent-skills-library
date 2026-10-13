---
name: x-openai-figma-use-figjam-731cb26
description: This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# use_figma — Figma Plugin API Skill for FigJam

This skill contains FigJam-specific context for the `use_figma` MCP tool. The [figma-use](../x-openai-figma-use-678d26c/SKILL.md) skill provides foundational context for plugin API execution via MCP as well as the full Figma plugin API for more advanced use-cases that are not described here.

**Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage — it does not affect execution.

> **FigJam URL is `figma.com/board/...`.** Do NOT call `figma.createPage()` in FigJam — it throws `TypeError: figma.createPage no such property 'createPage' on the figma global object`. `createPage()` is a Design-file API only (`figma.com/design/...`). FigJam files have a single implicit page; organize content with sections instead (see [create-section](references/create-section.md)).

## Inspecting FigJam Files

**`get_figjam` is the inspection tool for FigJam files.** It returns the full node tree as XML, including IDs of pages, sections, stickies, connectors, and other nodes you need to reference in subsequent `use_figma` calls.

- **Use `get_figjam` upfront** before writing any `use_figma` code that needs to reference existing nodes (page IDs, section IDs, etc.). Don't try to discover IDs by running an inspection script — `console.log` output from `use_figma` is **not returned to the agent** (see [figma-use Critical Rule #4](../x-openai-figma-use-678d26c/SKILL.md)). Only the `return` value comes back.
- **`get_metadata` does NOT work on FigJam files** — it is design-mode only and will fail immediately with "unsupported for FigJam files".
- **`get_screenshot` requires a valid `nodeId`** — passing an empty nodeId returns "invalid nodeId" error. Get IDs from `get_figjam` first.
- If you forgot to `return` an ID from a previous `use_figma` call and need it now, call `get_figjam` rather than re-running an inspection script.

## Loading Reference Docs Efficiently

Load only the references your task needs — but when you do need to load multiple, **issue all reads in a single parallel tool-call batch**, not sequentially across turns. For a typical board-creation task, that means a single message containing reads for `plan-board-content` plus the 3-4 specific node-type references you'll use.

## Deferred Tools — Batch-Load Schemas

Discover the connected Figma MCP tools (`use_figma`, `get_figjam`, `get_screenshot`, `get_metadata`, `create_new_file`, `whoami`) through the current host tool catalog or MCP discovery mechanism. Batch schema discovery when the host supports it; do not assume a tool-search function or query syntax exists. Read each exposed schema before invocation. If no supported FigJam inspection or Plugin API execution adapter is available, report the missing capability instead of substituting a generic REST call. Runtime rules below describe the referenced adapter and must be checked against any equivalent adapter.

## Text Mutations — Canonical Recipe

Every FigJam text mutation (sticky/shape/label/table cell/connector text, standalone text nodes) follows the same recipe as Design files: load font → `await` → mutate → return affected IDs. Skipping the load throws `Cannot write to node with unloaded font "<family> <style>"`. See [figma-use → gotchas.md → Canonical text-edit recipe](../x-openai-figma-use-678d26c/references/gotchas.md#canonical-text-edit-recipe-font-load--await--mutate--return-ids). FigJam-specific note: sublayer defaults vary (sticky → `Inter Medium`, shape → `Inter Medium`, connector → invalid until set), so always load from `node.text.fontName` rather than hardcoding `{ family: 'Inter', style: 'Regular' }`.

## Adding Images to a FigJam Board

**`upload_assets` is the ONLY supported way to add images to a FigJam file.** Do NOT use `figma.createImage()` or `figma.createImageAsync()` from inside `use_figma` — they are unsupported as image-upload entry points in FigJam. Call `upload_assets` with the FigJam `fileKey`; the tool returns single-use upload URLs that you POST raw image bytes to, and the image is committed and placed automatically. Pass `nodeId` (with `count: 1`) to attach the upload to an existing FigJam node as a fill; omit `nodeId` to drop the image onto the board as a new layer.

For the full request/response shape, see [figma-use → api-reference.md → Images](../x-openai-figma-use-678d26c/references/api-reference.md#images).

## Reference Docs

- [plan-board-content](references/plan-board-content.md) - Read this for any board content request — board template, retro, brainstorm, ice breaker, meeting board, scaffold
  - Covers planning of generated board content, including sequential outline, sections, intents, and hierarchical text
  - Delegates to other references for specific API details
- [create-section](references/create-section.md) — Create and configure FigJam sections (sizing, naming, colors, content visibility, organizing nodes, column layouts)
- [create-sticky](references/create-sticky.md) — Create and configure FigJam sticky notes (colors, sizing, text, author visibility, batch creation)
- [create-connector](references/create-connector.md) — Create and configure FigJam connectors (endpoints, arrows, line types, labels, colors, diagram wiring)
- [create-text](references/create-text.md) — Create and configure FigJam text nodes (font loading, preset fonts and colors, sizing, lists, mind map operations)
- [position-figjam-nodes](references/position-figjam-nodes.md) — Position, size, and reparent nodes on the canvas (including within sections)
- [create-shape-with-text](references/create-shape-with-text.md) — Create and configure FigJam shapes with embedded text (shape types, color presets, sizing to fit text, diagram layouts)
- [create-code-block](references/create-code-block.md) — Create and configure FigJam code block nodes (languages, syntax highlighting, positioning, embedding in sections)
- [create-table](references/create-table.md) — Create and configure FigJam tables (rows, columns, cell text, color presets, resizing)
- [edit-text](references/edit-text.md) — Edit existing text nodes (font loading, styled ranges, find/replace, FigJam Charcoal default color)
- [create-label](references/create-label.md) — Create and configure FigJam label nodes (small numbered/lettered circle callout markers, sequences, positioning)
- [batch-modify](references/batch-modify.md) — Patterns for modifying many existing nodes at once (bulk style changes, repositioning, property updates)
- [figjam-colors](references/figjam-colors.md) — Canonical FigJam color palettes for every node type (sticky, section, connector, shape, label) plus the `hex/255` notation rule and the `h()` helper
