---
name: x-openai-node-link-and-diagram-layout-4c4839c
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Choose and apply automatic layout strategies for node-link diagrams and connected-node visuals. Use when the user asks how to auto-arrange nodes, reduce line crossings, route edges, avoid overlaps, stabilize layout, or choose graph-layout algorithms for network diagrams, dependency graphs, database schema diagrams, ERDs, state machines, decision trees, flow diagrams, box-and-line editors, or other line-connected nodes.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Node-Link and Diagram Layout

## Overview

Use this skill when the main problem is not which notation to use, but how to place connected nodes so the diagram stays readable. The job is to classify the graph family, choose a layout algorithm that matches the reading task, separate node placement from edge routing and overlap removal, and recommend a stack that can preserve those constraints in production.

Default assumption: the best automatic layout is the one that reinforces the intended reading path with the fewest crossings, bends, overlaps, and surprise placements. Do not treat force-directed layout as a generic answer for all diagrams. Trees, DAGs, port-constrained block diagrams, ERDs, and undirected exploration graphs usually need different algorithms.

For browser-facing node-link views, mobile layout is a graph-reading constraint, not only a CSS breakpoint. Use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md` when choosing portrait focus views, optional landscape inspection, touch/pan/zoom ownership, and settings placement.

For operational graph workspaces, use `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/operational-visualization-workspaces.md` so layout decisions account for outlines, inspectors, command bars, selected neighborhoods, URL state, mobile panels, and repeated navigation.

## Core Workflow

1. Classify the graph structure before choosing a renderer:
   - rooted tree or forest
   - directed acyclic graph
   - cyclic directed graph with a dominant flow
   - general undirected graph
   - radial or hub-and-spoke structure
   - clustered or compound graph
   - port-constrained block diagram
   - table-like schema or ERD
   - nearly planar topology where crossing count dominates readability
2. Identify the primary reading task:
   - parent-child depth
   - top-to-bottom or left-to-right flow
   - reachability and dependency tracing
   - cluster discovery
   - cycle inspection
   - shortest path or neighborhood exploration
   - table relationship tracing
   - stable editing with minimal layout drift
3. Record geometry constraints up front:
   - real node widths and heights, not point nodes
   - labels that must fit without scaling below readability
   - ports, handles, side constraints, or fixed connection order
   - nested groups, lanes, clusters, or compounds
   - whether some nodes are pinned or semi-pinned
4. Choose the layout family that matches the structure:
   - tidy tree layout for rooted ordered trees and decision trees
   - layered or Sugiyama-style layout for directional processes, state machines, dependency maps, class hierarchies, ERDs, and most UML-like flow diagrams
   - stress majorization or force-directed layout for undirected relational exploration where cluster shape matters more than global direction
   - radial or concentric layout when distance from a root is the main story
   - circular layout when cycle structure is the evidence
   - planarization-driven layout when the graph is non-planar but low crossing count is the main objective
5. Choose edge routing separately from node placement:
   - straight or polyline when the graph is sparse and directional flow is already clear
   - orthogonal when tables, ports, block diagrams, lanes, or circuit-like reading dominate
   - spline routing when static aesthetics matter more than precise traceability and there is enough whitespace
6. Treat overlap removal, label placement, and packing as explicit phases:
   - remove node overlap after layout if the engine starts from point nodes
   - reserve gutters for connector-dense tables and schemas
   - keep edge labels out of node bodies and above selected paths
   - pack connected components only after the component layouts are individually legible
7. Prefer stability when users will edit, compare revisions, or recognize repeated diagrams:
   - preserve node order when the source model has meaningful order
   - preserve port order when connectors are semantically ordered
   - use interactive or constraint-aware layered modes instead of re-randomizing
8. Validate the result with readability criteria instead of trusting the engine:
   - crossings are low enough for the task
   - bends are limited and meaningful
   - nodes and labels do not overlap
   - directionality is obvious
   - edge tracing is possible without visual hunting
   - the layout stays readable on narrow widths or falls back to scrolling, filtering, or faceting
   - mobile portrait starts on the most important region instead of shrinking the entire graph
   - mobile landscape is offered when a wide graph, timeline, or schema materially improves tracing
   - operational shells keep filters, outline trees, selected nodes, and inspectors synchronized without stealing space from the graph

## Algorithm Defaults

- Rooted ordered trees and decision trees:
  - Prefer Reingold-Tilford style tidy trees and Buchheim's linear-time refinement.
  - Use radial tree variants only when depth from a root matters more than label density.
  - Do not use generic force layout for decision trees unless the tree metaphor itself is intentionally abandoned.
- State machines, dependency graphs, workflow diagrams, class hierarchies, ERDs, and most UML-like directional diagrams:
  - Prefer layered layout derived from Sugiyama.
  - Use cycle breaking, layer assignment, crossing minimization, node placement, and edge routing as separate concerns.
  - For table schemas, state diagrams, and block diagrams with connector semantics, prefer port-aware layered layout with orthogonal routing.
- General undirected networks:
  - Prefer stress majorization or force-directed placement when cluster shape, neighborhood, or approximate graph distance is the point.
  - Prefer multilevel force methods for larger graphs.
  - Avoid force layout when users need strict rank order, deterministic business flow, or table-like schemas.
- Large topology where the graph is dense and not meaningfully hierarchical:
  - Use multilevel force approaches, filtering, clustering, matrix fallbacks, or multiple coordinated views before cramming everything into one node-link view.
- Nearly planar but non-planar graphs:
  - Consider planarization pipelines when crossing count matters more than preserving a strict hierarchy.
  - Treat this as an advanced fallback, not a default for ordinary UML-like diagrams.

## Stack Defaults

- Graphviz `dot`: best default for static layered layouts in documentation or build-time generation.
- Graphviz `neato`: good default for modest undirected graphs when stress majorization is appropriate.
- Graphviz `fdp` and `sfdp`: good for force-directed and multilevel force layouts, especially for larger undirected networks.
- Graphviz `twopi` and `circo`: use when radial or circular structure is truly the reading model.
- ELK Layered: best default for interactive products that need layered layout with ports, compounds, labels, orthogonal routing, or layout constraints.
- React Flow plus ELK or Dagre: good for node editors when React owns the interaction layer and the actual layout engine remains external.
- Cytoscape.js: good when graph analysis, graph algorithms, and multiple layout modes matter as much as the rendering.
- Bespoke SVG, Canvas, or WebGL: use only when the visual composition or scale requires it after the algorithm family is already decided.

## Anti-Patterns

- Using force-directed layout for ERDs, state machines, or business workflows that have a clear direction.
- Treating overlap removal as a substitute for choosing the right layout family.
- Ignoring real node dimensions and then trying to fix collisions at the end.
- Letting connectors run under schema tables, lane headers, or large node labels.
- Relying on a single dense node-link view when a matrix, tree, outline, focus view, or filtered subgraph would explain the structure better.
- Re-running unstable layout from scratch after every small edit in an interactive tool.
- Shrinking text below readable size instead of using an intrinsic canvas and scrollable viewport.
- Letting mobile controls or legends appear before the graph while the actual topology starts below the fold.
- Requiring pixel-perfect taps on dense nodes without search, step-through, or enlarged hit regions.

## Reference Guide

- Read `references/algorithm-selection.md` first for graph-family to algorithm-family mapping.
- Read `references/layered-tree-force-and-radial-layouts.md` when choosing among tree, layered, force, radial, circular, and multilevel approaches.
- Read `references/routing-overlap-and-quality.md` for orthogonal routing, planarization, overlap removal, port constraints, and readability criteria.

## Output Expectations

- State the graph family and why it was classified that way.
- State the recommended layout family and one fallback.
- State the routing style, overlap strategy, and stability strategy.
- Call out whether ports, order constraints, fixed nodes, or compounds require a layout engine with stronger constraint support.
- For product work, recommend a concrete stack and make clear which part owns semantics, layout, and rendering.
- If the graph is too dense for a clean node-link view, say so and recommend filtering, faceting, clustering, matrix views, or overview-plus-detail.
- For mobile, state the portrait focus strategy, landscape need if any, touch target/hit-area policy, search or step-through path, and pan/zoom/browser gesture ownership.
- For operational graph workspaces, state the shell, default selected or focused neighborhood, outline/inspector synchronization, URL state, and empty-surface clear-selection behavior.
- If the problem is really notation selection, route to the UML or strategy skill instead of over-solving layout alone.

## Adjacent Skills

- `../x-openai-data-visualization-ae23089/SKILL.md`
- `../x-openai-uml-and-software-architecture-visualization-8275677/SKILL.md`
- `../x-openai-typescript-data-visualization-engineering-02d5aac/SKILL.md`
- `../x-openai-react-and-nextjs-data-visualization-609c566/SKILL.md`
- `../x-openai-d3-data-visualization-94d53d3/SKILL.md`
- `../x-openai-canvas2d-data-visualization-1b7046b/SKILL.md`
- `../x-openai-threejs-data-visualization-dce6db6/SKILL.md`
- `../x-openai-testing-data-visualizations-9607dba/SKILL.md`
- `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`
- `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/operational-visualization-workspaces.md`

## Representative Prompts

- "How should I auto-arrange this network diagram so the lines stop crossing so much?"
- "What layout algorithm should I use for a database schema diagram?"
- "Choose between ELK, Graphviz, Dagre, force layout, and a custom approach for this state machine."
- "Make this dependency graph readable without overlapping boxes and labels."
- "How do I route edges for an ERD so foreign keys do not run under the tables?"
- "What should I use for a decision tree, a DAG, and an undirected network?"
- "We need stable auto-layout in a React node editor."
