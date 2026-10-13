---
name: x-openai-google-drive-7855235
description: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work. Use when the user wants to find, fetch, organize, share, export, copy, or delete Drive files, or summarize and edit Google Docs, Google Sheets, and Google Slides through one unified Google Drive plugin.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Google Drive

Use this as the top-level router for Google file work inside the unified Google Drive plugin. Do not route the user toward separate Google Docs, Google Sheets, or Google Slides plugins.

Start with Google Drive for file discovery and file lifecycle tasks, then route to narrower sibling skills only when the task becomes specific to Docs, Sheets, or Slides.

## Workflow

1. Ground the target file first.
- If the user did not provide an exact file URL or ID, use Google Drive search, recent files, folder listing, or metadata reads to identify the right file.
- If the request starts as "find X and then update it," do the Drive discovery step first instead of guessing the target.

2. Stay in the base Google Drive workflow for Drive-native tasks.
- Use the base workflow for search, fetch, recent files, folders, sharing, copying, deleting, exporting, revision history, file moves, and other file-lifecycle work that is not primarily about editing Docs, Sheets, or Slides content.
- For version-history requests, including "previous version," "revision history," "what changed since the last version," or "compare to the prior revision," ground the file, fetch the current content, use `list_file_revisions`, fetch the immediately previous revision or the user-named revision with `fetch_file_revision`, then compare the fetched revision against the current content. Do not say previous versions are unsupported until you have checked whether revision tools are available for the target file.
- For file move requests, ground the source file and target folder, read the file metadata including its current parents, then use `update_file` with `addParents` for the target folder and `removeParents` for only the verified source parent or parents that should no longer contain it. Preserve unrelated parents, and verify the move by reading metadata or listing the target folder before the final response.
- Before any export or raw-file fetch, read or reuse Drive metadata so the MIME type and Google Drive URL are known. Use `export_file` only to convert a native Google Doc, Sheet, or Slide into an explicitly requested format; it returns an authenticated file reference, not inline bytes or base64. Google limits `files.export` responses to **10 MB**; oversized exports fail rather than returning truncated content. For a larger native PDF, use `download_file(id=file_id, mime_type="application/pdf")` when the streaming action is available. It calls Google's `files.download` API and returns a top-level materializable `file_uri`. Once `download_file` is unavailable and canonical `fetch` uses that streamed download path, use `fetch(url=google_drive_url, download_raw_file=True, raw_export_mime_type="application/pdf")` instead. A native-file `fetch` that still uses `files.export` cannot bypass the 10 MB limit. For PDFs, images, ZIPs, Office files, recordings, and other stored, non-native files, use `fetch(url=google_drive_url, download_raw_file=True)`. Use only the authenticated top-level `file_uri` or materialized `workspace_path`; never request inline base64 unless an existing caller explicitly opts into bounded legacy compatibility. Use `fetch` without `download_raw_file` for bounded, best-effort readable text. Do not retry `export_file` after metadata shows a non-native MIME type.

3. Route to the narrowest sibling skill that matches the file type and job.
- Drive, Docs, Sheets, or Slides comment creation, comment replies, comment resolution, or review-by-comments: use [google-drive-comments](../x-openai-google-drive-comments-e8e10c7/SKILL.md).
- Google Docs net-new creation, content summary, revision planning, prose rewriting, or section edits: use [google-docs](../x-openai-google-docs-70e759c/SKILL.md).
- Google Sheets creation, local spreadsheet import, range inspection, table cleanup, data restructuring, formula design or repair, chart creation or repair, or batch updates: use [google-sheets](../x-openai-google-sheets-9c9c18b/SKILL.md).
- Google Slides deck summary, content edits, new deck creation, local presentation import, visual cleanup, structural repair, or template migration: use [google-slides](../x-openai-google-slides-f9361a1/SKILL.md).

## Routing Rules

- If the request is ambiguous between Drive and a file-type surface, use the artifact itself as the tie-breaker:
  - Doc -> Docs skill
  - Sheet -> Sheets skill
  - Deck -> Slides skill
- If the user wants to find a file and then edit it, do both in one flow: Drive for discovery, then the file-type skill for the edit.
- If the user wants a Google Workspace outcome but has not named a file type yet, start with Drive discovery instead of asking them to choose among separate Google plugins.
- If the user asks to create a new Google Doc, route to the Docs skill; it owns the mandatory local `.docx` -> native Google Docs import workflow and the explicit-user-override boundary. Do not create a blank Google Doc directly from this router.
- If the user asks to import a local `.docx` into Google Docs, route to the Docs skill and use its native conversion workflow. Preserve the source file type only when the user explicitly asks for that.
- If the user asks to create a new Google Sheet, route to the Sheets skill. The Sheets skill should prefer the `[@spreadsheets](plugin://spreadsheets@openai-primary-runtime)` plugin or `$Excel` skill to create a local `.xlsx`, then import it as native Google Sheets.
- If the user asks to import a local `.xlsx`, `.xls`, `.ods`, `.csv`, or `.tsv` into Google Sheets, route to the Sheets skill and use native Google Sheets conversion by default. Preserve the source file type only when the user explicitly asks for that.
- If the user asks to create a new Google Slides deck, route to the Slides skill; it owns the mandatory local `.pptx` -> native Google Slides import workflow and the explicit-user-override boundary. Do not create a blank Google Slides deck directly from this router.
- If the user asks to import a local `.ppt`, `.pptx`, or `.odp` into Google Slides, route to the Slides skill and use its native conversion workflow. Preserve the source file type only when the user explicitly asks for that.
- If the user asks to export or download an existing Drive file, choose the action from metadata: native Google Docs, Sheets, and Slides files use `export_file` for explicit conversions within Google's **10 MB** limit. For a larger native PDF, prefer the currently available streaming `download_file(id=file_id, mime_type="application/pdf")`; after canonical `fetch` adopts the same streamed download path and `download_file` is removed, use `fetch(url=google_drive_url, download_raw_file=True, raw_export_mime_type="application/pdf")`. Stored, non-native PDFs, images, ZIPs, CSVs, Office files, audio, and video use `fetch(url=google_drive_url, download_raw_file=True)`. Use the returned top-level `file_uri` or its authenticated, materialized `workspace_path`; do not expose inline binary, base64, or a bearer URL. Base64 is available only when an existing compatibility caller explicitly requests the bounded legacy behavior.

## Write Safety

- Preserve the user's existing file organization, sharing state, and target artifact unless the request clearly asks to change them.
- When a task can be satisfied by a file-level Drive operation alone, do not load heavier Docs, Sheets, or Slides skills.
- For write-heavy Sheets or Slides work, read the specialized skill before the first large update so request shapes stay grounded.
- For any file import or explicit direct create that returns a user-facing Google Workspace link, wait for the write action to complete and verify the created file with connector readback or Drive metadata readback before returning the URL. Use only a URL or id observed from the completed connector result or readback; never synthesize or predict the URL.

## Related Skills

- Comments: [google-drive-comments](../x-openai-google-drive-comments-e8e10c7/SKILL.md)
- Docs: [google-docs](../x-openai-google-docs-70e759c/SKILL.md)
- Sheets: [google-sheets](../x-openai-google-sheets-9c9c18b/SKILL.md)
- Slides: [google-slides](../x-openai-google-slides-f9361a1/SKILL.md)
