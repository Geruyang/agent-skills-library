---
name: x-openai-report-to-google-slides-442261d
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Narrow conversion skill. Invoke only when the user explicitly asks to convert an existing HTML analytics report into a native Google Slides deck.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Report To Google Slides

Use this skill only when the user explicitly has an existing HTML analytics report and wants a Google Slides deliverable. The output should be a deck, not a pasted report. A stakeholder skimming the slides should understand the answer, evidence,
caveats, and recommended follow-up without opening the source report.

This skill consumes an HTML report. It does not convert a live MCP app report directly; if only an MCP app report exists, build a separate HTML delivery from the same canonical artifact evidence with `x-openai-build-report-768bc8e`'s portable builder first.

## Workflow

1. Resolve the local HTML report.

   Use an absolute file path. If the user provides a remote report, retrieve it outside this skill first. If the local file is a sign-in page, redirect page,
   or very small stub, stop and obtain the real report before continuing.

2. Run the helper.

   ```bash
   python3 <REPORT_TO_GOOGLE_SLIDES_SKILL_DIR>/scripts/report_to_google_slides.py \
     <LOCAL_HTML_REPORT_PATH> \
     --out-dir <PROJECT_OUTPUT_DIR>/report_to_google_slides
   ```

3. Inspect local outputs.

   Required outputs:

   - `deck.pptx`: editable local PowerPoint file
   - `manifest.json`: parsed source inventory and coverage counts
   - `deck_plan.json`: slide-by-slide plan with named elements
   - `preflight_checks.json`: local quality checks and pass/fail status
   - `assets/`: rendered chart images

   Do not import the PPTX until `preflight_checks.json` has `status: "passed"`.
   Then run `unzip -t <out-dir>/deck.pptx`.

4. Import and verify in Google Slides.

   Discover an authorized Google Drive/Slides integration that supports importing PPTX as a native Google Slides presentation, and use its actual tool/API schema. The original connector’s `_import_presentation` with `upload_mode="native_google_slides"` is only an example if that exact tool exists. Verify the resulting presentation outline and slide thumbnails using the integration’s available read APIs for every slide when possible. If no import capability or authentication is available, deliver the verified local PPTX and explain that native Slides creation and cloud verification are blocked; do not fabricate a Slides URL. At minimum, inspect the cover, one chart slide, one table slide,
   and the caveats/sources slides.

5. Repair before handoff.

   If thumbnails show clipped text, missing charts, low contrast, blank images,
   or awkward sizing, revise the helper output or source assumptions and regenerate before handing off the deck URL.

6. Hand off the deck.

   Return the Google Slides URL and, when useful, the local PPTX path or source HTML path. Keep routine check, preflight, thumbnail-inspection, and import-check details in support artifacts. Do not list internal checks in the user-facing handoff unless a check failed, was unavailable, or produced a user-relevant caveat.

## Standards

- Preserve the report's decision-critical information: headline claim,
  executive summary, major findings, metric definitions, material charts,
  decision-critical tables, recommendations, implications, caveats,
  assumptions, freshness notes, and source/provenance notes.
- Translate report prose into slide-native communication. Lead with the takeaway, use one main idea per slide, and put supporting detail in concise callouts, bullets, tables, chart annotations, or speaker notes.
- Tighten copy before shrinking fonts.
- Keep gross metric reads, net/incremental reads, causal claims, and caveats visibly separated when the source report distinguishes those lenses.
- Use editable text and native PPTX tables wherever practical. Use native PPTX bullets; do not fake bullets with typed dashes.
- Preserve source charts as evidence images. Do not screenshot the whole HTML report or paste whole report sections.
- Support self-contained portable-builder reports whose native charts and builder-generated semantic chart-data representations remain available to the conversion helper; the helper renders faithful local chart evidence images before building the deck.
- Use one chart per evidence slide unless the report has a stronger grouped comparison.
- Keep table slides legible. If a full table is too dense, keep the main comparison in the deck and move extra detail to speaker notes or source slides.
- Source notes should be visible but quiet.

## Visual System

The helper derives colors and hierarchy from the HTML report CSS and chart palette, then applies a restrained analytics deck layout. It does not follow external deck files or company-specific branding.
