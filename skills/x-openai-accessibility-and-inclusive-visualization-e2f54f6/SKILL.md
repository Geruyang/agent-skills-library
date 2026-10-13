---
name: x-openai-accessibility-and-inclusive-visualization-e2f54f6
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Make data visualizations accessible and inclusive. Use when the user needs chart or diagram accessibility guidance, text alternatives for complex visuals, color and contrast review, keyboard support, reduced-motion behavior for animation or parallax, or an accessibility QA workflow for exported figures, UML-like diagrams, and dashboards.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Accessibility and Inclusive Visualization

## Overview

Use this skill when a visualization must be understandable by more people, in more contexts, with more assistive needs. Accessibility is not a post-processing step. It shapes chart selection, color, labeling, interaction, fallback text, and export strategy.

Default assumption: every important visualization should have a non-visual path to the key insight, whether through surrounding text, direct labels, data tables, or formal text alternatives.

## Working Pattern

1. Identify whether the chart is exploratory, explanatory, interactive, or exported.
2. Decide which information must remain available without hover, color discrimination, pointer precision, expanded panels, private persisted state, permission-gated capabilities, or a strong connection.
3. If the story uses generated imagery, illustration, WebGL, particles, 3D, maps, scrollytelling, parallax, or animation, separate what the asset shows from what the data proves.
4. If an available image-generation capability was used for a layout, figure, page-integration, asset, or key-frame concept, verify that the large-screen and mobile concept images were shown with concise plan and interaction bullets, the user approved the generated design set before project changes or implementation code began, and the semantic design contract from `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md` exists: the accessible path must preserve the same claim, caveat, source context, evidence hierarchy, locked layout elements, mobile continuation, and interaction meaning as the visual design.
5. If the view is a UML-like, ERD, state machine, workflow, dependency, or architecture diagram, preserve a text outline of nodes, groups, relationships, and selected paths; use `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md` for diagram-specific semantics.
6. Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md` to verify touch targets, drag alternatives, keyboard-open visual viewport behavior, main-visualization visibility, spotty-connection states, and fallbacks for AR, camera, motion, vibration, notifications, and geolocation.
7. Provide direct labels, strong contrast, redundant encodings, keyboard paths, reduced-motion alternatives, accessible disclosure controls, and text alternatives.
8. For interactive visualizations, check that shared URLs, saved views, refresh, and back/forward navigation preserve the same accessible state summaries as the visual surface.
9. Test both the chart or diagram and the surrounding narrative.

## Output Expectations

- Name the accessibility risks specific to the chart, not just generic WCAG items.
- Provide fallback strategies for screen readers, PDFs, and static exports.
- Explain what to keep visible without relying on hover or color alone.
- Explain which active filters, selections, caveats, and summary values remain visible when configuration or drill-down panels are collapsed.
- For color guidance, name the semantic color roles, contrast risks, redundant encodings, and grayscale or color-deficiency review path.
- For image-supported visual stories, provide alt text or long descriptions that cover the scene, the data layer, the main takeaway, and the caveat without overstating generated imagery.
- For concepted visualizations, make sure the user approval record exists and the long description, reduced-motion path, static export, and source/caveat text preserve the approved semantic design contract and locked concept elements, not just the final rendered pixels.
- For mobile visualizations, make sure the main evidence is not pushed below settings, touch targets and hit areas are large enough, drag has alternatives, hover has tap/focus equivalents, keyboard-open states remain operable, stale/offline states are named, and sensor/camera/notification features have non-permission fallbacks.
- For animation, specify reduced-motion behavior and key-frame or final-state fallback.
- For scrollytelling or parallax, preserve native scroll and keyboard behavior, specify static key frames or stacked fallback, and make sure motion can be disabled without losing the evidence.
- For WebGL or particle effects, describe the data meaning in text, expose keyboard-accessible focus or selection paths for important marks, and provide a non-animated fallback that preserves flow, direction, focus, and uncertainty.
- For interactive diagrams, make search, selection, details panels, reset, export, expand/collapse, and drill-down reachable without pointer-only interaction.
- For shareable visualizations, make copy-link, saved-view, reset, expanded/collapsed panels, and restored URL state reachable and understandable by keyboard and screen-reader users.

## References

- Shared theory:
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/perception-color-and-encoding.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/storytelling-annotation-and-critique.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`
- Skill references:
  - `./references/text-alternatives-and-complex-images.md`
  - `./references/color-contrast-and-redundant-encoding.md`
  - `./references/keyboard-screen-reader-and-export.md`
  - `./references/testing-and-review-workflow.md`
  - `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md`
  - `../x-openai-scrollytelling-and-parallax-data-visualization-9b5580a/references/accessibility-testing-and-review.md`

## Representative Prompts

- "Make this chart accessible."
- "How should I write alt text or a long description for this visualization?"
- "Review this dashboard for color, keyboard, and screen-reader issues."
- "What needs to change before this chart goes into a PDF report?"
- "How do I design tooltips and hover interactions without excluding people?"
- "Make this parallax scrollytelling visualization safe for reduced-motion users."
- "Make this UML, ERD, workflow, state machine, or architecture diagram accessible."
