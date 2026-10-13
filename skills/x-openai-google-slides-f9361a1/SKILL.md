---
name: x-openai-google-slides-f9361a1
description: Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or prior-period source, or asks to edit, update, repair, restyle, or clean up an existing native Google Slides deck. Use the Presentations skill instead for net-new presentation creation when no existing native Google Slides deck must be followed.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Google Slides

### Presentations clarification questions

- Ask for new presentations or major rewrites. Skip this for edits/conversions.
- Inspect prompt, conversation history, existing file and relevant references to figure out what questions to ask.
- Questions should cover topic, audience, and purpose and come before planning
- When asking questions, focus on consequential dimensions not stated or clearly implied.
- When the artifact is a new analysis, focus on which definition, metric, or lens should drive conclusions.
- Unresolved reference labels or question marks are user-owned: ask, don't infer.
- Once topic, audience, and purpose are clear, proceed without asking. Choose emphasis, format, length, style, details. Use placeholders for missing facts.

Use `request_user_input` once if available, else ask via a message. Have the best suggestion first. Append `(Recommended)` to its label. Have another good alternative second. Have `Use your judgment` as the third and final option. If the request times out or returns no answer, proceed using your best judgment; do not ask again.

## Route the Request

- Use the installed Presentations skill to create a net-new presentation when no existing native Google Slides deck is the template or reference.
- Use this skill to create a presentation by following an existing native Google Slides template, reference deck, or prior-period deck.
- Use this skill to edit, update, repair, restyle, or clean up an existing native Google Slides deck.
- If a request combines new content with an existing native Google Slides deck that must be followed, use this skill.
- Do not use this skill to author a blank or from-scratch presentation.

## Parse a Template Deck

Discover an authenticated Google Slides/Drive connector or official API client and verify its read, copy, update, and export schemas. If none is available, use an exported deck supplied by the user for local analysis and report that native document changes are blocked.

Read the complete template presentation resource (omit field filtering) and save the unmodified JSON as `raw-template.json` in the task workspace. Set `SKILL_DIR` to this skill's absolute directory and `WORKSPACE` to the current task workspace. Use the host's file writer or a verified local client, avoiding large raw JSON in conversation. The `host/` adapters are optional original-host integrations; use them only when their actual `tools` interface is available, never as invented portable APIs.

Set `NODE` to a verified local Node.js executable and run:

```bash
"$NODE" "$SKILL_DIR/scripts/parse_template_design_system.mjs" \
  --input "$WORKSPACE/raw-template.json" \
  --output "$WORKSPACE/design-system.json" \
  --catalog "$WORKSPACE/design-catalog.md"
```

`--catalog` is optional. Use the JSON for master families, layout and placeholder IDs, inherited styles, theme colors, protected regions, and exemplar geometry. Use the catalog as a compact planning view. Confirm semantic and visual interpretations against rendered source slides; the parser derives structure but does not render the deck.

## Render a Deck

Export the deck once as PDF through the authorized Drive connector or official API and save it locally. Use a verified PDF renderer such as `pdftoppm` from the current toolchain to render every page. The optional `host/export-and-render-slides.mjs` adapter requires its original host interfaces; inspect those interfaces before using it. Otherwise preserve its guarantees with the available connector and local tools: fresh output directory, saved `presentation.pdf`, ordered PNGs mapped to native slide IDs, and matching PDF page/design-system counts. Inspect each rendered image through the current host's image viewer; create a contact sheet when useful. If export or rendering is unavailable, report the incomplete visual validation.

### Presentations location

Use the user-specified Drive folder or an existing appropriate project folder. If no location is specified, resolve the destination through the current connector; do not assume a host-branded folder exists.
Edit existing presentations in place.

Respect user-specified locations.

## Build From the Template

For template or reference following, copy the template once and edit only the copy.

Before making mutations, use the design catalog and rendered template slides to choose and record for every planned output slide:

- its narrative role;
- the native template exemplar slide ID or layout ID;
- whether it will be built by duplicating the exemplar or creating from the layout.

Match exemplars by narrative role, content density, evidence type, orientation, hierarchy, and meaning-bearing slots—not merely by object count or visual similarity. If the user links a particular template slide, inspect it explicitly and use it when it fits the requested role.

Do not use an exemplar containing device mockups, photography, screenshots, charts, or other meaning-bearing slide-local media unless every such element is explicitly mapped to destination content as keep, replace, or delete. If every element cannot be mapped, choose another exemplar.

Treat template placeholder media as meaning-bearing slide-local media. Explicitly map every image and video slot in a selected exemplar—especially speaker portraits—to keep, replace, or delete; never leave an unmapped placeholder in the output.

Prefer these construction methods in order:

1. Duplicate a rendered template exemplar when its design depends on slide-local shapes, image or chart frames, tables, groups, video, custom text styles, footer treatment, or other native objects.
2. Create from an inspected template layout only when its inherited placeholders are sufficient.
3. Populate, replace, or remove existing exemplar objects and inherited placeholders before creating new primary text, image, table, chart, or shape objects.
4. Create a new composition only when no inspected exemplar or layout can support the content; keep it consistent with the nearest template family.

Treat slide-local structure as part of the template. When a duplicated exemplar already contains a table, title frame, card structure, divider, footer, image frame, or other reusable structural object, edit it in place. Do not delete and recreate it merely to simplify implementation. Remove an object only after explicitly mapping it to `delete` because the destination slide does not need it.

