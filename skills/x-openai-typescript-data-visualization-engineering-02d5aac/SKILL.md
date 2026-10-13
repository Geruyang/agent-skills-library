---
name: x-openai-typescript-data-visualization-engineering-02d5aac
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Build typed data visualizations in TypeScript. Use when the user wants TypeScript visualization code, typed data models, browser visualization components, UML-like diagram models, interactive graph or architecture diagram contracts, scroll-driven scene contracts, library selection guidance, or a maintainable visualization architecture beyond React- or Next-specific concerns.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# TypeScript Data Visualization Engineering

## Overview

Use this skill when the visualization must live in a TypeScript application. The focus is not just chart rendering. The focus is reliable data contracts, clear component boundaries, maintainable integration architecture, and a renderer that fits the product surface.

If the request is specifically about React components, client or server boundaries, hydration, dynamic loading, or Next.js delivery constraints, route first to `../x-openai-react-and-nextjs-data-visualization-609c566/SKILL.md`.

If the request is primarily about test strategy, mocks, screenshot coverage, or deciding which chart logic deserves unit tests, route first to `../x-openai-testing-data-visualizations-9607dba/SKILL.md`.

## Renderer and Library Selection

- D3: custom chart math, behaviors, and bespoke SVG or hybrid views.
- Observable Plot or Vega-Lite wrappers: fast, declarative 2D charts.
- Visx, Recharts, ECharts, or Chart.js: product-oriented chart layers when their abstraction fits.
- Canvas2D adapters: dense flat views, immediate-mode rendering, and custom hit testing where Canvas is simpler than WebGL.
- WebGL adapters: dense GPU-scale 2D, particles, flow animation, custom shaders, GPU picking, or true 3D.
- Three.js: spatial, volumetric, instanced, particle, or camera-led 3D scenes.
- deck.gl, PixiJS, Sigma.js, Plotly WebGL traces, ECharts GL, MapLibre, CesiumJS, luma.gl, regl, TWGL, or raw WebGL2 when their renderer model matches the data shape.
- Scrollama, CSS ScrollTimeline/ViewTimeline, Motion `useScroll`, or GSAP ScrollTrigger when a scroll-driven scene controller is needed.
- Image generation pipeline: produced assets, transparent cutouts, textures, and scene backgrounds that remain separate from data-bound overlays.
- Mermaid, PlantUML/Kroki, Graphviz/WASM, D2, Structurizr, React Flow, Cytoscape.js, Sprotty, JointJS, GoJS, ELK, or Dagre when the surface is UML, ERD, C4, flow, state, schema, dependency, architecture, or interactive diagramming.

## TypeScript Rules

1. Define the data schema before rendering.
2. Validate external data at the boundary.
3. Keep derived chart geometry in typed functions.
4. Separate:
   - data loading
   - transformation
   - scale creation
   - rendering
   - interaction state
5. Model selections, filters, tooltip payloads, URL state, persisted preferences, and saved-view payloads as explicit types.
6. Define a canonical view-state codec for shareable state: parse, validate, normalize defaults, serialize in stable order, and migrate or reject stale schema versions.
7. Keep ephemeral interaction state separate from durable state. Hover, drag-in-progress, animation frame, and pointer position should not leak into saved URLs or persisted workspaces.
8. For new work, assess the intended number of simultaneous visualization instances so the architecture reflects page-level costs instead of single-instance demos.
9. For editorial systems, model reusable design tokens, annotation specs, label placement rules, artifact modes, motion states, asset manifests, color-role ledgers, and rubric checks as typed data instead of ad hoc strings inside render code.
10. For fictional, synthetic, or illustrative stories, model the data-generating world explicitly. Include seed, assumptions, entities, temporal records, spatial or physical substrate, event windows, outcomes, derived comparisons, and invariants. Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/fictional-data-story-simulation.md`.
11. For concepted editorial, report, deck, generated-image, animation, scrollytelling, or existing-page integration work, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md` and `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`. Apply the shared workflow for concept images, large-screen/mobile variants, approval or iteration, and typed semantic design contracts for evidence locks, responsive states, generated assets, fallbacks, and approved deviations.
12. For scrollytelling or parallax, use `../x-openai-scrollytelling-and-parallax-data-visualization-9b5580a/SKILL.md` and define a typed scene contract:
   - visible data layers
   - generated or illustrated assets
   - media assets
   - camera or transform state
   - annotation state
   - trigger or progress range
   - interaction state
   - static key frame
   - reduced-motion fallback
