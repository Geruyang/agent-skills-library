---
name: x-openai-report-to-google-doc-c4cc091
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Narrow conversion skill. Invoke only when the user explicitly asks to convert an existing local or blob-hosted HTML analytics report into a Google Doc, DOCX, or shareable document.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Report To Google Doc

Use this skill only when the user explicitly needs a shareable Google Drive document from an existing HTML analytics report. The source must be an HTML report: a local file, a downloaded blob-hosted report, or a report produced by `x-openai-build-report-768bc8e` HTML mode with the portable builder. This skill does not convert a live MCP app report directly.

The expected path is HTML -> DOCX -> Drive upload. It is acceptable for Drive to host the upload as a DOCX-backed viewer file rather than a native Google Docs MIME type. Do not use the old Google Docs batch-update request path.

## Workflow

1. Resolve the HTML report.

   Use an absolute local path. If the user provides a remote report, retrieve it first and pass the local HTML file to the helper. If the file is a sign-in page, redirect page, or tiny stub, stop and obtain the real report.

2. Run the bundled helper.

   ```bash
   python3 <REPORT_TO_GOOGLE_DOC_SKILL_DIR>/scripts/report_to_google_doc_plan.py \
     /absolute/path/to/report.html \
     --out-dir ./artifacts/report_to_google_doc_plan
   ```

   Omit `--render-workers` on the normal path. Only pass a worker count after benchmarking the same report family locally. If dependencies are missing,
   use a local virtual environment with `beautifulsoup4`, `pillow`, and `python-docx`; `cairosvg` or headless Playwright are optional renderers.

3. Inspect helper outputs.

   Required outputs:

   - `skeleton.txt`: source text with stable placeholders
   - `manifest.json`: parsed headings, tables, callouts, lists, styles, links,
     and rendered visual inventory
   - `preflight_checks.json`: source, width, DOCX, and rendered-image checks
   - `report.docx`: generated local Word document
   - `docx_upload_plan.json`: compact upload instructions
   - `placeholder_queries.json`: source mapping debug labels

   Do not upload until `preflight_checks.json` has `status: "passed"` with zero errors. Warnings must either be fixed or called out in the handoff.

4. Upload the DOCX.

   Discover a verified, authenticated Google Drive file-upload capability in the current host (MCP connector, supported CLI, or authorized Drive API). Inspect its actual schema and supply the generated `report.docx`, the requested filename, and MIME type `application/vnd.openxmlformats-officedocument.wordprocessingml.document`. The helper's upload plan is a capability description, not an executable tool invocation. Do not guess a host tool name or API parameter shape.

   If Drive access is unavailable, deliver the validated local DOCX and state the upload blocker; do not claim a Google Doc or cloud URL was created. Preserve the user's authorized destination and sharing scope.

   Treat the returned Drive URL as the deliverable. Do not attempt to force native Google Docs conversion, and do not fall back to `_batch_update_document`.

5. Validate the uploaded result.

   Confirm the uploaded file is readable and non-empty. Compare uploaded text against the source inventory: title, section headings, executive summary or answer callout, caveats, recommendations, source notes, and source links.
   Inspect the local `report.docx` structure when available: heading counts,
   lists, tables, hyperlink relationships, and image relationships should match `manifest.json`.

6. Hand off the link.

   Return the Drive/Docs URL and, when useful, the local DOCX path or source HTML path. Connector success alone is not enough; the handoff is complete only after the uploaded file and local DOCX structure have been checked against the source report. Keep routine check and preflight details in support artifacts. Do not list internal checks in the user-facing handoff unless a check failed, was unavailable, or produced a user-relevant caveat.

## Standards

- Preserve every section, headline claim, metric card, metric definition,
  source note, chart takeaway, recommendation, caveat, and link from the HTML report.
- Preserve semantic formatting: headings, paragraphs, inline bold/emphasis,
  inline code, positive/negative colors, links, lists, callouts, metric-card grids, tables, notes, captions, and charts.
- Use DOCX-native structures wherever practical: headings, paragraphs, tables,
  bullets/numbered lists, links, inline images, paragraph shading, table cell shading, and text styles.
- Keep the report text column readable. Tables, charts, rendered table grids,
  screenshots, and visual blocks must not exceed the DOCX page text width.
- Preserve charts as inline images rendered from the portable reader's source visual or builder-generated semantic chart-data representation, aligned to the same left edge as text and tables. A chart with missing bars, missing legend swatches, or all-black/all-white marks fails validation even if the DOCX contains an image object.
- Preserve multi-column report blocks. A two-column grid made only of titled mini-tables can remain a two-column rendered image capped to the text width;
  mixed two-column blocks with narrative text, pills, callouts, or non-table panels should preserve that content natively instead of dropping it.
- Do not expose customer-level details or sensitive links that were intentionally omitted from a sanitized report.
- Do not write Google Docs batch-update artifacts such as `seed_requests.json`,
  `remote_write_plan.json`, or `all_requests*.json`.

## Repairs

Use these fixes when validation exposes a conversion issue:

| Problem | Fix |
| --- | --- |
| Heading is regular weight | Fix the DOCX writer heading style or explicit run bolding. |
| Blank line after title or heading | Delete spacer paragraphs; skeletons should emit `\n`, not `\n\n`, after headings. |
| Body paragraphs have too much space | Delete literal blank paragraphs and set modest style spacing. |
| Table/image too wide | Set table columns or image width to the DOCX text column width. |
| Chart has labels but missing bars | Inline SVG class styles or use a headless screenshot before inserting. |
| Two-column table group is flattened | Treat the grid as one layout block with mini-table titles preserved. |
| Executive summary, metric cards, or section is missing | Fix parser inventory before upload. |
| Chart overlaps table | Insert the image on its own paragraph after the table. |
| Chart duplicated | Remove the extra image; keep exactly one source-order copy. |
| Inline bold/code/color missing | Fix manifest range splitting in the DOCX writer. |
| Source links show raw URLs | Replace with native linked labels or native bullets using HTML link text. |

## Local Checks

```bash
python3 -m py_compile <REPORT_TO_GOOGLE_DOC_SKILL_DIR>/scripts/report_to_google_doc_plan.py
python3 <REPORT_TO_GOOGLE_DOC_SKILL_DIR>/scripts/report_to_google_doc_plan.py \
  /absolute/path/to/report.html \
  --out-dir ./artifacts/report_to_google_doc_plan_smoke
jq '.status, .summary' ./artifacts/report_to_google_doc_plan_smoke/preflight_checks.json
test -f ./artifacts/report_to_google_doc_plan_smoke/report.docx
test -f ./artifacts/report_to_google_doc_plan_smoke/docx_upload_plan.json
git diff --check -- plugins/data-analytics/skills/build-report/report-to-google-doc
```