Preserve the intrinsic aspect ratio of every image and video. Never stretch media by independently setting its width and height or by applying unequal horizontal and vertical scaling without deriving both from its intrinsic dimensions. Do not blindly reuse an exemplar media transform when the replacement has a different aspect ratio.

Use crop-to-fill only for decorative photography or full-bleed imagery where edge cropping is safe. Fit screenshots, charts, diagrams, UI, and videos fully within the intended frame so all meaning-bearing content remains visible; center the result, and prefer empty margins to distortion or loss of important content. Treat stretched media or improperly cropped meaning-bearing content as a concrete visual defect.

Preserve each exemplar's font family, weighted font family, font size, bold and italic state, color, paragraph styling, geometry, and object type by default. Change one of these only to resolve a concrete content-fit defect.

Preserve the template's font sizes whenever possible. If text overflows, first consider a small, local font-size reduction; do not shrink an entire mixed-style text box to solve one overflowing passage. Never reduce narrative body or list text below 12 pt. If the template already defines smaller narrative text for the same role, preserve that template size but do not reduce it further. Template-native captions, footers, source notes, and micro-labels may remain smaller, but do not reuse those smaller styles for narrative content.

If content still does not fit readably, choose a denser suitable exemplar or shorten flexible wording while preserving the original meaning, tone, facts, and required details. Treat reaching the 12 pt narrative floor, visible overcrowding, conspicuously undersized text, or leaving a major intended region unused as evidence that the archetype is wrong—not as a cue for further local typography repairs. Restore the template size and switch to a more appropriate exemplar or shorten the copy; do not apply a uniform minimum-size style to an entire text box or keep adjusting paragraphs to force an unsuitable exemplar. If adapting an image-led exemplar requires deleting its principal media slot and leaving that region empty, choose a text-first exemplar instead.

Treat multiple text and paragraph styles within one text box as structural. If a text box combines a title, kicker, label, body, or other differently styled runs, replace the corresponding text while preserving the existing run and paragraph styles. Do not apply one uniform style to the entire text box.

Before replacing text in a mixed-style text box, record its existing text and paragraph runs and update the corresponding ranges. Do not use `deleteText` over `ALL` followed by `insertText` and `updateTextStyle` over `ALL`; if replacement changes run lengths, reconstruct the original styled ranges explicitly.

Use native paragraph bullets for lists. Never type leading hyphens or visible bullet glyphs such as `•`, `◦`, `▪`, or `‣` into inserted text to imitate a bulleted list. When an exemplar uses a custom bullet character or style, preserve its existing list formatting and edit the paragraph text without replacing or normalizing the marker.

Every bulleted paragraph must contain visible text. Never leave an empty or whitespace-only bulleted paragraph. When an exemplar contains more list items than needed, delete the unused paragraph or remove its bullet formatting; use paragraph spacing instead of a blank bullet to create vertical separation.

Do not create from a blank layout when an inspected rich exemplar can support the narrative role and evidence type.

Use one consistent exemplar or layout family for truly recurring slide roles. This does not mean collapsing visually distinct section-title, speaker, agenda, or content archetypes into one generic construction. If content does not fit, shorten flexible wording or choose a better-fitting template archetype; do not flatten the template's typography or redesign a sparse composition into a dense canvas.

Preserve native links, notes, tables, charts, and media types when supported, and remove stale exemplar content. Keep unused template-library slides until the delivered slides and final order are verified, then delete them last.

Do not rasterize editable source narrative text merely to preserve its appearance. Recreate it as native Google Slides text using the template's typography and hierarchy. Text may remain rasterized only when it is intrinsically part of a required screenshot or other source media asset.

## Work Efficiently

Read, parse, and render each unchanged template or content source only once. Reuse the local design system, catalog, PDF, and rendered images.

Complete all planned slide construction and content population before output visual QA. Confirm the delivered slide IDs through one live structural readback, then remove unused template-library slides and establish the final order before the first output PDF render.

Read and parse the output once after its final slide set and order are established. Reuse that output design system after text, style, image, or media repairs. Parse it again only when a structural mutation changes slide IDs, slide count, or slide order.

Before the first output PDF render, run the local issue checker on the raw presentation JSON already saved by that structural readback:

```bash
"$NODE" "$SKILL_DIR/scripts/check_output_issues.mjs" \
  --input "$WORKSPACE/raw-output.json" \
  --output "$WORKSPACE/output-issues.json"
```

The checker makes no API or render calls. It reports only compact, object-level findings for empty native bullet paragraphs, duplicate or typed bullet markers, explicitly undersized narrative text, unresolved generic placeholder text, empty text placeholders, and structurally blank slides. Repair every `error` before rendering. Treat `warning` findings as review prompts and preserve intentional template-native exceptions. Combine applicable repairs with the existing consolidated repair pass; do not add a read, parse, render, or diagnostic-rerun cycle solely to clear warnings.

Inspect every delivered slide from one output render and collect all concrete defects before repairing. Prefer one consolidated repair pass, but perform a second consolidated pass when defects remain. A structural rebuild invalidates prior visual QA: render the complete delivered deck again and use the second repair pass if needed. Do not perform more than two repair passes. Do not create additional read, parse, or render cycles without a concrete defect or structural change that invalidates an existing artifact.

Complete duplication and slide creation before reordering. Reorder in a separate mutation after structural readback, using each delivered slide ID exactly once.
