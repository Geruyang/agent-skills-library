---
name: x-openai-react-and-nextjs-data-visualization-609c566
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Integrate data visualizations into React and Next.js applications. Use when the user needs chart components, UML-like or architecture diagram components, React integration patterns, Next.js client or server boundaries, hydration-safe rendering, lazy loading, framework-aware performance, scroll-driven visual stories, or export guidance.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# React and Next.js Data Visualization

## Overview

Use this skill when the visualization lives inside a React or Next.js product surface. The focus is not just chart rendering. The focus is component ownership, hydration safety, client and server boundaries, bundle strategy, and clean integration between React and whichever visualization layer is actually drawing the marks.

Default assumption: React should own structure, layout, and application state, while the visualization layer owns scales, geometry, and narrowly scoped imperative rendering.

If the main request is about screenshot testing, visual regression, mocked chart data, or E2E coverage strategy, route first to `../x-openai-testing-data-visualizations-9607dba/SKILL.md` and pair back to this skill only for React- or Next-specific implementation details.

## Choose This Skill When

- the user is building charts inside React components
- the app is using Next.js, the App Router, or server and client component boundaries
- the chart uses D3, Canvas, SVG, Vega-Lite, Plot, WebGL, deck.gl, PixiJS, Sigma.js, or Three.js inside a React surface
- the surface uses Mermaid, React Flow, Cytoscape.js, Sprotty, JointJS, GoJS, ELK, Dagre, Graphviz/WASM, D2, or another UML-like diagram renderer
- hydration, SSR, dynamic loading, or browser-only APIs affect the implementation
- bundle size, route-level loading, and product integration matter
- the page is an editorial visual story that combines React layout, scroll states, parallax, sticky graphics, generated assets, SVG/Canvas/D3/WebGL/Three.js layers, particles, flow animation, and accessibility fallbacks

## Working Pattern

