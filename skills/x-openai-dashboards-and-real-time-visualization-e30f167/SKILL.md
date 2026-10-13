---
name: x-openai-dashboards-and-real-time-visualization-e30f167
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Design dashboards and live visualization systems. Use when the user needs monitoring views, streaming charts, coordinated interactions, downsampling, or performance-aware operational visualization.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Dashboards and Real-Time Visualization

## Overview

### Resolve package resources

The original `build-web-data-visualization` plugin supplied shared foundations and templates outside this skill. Resolve the resource identifiers below through the installed package, skill registry, or user-provided source copy; they are not relative filesystem paths in this export. Resolve related skills by their names. If a required resource is absent, report the missing dependency before the dependent step, without claiming to have read it. Self-contained guidance can still support analysis that does not need it.

Use this skill when the visualization is a system, not a screenshot. That means update cadence, latency, interaction design, observability, and rendering budgets matter as much as chart choice.

If the main request is about how to test a live dashboard, freeze streams, mock refresh behavior, or cover alerting and stale states end to end, route first to the installed `testing-data-visualizations` skill.

Mobile operational use is default unless explicitly excluded. Use `build-web-data-visualization:references/foundations/mobile-first-responsive-visualization.md` to plan the mobile portrait dashboard, optional landscape mode, touch interaction, on-screen keyboard behavior, spotty connection handling, and alerting or vibration strategy.

This skill covers three tightly related problems:

- real-time streaming and refresh behavior
- layout hierarchy and scan-first dashboard composition
- interaction patterns and coordinated views
- performance and scale

## Default Questions

1. What is the update model?
   - append-only stream
   - periodic polling
   - event bursts
   - full snapshot replacement
2. What latency matters?
   - sub-second monitoring
   - near-real-time operational review
   - asynchronous reporting
3. What must the user do?
   - notice anomalies
   - compare current versus historical
   - inspect causes
   - filter and drill down
4. What are the hard limits?
   - frame budget
   - memory budget
   - network budget
   - exportability
   - mobile bandwidth, battery, and thermal budget
5. How many visualization instances can be visible at once?
   - single focal chart
   - a few coordinated panels
   - many repeated tiles or sparklines
6. What mobile state must work under interruption?
   - spotty or offline connection
   - app backgrounding or tab visibility changes
   - one-handed use
   - alert acknowledgment
   - on-screen keyboard for filters or notes

## Real-Time Design Rules

- Show time windows clearly.
- Distinguish live data from historical context.
- Handle missing, late, and out-of-order events explicitly.
- Keep the last known good visualization visible during reconnects, with stale, delayed, partial, offline, and error states distinct from normal live data.
- Show last updated time and update cadence near the evidence.
- Use aggregation, downsampling, or rollups before raw point dumping.
- Provide alert thresholds, annotations, and state transitions, not just moving lines.
- Use vibration, system notifications, or push-style alerts only for user-requested and meaningful state changes; always provide an in-app visual and accessible alert path.
- Keep the most important metric stable in position and encoding.
- Keep keys with their charts: direct labels or chart-adjacent keys beat a shared legend parked elsewhere on the screen.
- Use sparklines and other microcharts when compact trend context helps scanning, but rely on nearby labels and values to carry meaning.
- Design dashboards around situation awareness, not around maximum tile count.
- Prefer self-explanatory panels and concise labels over instructional paragraphs scattered across the UI.

## Layout and Scanning Defaults

- Give the screen a clear focal path: current state first, then supporting context, then controls and secondary diagnostics.
- Avoid grids where every tile has equal visual weight unless the user truly needs uniform scanning across peers.
- Keep filters and toggles near the views they change instead of collecting everything in a distant control rail.
- Reserve callouts and narrative copy for anomalies, caveats, or actions. The normal state should be legible without tutorial text.
- Collapse or defer low-value controls so the live state stays visually dominant.
- On mobile, do not stack the filter rail or diagnostic controls before the live state. Use bottom sheets, drawers, tabs, or inline controls that return the user to the affected visualization after Apply, Cancel, Reset, or close.
- Use mobile landscape for monitoring views when a wide timeline, map, field, route, dense table, or multi-series trace is meaningfully clearer in a handheld wide orientation, but still provide a portrait summary.

## Interaction Patterns

- overview first, filter or focus, then details on demand
- overview plus detail
- focus plus context
- brush and link
- hover for preview, click for commitment
- tap/focus for preview, tap again or explicit action for commitment on touch devices
- drill-down and drill-through
- persistent selections that survive updates
- explicit reset and undo paths

Interactivity should reduce cognitive load, not hide essential context behind constant mouse movement.

For mobile dashboards, add step-through controls, search, or nearest-item selection for dense marks; do not rely on hover, pixel-perfect taps, or one-finger chart panning that traps page scroll.

## Performance Defaults

1. Budget for 16 ms frames only when truly needed.
2. Reduce work before optimizing code:
   - fewer marks
   - smarter aggregation
   - smaller repaint regions
   - lower-frequency updates where appropriate
3. Choose the renderer intentionally:
   - SVG for semantics and annotation
   - Canvas2D for dense 2D raster workloads
   - WebGL, deck.gl, PixiJS, Sigma.js, or Three.js for GPU-scale marks, maps, particles, graph rendering, or true 3D
4. Use ring buffers, viewport culling, and multi-resolution summaries for long-running live views.
5. Separate interaction state from render state so updates remain predictable.
6. Use particles or glow in dashboards only for active flow, alert state, focus, or recency. Avoid ambient motion that competes with monitoring.

## Output Expectations

- Describe the update model and failure modes.
- Describe mobile reconnect, stale-data, offline/partial-data, and low-bandwidth behavior.
- Explain what a user should understand at first scan before touching any controls.
- Explain what the mobile user sees first and how the main visualization remains visible around controls and keyboard input.
- Define the interaction contract before building widgets.
- State how the system degrades when data rate or mark count rises.
- Include a technical design section for new work covering simultaneous chart count, per-instance and page-level budgets, and maintenance implications of the chosen rendering strategy.
- Keep accessibility and export strategy visible.

## References

- Shared theory:
  - `build-web-data-visualization:references/foundations/storytelling-annotation-and-critique.md`
  - `build-web-data-visualization:references/foundations/layout-hierarchy-and-self-explanatory-ux.md`
  - `build-web-data-visualization:references/foundations/interaction-models-and-progressive-disclosure.md`
  - `build-web-data-visualization:references/foundations/mobile-first-responsive-visualization.md`
  - `build-web-data-visualization:references/foundations/implementation-design-and-tradeoffs.md`
- Skill references:
  - `./references/monitoring-vs-analysis.md`
  - `./references/streaming-data-pipelines.md`
  - `./references/interaction-patterns.md`
  - `./references/performance-and-degradation.md`
  - the installed `testing-data-visualizations` skill

## Representative Prompts

- "Build a real-time operations dashboard from a WebSocket feed."
- "Keep this live chart smooth with 100 updates per second."
- "Design brushing, cross-filtering, and annotations for this monitoring UI."
- "Tell me if this should be a dashboard or a report."
- "Critique this monitoring screen using operational dashboard principles."
