---
name: x-openai-canva-edit-design-cabcf81
description: Make edits to an existing Canva design — change or fix text, replace/insert/delete images and videos, reformat text (size, weight, style, color, alignment, lists, line height), reposition or resize elements, and update the title. Use when the user wants to change, edit, update, fix, translate, replace, or reformat content in a specific Canva design. This is the safe edit engine that other Canva skills (e.g. implement-feedback) build on.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Canva Design Editing

## Discover the editing capability

Inspect the current host's connected Canva tools and their schemas before editing. The `Canva:*` names below describe the original connector's operations, not guaranteed host tool identifiers. Use an available Canva MCP or authenticated API only after verifying that it supports the same draft transaction, preview, commit, and cancel semantics. Keep the approval and scope gates below on any equivalent route. If those capabilities are unavailable, deliver a local edit specification with the design link, target elements, replacement content, and manual steps; explicitly state that the Canva design has not been changed. Do not invent transaction IDs or treat a local specification as a saved design.

The canonical, safe way to apply edits to an existing Canva design. Every Canva skill that mutates a design should follow this exact protocol: **start a transaction → perform operations → commit (with approval)**. Changes are draft-only until committed and are PERMANENTLY LOST if not committed.

## The Transaction Protocol (always these steps, in order)

1. **`Canva:start-editing-transaction`** — pass the `design_id`. Remember the returned `transaction_id` and the `pages` array; both are required by later calls. ALWAYS show the user the thumbnail(s) returned here.
2. **`Canva:perform-editing-operations`** — apply edits. Pass the `transaction_id`, the `pages` array from the previous response, the `page_index` of the first page being changed, and an `operations` array. Batch multiple operations into a single call wherever possible.
3. **`Canva:commit-editing-transaction`** — save. See the approval gate below. After committing, the `transaction_id` is invalid; a new edit needs a new transaction.
4. **`Canva:cancel-editing-transaction`** — discard the draft instead of saving (e.g. the user rejects the preview, or you opened a transaction only to inspect the design).

## Capabilities — what the API CAN and CANNOT do

### CAN (operations on `perform-editing-operations`)
- **Text content**: `replace_text` (whole element), `find_and_replace_text` (substring)
- **Text formatting** (`format_text`): font size, weight (normal/bold), style (normal/italic), color, alignment, line height, underline, strikethrough, links, list level/marker
- **Media**: `update_fill` (replace image/video), `insert_fill` (add image/video), `delete_element`
- **Layout**: `position_element`, `resize_element`
- **Metadata**: `update_title`
- **Autofill mapping**: `update_autofill_field` (fixed-page designs only)

### CANNOT
- Change font **family/typeface** (only size, weight, style)
- Add **new text elements** (you can only insert media, not new text boxes)
- Change background colors or gradients
- Add, remove, or reorder pages/slides
- Modify animations, transitions, or element opacity (except on newly inserted fills)
- Group/ungroup elements, or restyle shapes (only text inside shapes is editable)

When a requested change is in the CANNOT list, tell the user it must be done manually in the Canva editor — don't attempt a workaround.

## Responsive pages — restricted operation set

Some pages come back marked `is_responsive: true`. On those pages, ONLY these operations are allowed:
`update_title`, `replace_text`, `update_fill`, `delete_element`, `find_and_replace_text`.

Before calling `perform-editing-operations`, check the `pages` array. If any operation targets a responsive page with an unsupported op (e.g. `format_text`, `position_element`, `resize_element`, `insert_fill`), do NOT make the call — tell the user that operation isn't supported on that page and offer an alternative.

## The commit approval gate (required)

`commit-editing-transaction` makes changes permanent. You MUST show the user exactly what changed (and the preview thumbnail) and get explicit approval before committing — e.g. "Here's the preview. Save these changes to your design?" Wait for a clear yes.

- Do NOT commit without approval.
- Do NOT tell the user changes are saved before the commit call has succeeded.
- After a successful commit, give the user a direct link to open the design in Canva.
- If a commit fails, all changes are lost — start a new transaction to retry.

> Note for composing skills: a skill that already collects a single up-front approval for a batch of changes (e.g. `canva-implement-feedback`) should treat that approval as covering the commit and NOT ask again. Follow that skill's own confirmation rules; the gate above is the default for direct, ad-hoc edits.

## Workflow

### Step 1: Resolve the design
- Short link (`canva.link/...`) → `Canva:resolve-shortlink` to get the URL.
- Full Canva URL → extract the design ID (the segment after `/design/`).
- Raw design ID (starts with `D`) → use directly; do NOT search.
- Nothing provided → ask for the design ID or link.

### Step 2: Start the transaction and inspect
Call `Canva:start-editing-transaction`. Show the thumbnail(s). Use the returned content to locate the exact `element_id`s you need to target. (If you only needed to look, call `cancel-editing-transaction` and stop.)

### Step 3: Build and perform operations
Translate the user's request into concrete operations. Confirm scope first when a `find_and_replace_text` string could match in multiple places or contexts — ask which instances they mean. Batch all operations into one `perform-editing-operations` call when you can.

### Step 4: Preview and commit
Show the resulting thumbnail and a plain-language list of what changed. Ask for approval, then `commit-editing-transaction`. Share the edit link.

## Rules
- Always remember and reuse the `transaction_id` and `pages` array within a transaction.
- Never leave a transaction uncommitted without telling the user their draft was discarded.
- For destructive ops (`delete_element`, large `find_and_replace_text`), confirm scope before performing.
- Prefer one batched `perform-editing-operations` call over many small ones.