1. Decide which parts are server-safe and which must run in the browser.
2. Keep data loading, transformation, chart configuration, and render-layer concerns separated.
3. Estimate how many chart instances can be visible on a page at once and whether expensive work can be shared across them.
4. Let React own layout, controls, routing state, persistence affordances, and active-state summaries.
5. Let D3, Canvas, Vega-Lite embeds, Plot, WebGL libraries, or Three.js own the mark-level rendering.
6. Model URL-backed view state explicitly before wiring controls: filters, range, metric, comparison, selected entity, active tab, map bounds, zoom, camera target, and drill-down path.
7. Use localStorage only for tiny personal preferences; use IndexedDB or remote storage for larger saved views, drafts, cached slices, custom annotations, or shared/cross-device workspaces. Incoming URL state should override persisted defaults.
8. Use dynamic loading or client-only boundaries intentionally for browser-only visualization code.
9. If the chart owns wheel, pinch, or drag interactions, make the browser contract explicit. Use a non-passive native listener or library hook when default scrolling must be canceled, and do not assume framework-level `onWheel` is enough.
10. For editorial or infographic surfaces, keep the insight title, artifact mode, subtitle, annotation plan, source note, large-screen layout, mobile portrait layout, optional mobile landscape layout, and chart render layer as explicit component responsibilities. Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md` for touch, keyboard, visual viewport, spotty-connection, and device-capability decisions.
11. For scrollytelling or parallax, use `../x-openai-scrollytelling-and-parallax-data-visualization-9b5580a/SKILL.md` for the story contract. Model scenes as typed state rather than ad hoc scroll math. Each scene should define visible layers, annotation text, media assets, camera or transform state, trigger/progress range, static key frame, and reduced-motion fallback.
12. For advanced editorial, report, deck, generated-image, animation, or existing-page integration work, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md` and `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md` before implementation. Apply the shared workflow for concept images, large-screen/mobile variants, approval or iteration, and the binding semantic design contract React must implement.
13. For generated imagery or illustration, keep assets in deterministic public paths or importable modules, and keep labels/data overlays in React-owned, editable layers.
14. For WebGL, keep renderer lifecycle, resize, context loss, disposal, and animation loops inside a narrow client-only component boundary. React should pass data versions and props, not mutate GPU objects throughout the tree.
15. For interactive UML, ERD, dependency, state machine, flow, or architecture diagrams, use `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md` first; React should own app state, panels, controls, routing, and persistence while the diagram layer owns layout/rendering details.
16. For operational workspaces, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/operational-visualization-workspaces.md` before component decomposition. React should own shell state, command bars, drawers, rails, active summaries, URL state, and inspector synchronization while the visualization layer owns geometry, layout, and picking.

## Next.js Guidance

- Prefer Server Components for data fetching, framing content, and layout when the chart does not need browser APIs there.
- Use Client Components for interactive charts, measuring containers, pointer events, or browser-only libraries.
- Use dynamic imports when the charting runtime is not needed on the initial path or should avoid SSR.
- Keep chart assets and export paths deterministic when the same visualization must appear in reports or documents.
- Use route params or search params as the canonical input for shareable view state when possible. Parse and normalize them before initializing client-only chart state so linked views do not flicker through unrelated defaults.
- Use replace-style navigation for high-frequency transient changes and push-style navigation for committed selections, applied filters, drill-down steps, and saved-view transitions.
- For publication-style pages, design desktop and mobile compositions as sibling states, not as a single squeezed SVG.
- On mobile, keep the main visualization first or immediately available. Put secondary filters, inspectors, and settings in collapsible panels, drawers, bottom sheets, or inline controls that preserve active-state summaries and return focus/scroll to the chart after Apply, Cancel, Reset, or close.
- For dense workspaces, prefer a desktop outline/control rail, central viewport, and inspector rail; use a mobile command bar with outline, filter, and details panels instead of stacking the desktop rails above the visualization.
- Use `window.visualViewport` or equivalent resize handling for keyboard-heavy controls so search, filter, and annotation flows do not hide the only critical action or permanently obscure the visualization.
- Use Pointer Events for custom touch/pen/mouse interactions when possible, with explicit `touch-action`, enlarged hit areas, drag alternatives, reset controls, and no hover-only evidence.
- Use IntersectionObserver, Scrollama, Motion `useScroll`, GSAP ScrollTrigger, CSS scroll timelines, or explicit step controls sparingly and accessibly. The default view should still communicate the claim.
- Prefer native scroll and `position: sticky` for pinned story sections. Avoid scrolljacking and keep wheel, touch, scrollbar, and keyboard behavior predictable.
- Use `prefers-reduced-motion` to switch animated stories to final-state, key-frame, or stepped layouts.
- Lazy-load heavy WebGL, 3D, video, or image-generation-derived assets without causing layout shift. Reserve aspect ratios and label lanes.
- Pause WebGL animation loops when offscreen, route-hidden, tabbed away, or reduced-motion is active.

## Output Expectations

- Name the ownership boundary between React and the visualization layer.
- For explanatory work, name the insight title, artifact mode, annotation layer, direct-label strategy, and mobile reading path.
- For mobile work, name the mobile portrait layout, whether landscape is supported, how controls avoid covering the chart, how the on-screen keyboard behaves, and how touch/pinch interactions map to selection, zoom, pan, and reset.
- For operational workspaces, name the shell components, default selected state, synchronized outline/search/filter/inspector behavior, empty-surface clear-selection rule, mobile command panels, and URL-backed workspace state.
- For art-directed work, name generated or illustrated assets, scroll/animation states, reduced-motion behavior, and still-frame fallback.
- For concepted surfaces, use the shared design workflow for concept images, approval status, approved references, binding semantic design contract, locked and flexible elements, React-owned data layers, renderer-owned layers, mobile/landscape continuation, and approved deviations.
- For scrollytelling or parallax, name the scroll controller, scene contract, trigger/progress ranges, sticky layout, mobile fallback, and static key frames.
- For WebGL or particles, name the renderer, data-to-buffer boundary, animation clock, cleanup/disposal path, reduced-motion behavior, and static fallback.
- Call out any client-only or hydration-sensitive code explicitly.
- Call out any interaction that must suppress native browser scrolling or scroll chaining.
- Call out which state is URL-backed, locally persisted, IndexedDB-backed, remote-saved, or intentionally ephemeral.
- Call out copy-link, saved-view, reset, refresh, back/forward, and invalid URL-state behavior.
- Call out which control or detail areas are collapsed by default or closable, and how active state remains visible.
- Call out live-data connection behavior on mobile: stale state, reconnect, offline/partial data, lower-bandwidth mode, and alerting/notification strategy when relevant.
- State whether the chart is a good fit for SSR, client-only rendering, or dynamic loading.
- For new work, include a technical design section covering simultaneous instance count, per-instance versus page-level performance, and maintenance implications of the chosen integration pattern.
- Keep bundle size, export needs, and accessibility visible in the design.

## References

- Shared theory:
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/editorial-infographic-system.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/art-directed-interactive-visual-stories.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/task-abstraction-and-chart-selection.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/perception-color-and-encoding.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/shareable-state-and-persistence.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/operational-visualization-workspaces.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/implementation-design-and-tradeoffs.md`
- Skill references:
  - `./references/react-component-patterns.md`
  - `./references/d3-canvas-and-grammar-in-react.md`
  - `./references/nextjs-client-server-boundaries.md`
  - `./references/lazy-loading-ssr-and-bundle-strategy.md`
  - `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md`
  - `../x-openai-scrollytelling-and-parallax-data-visualization-9b5580a/SKILL.md`
  - `../x-openai-testing-data-visualizations-9607dba/SKILL.md`

## Representative Prompts

- "How should I integrate this chart into a React app?"
- "What is the right React pattern for D3, Canvas, or Vega-Lite here?"
- "Make this visualization work cleanly in Next.js App Router."
- "Build a React scrollytelling story with sticky graphics and reduced-motion fallback."
- "Should this chart be a Client Component or use dynamic import?"
- "Help me avoid hydration and SSR issues with this visualization."
- "Build an interactive React UML, ERD, flow, state machine, dependency, or architecture diagram."
