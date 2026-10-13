---
name: x-openai-scrollytelling-and-parallax-data-visualization-9b5580a
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Design and implement parallax scrolling and scrollytelling data visualizations. Use when the user asks for parallax scrolling, scrollytelling, scroll-driven timelines, sticky graphics, Scrollama, ScrollTrigger, ScrollTimeline, view timelines, rich-media timelines, moviescrollers, scroll-scrubbed charts, staged narrative reveals, or interactive visual stories where scrolling changes a data visualization or media scene.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Scrollytelling and Parallax Data Visualization

## Overview

Use this skill when scrolling is part of the explanation, not just navigation. Scrollytelling is an author-led narrative structure in which text, data marks, imagery, video, maps, or camera states change as the reader scrolls. Parallax is one possible scrollytelling technique: layers move at different rates to create depth, reveal scale, or connect foreground evidence to background context.

Default assumption: preserve native scrolling and make every scene meaningful as a still. Do not use parallax or scroll-scrubbed motion as decoration. Use it only when staged reveal, state change, elapsed time, spatial movement, or rich-media synchronization materially reduces interpretation cost.

## When To Use It

- A timeline, map, chart, 3D scene, video, or illustrated substrate needs staged reveal while the reader scrolls.
- The story benefits from a linear author-led path before optional reader exploration.
- A sticky graphic, side-by-side text/visual layout, overlay text on media, or scroll-scrubbed transition is being planned or implemented.
- The user mentions Scrollama, GSAP ScrollTrigger, Motion `useScroll`, CSS `ScrollTimeline`, ViewTimeline, IntersectionObserver, `position: sticky`, parallax layers, moviescroller, or scroll-driven animation.

Avoid scrollytelling when the story is clearer as a static chart, direct-label small multiples, a conventional article with inline figures, or an explicit stepper. Prefer a stepper when the states are discrete and the reader needs direct access, known length, replay, or controlled comparison more than continuous scroll.

## Working Pattern

1. Define the story contract:
   - one-sentence takeaway
   - author-led sequence and any reader-controlled exploration
   - why scrolling is necessary
   - what the first frame, each key frame, and final frame prove
2. For fictional, synthetic, or illustrative stories, require a data-rich simulation before storyboarding. Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/fictional-data-story-simulation.md` to define entity, temporal, spatial or physical, event, outcome, and derived comparison layers.
3. For art-directed, image-supported, composite, or existing-page scrollytelling work, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md` and `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`. Apply those shared references for concept generation with an available image service, large-screen/mobile variants, approval or iteration, scene contracts, and implementation deferral.
4. Choose the scrollytelling technique:
   - graphic sequence
   - animated transition
   - pan and zoom
   - moviescroller
   - show-and-play
   - parallax depth layer
   - sticky side-by-side or overlay
   - stacked mobile fallback or mobile-specific stepper
