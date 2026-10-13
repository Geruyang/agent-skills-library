---
name: x-openai-produce-f594139
description: Use when the user wants to create, explore, adapt, refine, polish, or review visual creative such as campaigns, ads, social posts, product imagery, scenes, offers, logos, brand systems, styles, charts, decks, or related marketing and design assets.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Produce

Produce is the main Creative Production workflow. It turns a concrete brief, source asset, selected board item, or starter follow-up into reviewable visual work. Discover the Creative Production MCP app and image-generation capability first. When the app or rich widgets are unavailable, use the bundled local review-page helpers and deliver files in the task workspace, clearly stating that no live board was created. When generation itself is unavailable, report the blocker; do not fabricate assets. The board steps below apply only with the discovered app.

## App-First Workflow

1. If the request lacks a real subject, business, offer, campaign, source asset, or desired output, use `intake` to mount the zero-state board. Do not use structured intake.
2. If enough context exists and no board is visible, call `creative_production_board` directly once with `action=open`. Use the host’s direct MCP invocation path that preserves resource content and widgets; a text-only wrapper must not be used for the board UI. Keep the returned `boardId` for the entire workflow.
3. Immediately before generation starts, call the same tool with `action=begin_generation` and stable placeholder IDs. After each generated file exists, call `action=complete_generation` with the matching item ID and absolute `imagePath`. Use `fail_generation` for failed outputs. Never call `open` again to refresh or continue a board.
4. Read `references/board-runtime.md` when creating, importing into, or refreshing a board.
5. Choose only the conditional references that match the request. Do not load every mode.
6. Generate through the active route. For 1 uncached native image, the coordinator uses the discovered native image-generation tool directly. For 2 or more uncached native images, use host-supported subagents if available and authorized, otherwise generate serially with the same limits. Keep at most 4 native-image worker threads open across the workflow, counting active workers and terminal workers not yet closed. Queue excess work in later waves. Consume and close each worker immediately when it reaches success, failure, cancellation, or `NEEDS_COORDINATOR_INPUT`; close terminal workers before replacements or retries. If runtime capacity is lower than expected, reduce the wave size. Validate that every returned path exists and is non-empty. Preserve successful and cached outputs. Retry only outputs that are missing or invalid, with at most 2 total attempts per output. Do not use the local `/api/images` endpoint for native generation. Do not launch another agent process to impersonate a native image tool or restore the retired process-based native generation fallback. A separately authenticated supported image API may be selected only as an explicit API route.
7. Verify each completion receipt reports the expected `boardId`, item ID, and revision. Every result identifies the same widget resource and board session so the host can update the existing mounted board; the bounded refresh watcher is recovery, not the primary delivery path. Do not render or remount another board.
8. Keep iteration, remixing, selection, and follow-up work in that same board.

## Reference Routing

Load one or more mode references only when the request needs their distinct prompt or artifact guidance:

- `references/modes/ads.md` for paid social, display, OOH, ecommerce, UGC, proof-led, or campaign ad directions.
- `references/modes/scenes.md` for product, service, venue, or offer placement in realistic contexts.
- `references/modes/offers.md` for offer-led, product-led, service-led, hero, or landing-page visual families.
- `references/modes/shots.md` for angles, crops, pans, zooms, macro details, or camera variants from an anchor image.
- `references/modes/logos.md` for new identity directions, marks, wordmarks, and lockups.
- `references/modes/styles.md` for reusable palette, typography, texture, lighting, and visual-system directions.
- `references/modes/positioning.md` for audience, occasion, proof, differentiation, and visual implication exploration.
- `references/modes/charts.md` for chart-specific visual treatment that preserves data and meaning.

Load cross-cutting contracts only when their condition applies:

- `references/review-renderer.md` when a helper produces a review manifest or local review page.
- `references/contracts/source-preservation.md` when an existing image, selected board item, product, person, packaging, logo, or chart must remain recognizable.
- `references/contracts/exact-content.md` when copy, chart values, labels, logos, claims, dimensions, or legal content must remain exact.
- `references/contracts/deterministic-exports.md` when the user asks for publish-ready, platform-specific, or final exported assets.

## Default Generation Shape

When no mode requires a different structure, generate 4-6 distinct visual directions. Each board tile must be one clean visual asset, not a collage, contact sheet, or mood board inside a mood board.

Use safe defaults for sparse but concrete requests. Do not invent claims, prices, certifications, endorsements, product facts, or readable copy.

## Handoff

When a live board is available, lead with that board and what the user should compare, select, reject, or refine next. For the declared local fallback, link the actual review page and image files without claiming they are a live board.