13. For generated imagery, keep asset metadata explicit: prompt version, source, dimensions, focal crop, label-safe regions, alt text, continuity group, and data fields that bind to it.
14. For UML-like or software architecture diagrams, use `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md` first and keep a renderer-neutral diagram model separate from Mermaid, PlantUML, React Flow, Cytoscape.js, Sprotty, JointJS, GoJS, DOT, D2, or Structurizr adapters.

## React Guidance

- Prefer React-owned structure and D3-owned math when both are in play.
- Keep expensive transforms out of repeated render paths.
- Use clear component boundaries between chart container, render layer, and controls.
- Plan export paths if the chart must appear in reports or documents.
- Treat specs, scales, derived marks, and tooltip payloads as explicit typed interfaces.
- Treat URL codecs, saved-view payloads, storage keys, schema versions, and invalid-state fallbacks as part of the visualization API.
- Treat editorial elements as first-class props: insight title, subtitle, artifact mode, source, notes, annotations, direct labels, motion states, image assets, large-screen layout, mobile portrait layout, optional mobile landscape layout, and mobile fallback.
- Model mobile interaction and resilience explicitly: pointer mode, touch target/hit-area policy, hover replacement, pinch/drag ownership, visual viewport or keyboard state, stale/offline/partial data state, permission-gated capability availability, and reduced-motion/low-power mode.
- For embedded visual stories, make specialist skill ownership explicit in data contracts or implementation notes so maps, swarms, distributions, flow layers, and export fallbacks are not treated as generic components.

## Output Expectations

- Pick libraries that fit the app architecture, not generic popularity.
- Keep types useful at runtime boundaries.
- Call out whether the chart is DOM, Canvas, WebGL, or hybrid.
- For WebGL, call out whether the implementation is Three.js, deck.gl, PixiJS, Sigma.js, Plotly/ECharts GL, MapLibre/Cesium, luma.gl/regl/TWGL, raw WebGL, or a hybrid overlay.
- For particles or flow animation, state what each particle represents, the clock model, reduced-motion behavior, and static fallback.
- For art-directed stories, call out whether imagery is generated or hand-authored, which layers remain data-bound, and how still-frame and reduced-motion fallbacks are represented.
- For concepted stories or figures, use the shared design workflow for concept images, approval status, binding semantic design contract type, approved references, locked and flexible elements, data-bound layer contracts, generated asset metadata, mobile/landscape continuation, approved deviations, and semantic fidelity checks.
- For scroll-driven stories, call out the scene contract, controller, native-scroll behavior, static frames, reduced-motion path, and mobile fallback.
- For interactive tools, call out the URL view-state contract, persisted-state tiers, precedence rules, copy-link behavior, back/forward behavior, and collapsed-control state.
- For mobile-capable tools, call out the mobile portrait and optional landscape contracts, main-visualization visibility rule, touch/pinch/keyboard behavior, spotty-connection handling, and justified AR/camera/motion/vibration/notification capabilities.
- For fictional stories, call out the simulation seed, regeneration path, data richness layers, invariants, and derived datasets that support each embedded visualization.
- Include a technical design section for new work covering instance-count assumptions, performance implications, and maintenance tradeoffs of the chosen contracts and renderer.

## References

- Shared theory:
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/editorial-infographic-system.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/art-directed-interactive-visual-stories.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/meaning-preserving-visual-design-workflow.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/fictional-data-story-simulation.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/task-abstraction-and-chart-selection.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/perception-color-and-encoding.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/shareable-state-and-persistence.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/implementation-design-and-tradeoffs.md`
- Skill references:
  - `../x-openai-react-and-nextjs-data-visualization-609c566/SKILL.md`
  - `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md`
  - `../x-openai-scrollytelling-and-parallax-data-visualization-9b5580a/SKILL.md`
  - `../x-openai-testing-data-visualizations-9607dba/SKILL.md`
  - `./references/library-selection-for-builders.md`
  - `./references/react-and-framework-boundaries.md`
  - `./references/types-and-data-contracts.md`
  - `./references/export-and-product-integration.md`

## Representative Prompts

- "Build a typed React charting system."
- "Design the TypeScript chart contracts behind a React or Next.js visualization surface."
- "Design the typed scene contract for a scrollytelling or parallax data story."
- "Choose a TypeScript visualization library for this product."
- "Convert this D3 prototype into maintainable TypeScript."
- "Embed Vega-Lite or Observable Plot in a React app without losing control."
- "Design the types for selections, tooltips, and chart data contracts."
- "Design typed contracts for an interactive UML, ERD, architecture, state machine, or dependency diagram."