5. Model scenes as data, not ad hoc scroll math. Each scene declares text, visual state, data layer, media asset, annotation, scroll trigger or progress range, reduced-motion fallback, static key frame, embedded visualization skill owner, visual-density role, interactive discovery affordance, asset-continuity requirement, scroll-controlled media behavior, and any approved concept/key-frame contract. Approved key-frame concepts are binding scene contracts: the implementation must preserve their evidence hierarchy, staging, label-safe regions, interaction meaning, and static fallback unless a deviation is approved or recorded as meaning-preserving.
6. For each embedded visual layer, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/embedded-visualization-self-use.md` to name the primary specialist owner and mini-brief the layer's job, data shape, encoding, interaction, fallback, accessibility, QA check, and delegated or local fresh-pass status before scene composition.
7. Require every scene to include at least one evidence-bearing visual change: chart transition, map or layer reveal, annotation shift, camera move, particle or flow state, video frame or state, or interactive hotspot. If the scene only adds drama, simplify or add real evidence.
8. Pick the lightest implementation:
   - native scroll and `position: sticky` for pinning
   - IntersectionObserver or Scrollama for step triggers
   - CSS scroll-driven animations for simple transform or opacity when support and fallback are acceptable
   - Motion or GSAP ScrollTrigger for complex React choreography, scrubbing, pinning, snapping, or timeline labels
   - D3/SVG, Canvas2D, WebGL, deck.gl, PixiJS, Three.js, or video only when the visual layer requires it
9. Protect the browser contract:
   - do not scrolljack
   - keep feedback immediate, reversible, and interruptible
   - preserve standard wheel, touch, scrollbar, and keyboard behavior
   - avoid surprise autoplay, especially audio
   - account for mobile browser chrome, changing viewport height, touch momentum, and keyboard-open states
10. Build accessibility and fallbacks before polish:
   - honor `prefers-reduced-motion`
   - provide static key frames, a stacked version, or a stepped fallback
   - keep focus order and reading order coherent
   - ensure the main claim survives screenshots and static export
11. Test performance and interpretation:
   - profile scroll jank on desktop and mobile
   - verify no layout thrashing or layout-triggering animation
   - reserve media dimensions and lazy-load offscreen assets
   - test fast scroll, reverse scroll, resize, reduced motion, keyboard navigation, and mobile browser chrome changes

## Routing

- Use `../x-openai-visualization-strategy-and-critique-0e43db4/SKILL.md` first when deciding whether the story should be scrollytelling, a stepper, small multiples, or a static editorial chart.
- Use `../x-openai-react-and-nextjs-data-visualization-609c566/SKILL.md` when the implementation is a React or Next.js story surface, especially with hydration, client-only libraries, dynamic imports, or route-level asset loading.
- Use `../x-openai-d3-data-visualization-94d53d3/SKILL.md` when SVG data marks, labels, annotations, and scene-state transitions are the core work.
- Use `../x-openai-canvas2d-data-visualization-1b7046b/SKILL.md` when dense flat marks or custom hit testing make SVG too heavy.
- Use `../x-openai-threejs-data-visualization-dce6db6/SKILL.md` when WebGL, GPU layers, particles, flow, or camera-led 3D are necessary.
- Use `../x-openai-geospatial-and-cartographic-visualization-145505f/SKILL.md` for map scrollytelling, fly-to sequences, route stories, or pan/zoom geography.
- Use `../x-openai-accessibility-and-inclusive-visualization-e2f54f6/SKILL.md` when motion sensitivity, keyboard path, screen-reader alternatives, or static fallbacks are central.
- Use `../x-openai-testing-data-visualizations-9607dba/SKILL.md` when validating scroll states, visual regression, render readiness, media loading, or reduced-motion behavior.
- Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/fictional-data-story-simulation.md` when sparse invented data would otherwise force the scroll story to rely on walls of text, decorative parallax, or generic chart tiles.

## Output Expectations

- State whether scrollytelling is justified and what would be lost in a simpler format.
- Name the scrollytelling technique and the reader's path through scenes.
- Provide a scene contract with trigger/progress ranges and static fallbacks.
- For agent-generated image layout or key-frame concepts, use the shared design workflow for concept images, approval status, approved references, binding semantic design contract, locked and flexible elements, data-bound layers, mobile/landscape continuation, approved deviations, and concept-to-result fidelity checks.
- For every embedded visual layer, provide the specialist owner, mini-brief summary, QA check, and whether delegated fresh context, a local fresh specialist pass, or a lightweight exception was used.
- For fictional stories, provide the simulated-world data richness contract and the specialist mini-brief for every embedded visualization layer.
- Name the implementation stack and why it is the lightest reliable option.
- Call out browser behavior explicitly: native scroll, sticky pinning, event listeners, scroll ownership, and keyboard behavior.
- State reduced-motion behavior, mobile portrait path, optional landscape path, media loading plan, spotty-connection behavior, and performance risks.
- Include the first-frame, key-frame, final-frame, and screenshot acceptance criteria.

## References

- `./references/story-patterns-and-scene-contracts.md`
- `./references/implementation-and-performance.md`
- `./references/accessibility-testing-and-review.md`
- `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md`
- `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/embedded-visualization-self-use.md`
- `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`

## Representative Prompts

- "Make a parallax scrolling timeline with maps and video."
- "Use Scrollama for a data story."
- "Should this be scrollytelling or a stepper?"
- "Design a scroll-driven visualization that is accessible and performant."
- "Build a sticky graphic story where the chart changes as the reader scrolls."
- "Storyboard a moviescroller that advances video frames with scroll progress."
