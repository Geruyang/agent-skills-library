---
name: x-openai-canva-translate-design-c1a13bf
description: Translate all text in a Canva design to another language, creating a translated copy. Faster than manually copying and editing each text box in Canva's editor. Use when users say "translate my design to [language]", "make a Spanish/French/etc version", or "localize my Canva design".
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Canva Translate

Translate all text elements in a Canva design to a target language, creating a new copy with translated content.

## Workflow

### 1. Locate the Design

If user provides a **design ID** directly (typically starts with `D`, e.g. `DABcd1234ef`), use that as the design identifier; **do not** pass it to `Canva:search-designs` (search is for titles, not IDs).

If user provides a **URL**: Extract the design ID from the URL (format: `https://www.canva.com/design/{design_id}/...`).

If user provides a **name**: Use `Canva:search-designs` to find the design by title. If multiple matches, ask user to clarify.

### 2. Create a Translated Copy

Use `Canva:resize-design` with the same dimensions to create a copy. This preserves the original design untouched.

### 3. Start Editing Transaction

Use `Canva:start-editing-transaction` on the new copy to get:
- `transaction_id` for making edits
- All text elements with their `element_id` and current text content

### 4. Translate Text

For each text element returned:
1. Translate the text to the target language (use Claude's translation capability)
2. Preserve formatting cues (line breaks, emphasis patterns)
3. Keep proper nouns, brand names, and technical terms as appropriate

### 5. Apply Translations

Use `Canva:perform-editing-operations` with `replace_text` operations for all translated elements. Batch all replacements in a single call.

Also update the design title to indicate the language (e.g., append " (Spanish)" or use translated title).

### 6. Commit Changes

After showing the user the translated preview thumbnail:
1. Ask for explicit approval to save
2. Use `Canva:commit-editing-transaction` to finalize
3. Provide the link to the new translated design

## Example Interaction

**User**: Translate my "Summer Sale Poster" to French

**Steps**:
1. Search: `Canva:search-designs` with query "Summer Sale Poster"
2. Copy: `Canva:resize-design` to create duplicate
3. Edit: `Canva:start-editing-transaction` on copy
4. Translate all text elements to French
5. Apply: `Canva:perform-editing-operations` with all `replace_text` operations
6. Show preview, get approval, commit

## Important Notes

- Always create a copy—never modify the original design
- Batch all text replacements in one `perform-editing-operations` call for efficiency
- If translation significantly changes text length, warn user that layout adjustments may be needed in Canva
- For designs with many pages, translate all pages in the same transaction
