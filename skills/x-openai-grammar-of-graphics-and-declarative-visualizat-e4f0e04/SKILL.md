---
name: x-openai-grammar-of-graphics-and-declarative-visualizat-e4f0e04
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Build data visualizations with declarative grammars. Use when the user needs Vega-Lite, Vega, Observable Plot, or grammar-of-graphics reasoning, especially for tabular charts that do not require bespoke rendering.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Grammar of Graphics and Declarative Visualization

## Overview

Use this skill as the default implementation path for many tabular charts. Declarative grammars are often the fastest, clearest, and most maintainable route when the chart can be expressed as data plus marks plus encodings plus transforms.

This skill covers Vega-Lite, Vega, and Observable Plot. Default to the highest-level tool that cleanly expresses the needed chart and interaction.

## Selection Rules

1. Use Observable Plot for fast exploratory and explanatory charts in JavaScript when concise code is valuable.
2. Use Vega-Lite for portable, declarative specs, multi-view composition, transforms, and embed-friendly chart definitions.
3. Use Vega when the user needs lower-level control that still benefits from a declarative runtime.
4. Leave this skill and route to D3, Canvas, or the Three.js/WebGL skill only when the chart requires bespoke layout, extreme density, GPU-scale rendering, particles, true 3D, or rendering control that the grammar no longer expresses cleanly.

## Working Pattern

1. Normalize the table shape.
2. Name the mark, encodings, transforms, faceting, and interaction model explicitly.
3. Choose the highest-level grammar that supports the chart without contortions.
4. Keep specs readable and portable.
5. Check whether the declarative approach still fits the expected number of simultaneous chart instances on the page.
6. Check mobile portrait and optional landscape behavior: responsive spec, label/tick reduction, hover replacement, touch target policy, and whether the grammar can keep the main visualization visible around controls.
7. Use declarative composition before custom code.

## Output Expectations

- Explain why the chosen grammar fits better than bespoke rendering.
- Keep the spec readable enough to be reused, embedded, or translated across stacks.
- Call out when the declarative path is reaching its limits and a lower-level skill should take over.
- Call out whether the grammar can support the mobile concept contract or whether D3, Canvas, WebGL, or framework-owned layout should take over.
- For new work, include a technical design section covering instance-count assumptions, performance implications, and the maintenance upside of staying declarative.

## References

- Shared theory:
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/task-abstraction-and-chart-selection.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/perception-color-and-encoding.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/mobile-first-responsive-visualization.md`
  - `../../resources/plugins-6ebaff11/plugins/build-web-data-visualization/references/foundations/implementation-design-and-tradeoffs.md`
- Skill references:
  - `./references/vega-lite-and-vega.md`
  - `./references/observable-plot.md`
  - `./references/when-to-stay-declarative.md`

## Representative Prompts

- "Write a Vega-Lite spec for this dataset."
- "Should I use Plot, Vega-Lite, or D3 for this chart?"
- "Build a layered declarative chart with faceting and tooltips."
- "Tell me when this declarative approach stops being a good fit."
