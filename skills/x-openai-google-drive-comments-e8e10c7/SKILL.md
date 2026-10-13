---
name: x-openai-google-drive-comments-e8e10c7
description: Write, reply to, and resolve Google Drive comments on Docs, Sheets, Slides, and Drive files with evidence-backed location context. Use when the user asks to leave comments, review a file with comments, respond to comment threads, or resolve Drive comments.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Google Drive Comments

Use this skill for comment workflows in the unified Google Drive plugin. Drive comments can apply to Docs, Sheets, Slides, and generic Drive files, but API-created comments may appear unanchored in the Google editor UI. Every new top-level comment must therefore include enough surface-specific evidence for the reader to find the target without relying on native UI anchoring.

## Workflow

1. Ground the target file first.
- If the user did not provide an exact file URL or ID, search Drive, list recent files, list folders, or read metadata until the target file is unambiguous.
- Identify whether the file is a Google Doc, Sheet, Slides deck, or generic Drive file before drafting comments.

2. Read the surface that will be commented on.
- For Docs or text-like files, read the document text around each likely target.
- For Sheets, read spreadsheet metadata first, then read the specific sheet tabs and ranges that may receive comments.
- For Slides, read the presentation outline or text first, then read specific slides or thumbnails when visual context is needed.
- Do not guess a target quote, slide number, sheet name, or cell range from memory or search snippets.

3. Draft all intended comment updates before writing.
- Prefer one `bulk_update_file_comments` call for all creates, replies, and resolves in the same user request.
- Keep the batch to the action limit exposed by the tool. If the request needs more comments than the limit, ask before splitting into another batch.
- For replies and resolves, use existing comment IDs from the live comment thread data.

4. Attach surface-specific evidence to every new top-level comment.
- The comment body must explicitly name or quote the target evidence, because the Google editor UI may not show API-created anchors.
- Docs or text-like files: include `quoted_text` with the exact sentence, phrase, heading, or nearby text the comment refers to. Also quote that same text in the comment body when the critique would otherwise say "this sentence" or "this paragraph."
- Sheets: include `sheet_cell_range` with the sheet name and A1 cell or range, such as `Budget!C12` or `Pipeline!A2:D10`. Also name that sheet and range in the comment body, and include `quoted_text` when a displayed value, header, formula, or label would make the target clearer.
- Slides: include `slide_number`. Also name that slide number in the comment body, and include `quoted_text` when commenting on a title, bullet, label, chart text, or other visible slide text.
- Generic Drive files: if no structured surface exists, make the comment content explicitly name the file-level, page-level, timestamp-level, or section-level evidence it refers to.

5. Reject vague comments before sending them.
- Do not create comments that say only "this sentence," "this paragraph," "this slide," "this cell," or similar without the matching evidence field.
- If the model has a useful critique but cannot identify the exact evidence target, either turn it into an explicitly file-level summary comment or omit it and say the target was not specific enough.
- Do not rely on tool fields alone for location context. If the comment body would feel hand-wavy after removing the hidden tool fields, rewrite it before sending.

6. Verify the result.
- After writing, summarize how many comments were created, replied to, or resolved.
- Mention the evidence used for the highest-risk comments, especially any file-level comments that intentionally do not target a specific quote, slide, or cell.

## Limitations

- Do not rely on Drive comment `anchor` data for Google Docs, Sheets, or Slides unless the connector explicitly documents a provider-supported shape for that surface. Drive API-created comments may still display as unanchored in the Google editor UI.
- The evidence fields are the durable location contract for this workflow: exact quoted text for Docs and text-like files, sheet/cell range for Sheets, and slide number plus visible text for Slides.
