---
name: x-openai-image-to-code-3d49e76
description: Implement a selected image, screenshot, mockup, or Image Gen reference as a faithful, responsive frontend.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Image to Code

You're tasked with translating the visual target image into a high-quality, interactive website or web app.

## Critical Overrides

- Refer to the Plugin router [x-openai-index-d69efa7](../x-openai-index-d69efa7/SKILL.md) before proceeding.
- Follow [$critical-overrides](../../resources/plugins-6ebaff11/plugins/product-design/references/critical-overrides.md).

## User Context

Before starting, load [x-openai-user-context-dea3618](../x-openai-user-context-dea3618/SKILL.md) and run its preflight script when local shell access is available.

Use saved product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, component refs, browser preferences, and share targets as grounding material when relevant.

Do not inspect every saved reference. Inspect only what the current task needs.

### Previewing prototypes in the current host

For TRAE, Claude, or another local development host, start the project’s documented dev server, use its actual returned local URL, and inspect the rendered UI plus primary interactions in an available browser. Do not assume `sites-preview` or `terminal.local` exists. If browser access is missing, record visual verification as blocked. The following instructions apply only when the actual host is ChatGPT Work Mode with that preview runtime.

### [IMPORTANT] Previewing prototypes in ChatGPT Work Mode

Starting `sites-preview` is not verification. Verification requires opening `http://terminal.local:4173/` in the cloud browser, inspecting the rendered page, testing primary interactions, checking browser console errors, and passing design QA.

Do not substitute HTTP health, build success, preview-service status, or deployment success for browser verification. If the cloud browser cannot be used, report verification as blocked.

For local prototype verification and design QA in ChatGPT Work Mode:

1. Install dependencies if needed. The project must have an npm `dev` script.
2. `sites-preview` runs `npm run dev -- --host 0.0.0.0 --port 4173 --strictPort`. The `dev` script must accept those flags.
3. For Product Design Vite starters, use `"dev": "vite"`. Configure Vite with `server.host: "0.0.0.0"` and `server.allowedHosts: ["terminal.local"]`. Preserve an existing Sites project's supported dev script; do not replace its runtime.
4. From the site root, run `sites-preview start "$PWD"`.
5. Open `http://terminal.local:4173/` in the cloud browser. Do not use `localhost`, `127.0.0.1`, `0.0.0.0`, HTTPS, or another port.
6. Verify the rendered site and its primary interactions before reporting completion.
7. Keep the local preview open for the user. Do not deploy to Sites unless the user explicitly asks to share, publish, or deploy.

## Workflow

CRITICAL: THIS IS NOT GUIDANCE. THIS IS A CHECKLIST TO COMPLETE.

1. Do not start unless you have a selected image, screenshot, mockup, or Image Gen result to recreate. A written brief is not enough.

2. Resolve the exact selected visual target before building.

    - If the user selected a numbered `x-openai-ideate-d6e955f` option, use the Nth displayed generated-image result from the most recent ideation set. Do not use the original concept planning order or Image Gen prompt submission order.
    - Use the concept-name list from `x-openai-ideate-d6e955f` only when it was explicitly written in the same displayed-image order.
    - A generated-image result ID, selected image attachment, screenshot, mockup, or Figma frame is stronger than a bare ordinal. Prefer that exact reference when available.
    - If the selected result cannot be resolved unambiguously, stop before implementation and ask the user to name the concept or reattach/select the image. Never guess and build a nearby option.

    Mobile runtime exception: 1:1 fidelity applies only to app-owned content inside the device screen. `PhoneFrame`, `StatusBar`, `HomeIndicator`, `KeyboardDock`, and the device assets are template-owned infrastructure. Preserve them even if the reference omits them, depicts different device chrome, or includes chrome in the image. Never recreate device chrome as an image asset.

3. Treat the resolved image as the design to recreate.

4. If the provided design is a mobile viewport, build a mobile app. When creating a fresh local app for that case, use [local-prototype-preflight](../../resources/plugins-6ebaff11/plugins/product-design/references/local-prototype-preflight.md) with `--template mobile-app`. If it's unclear, default to desktop.

   Before planning or implementing with the `mobile-app` template, read its `AGENTS.md` and follow its runtime and component guidance.

5. Review the reference design, catalog every image asset in the design, and use the Image Gen tool to create individual images for each one. Zoom in so you can catch every asset that needs to be generated.

    Examples include:

    - Hero images including full bleed image backgrounds
    - Featured article imagery
    - Thumbnails
    - Decorative illustrations
    - Textures and background motifs
    - Logos
    - Product images
    - Avatars

    Rules:

    - CRITICAL RULE: Do not create custom div art, CSS art, inline SVGs, handcrafted SVGs, HTML element drawings, div/span shapes, CSS drawings, gradients, emoji, or text glyphs instead of real icons and image assets ever. Use the available image-generation service for images and the closest matching icon library for icons.
    - If text is part of an image asset, keep it in the image asset. Examples include full bleed hero images, signs, posters, packaging, storefronts, article art, and illustrations where the type belongs to the visual itself. Do not crop the background image and recreate that text with transparent text boxes, HTML, CSS, or separate overlay layers unless the source clearly shows editable UI text sitting on top of the image.
    - Do not use generic placeholders where the reference implies custom visual content.
    - Generated assets must share the same art direction, palette, rendering style, and design language as the reference mockup.
    - Check the selected image tool’s actual transparency capability. Request alpha output when supported; otherwise use an authorized post-processing path and verify the final alpha channel. If generation or required editing is unavailable, report that asset step as blocked.
    - For mobile prototypes, do not catalog or generate device bezels, notches, status bars, clocks, signal or battery indicators, or home indicators. The mobile runtime owns those elements.

### Parallel asset production

After cataloging and measuring the reference assets, use up to three asset subagents when the current host exposes that capability. Otherwise perform the same asset tasks sequentially with the same boundaries and visual checks; do not invent a subagent API.

Give each subagent one raster asset task at a time with its reference crop, exact dimensions, focal point, style, output path, and consuming component. Asset subagents generate, inspect, save, and report the asset path only. They must not edit source code, run the browser, or deploy.

Prioritize critical above-the-fold assets first, then reuse agents for supporting assets. Do not delegate standard UI icons or supplied brand logos.

6. Define all sections of the page. For each section, meticulously measure the layout, spacing between elements, and the size and space of the elements themselves.

7. Find freely available fonts that match the target design.

8. Find a freely available icon library that matches the target design. Do not default to Lucide icons. Search for the best match.

    Rules:

    - CRITICAL RULE: Do not create custom inline SVGs, handcrafted SVGs, HTML element drawings, div/span shapes, CSS drawings, gradients, emoji, or text glyphs. Use the available image-generation service to generate assets and use the closest matching icon library for icons.

9. Build the app starting with [local-prototype-preflight](../../resources/plugins-6ebaff11/plugins/product-design/references/local-prototype-preflight.md). Unless the user asks for a static mock, full production behavior, or a different scope, bring the app or website to life with:

    - Working navigation, links, tabs, menus, and primary CTAs.
    - Functional inputs, filters, toggles, selections, and forms shown in the main experience.
    - Visible UI states: hover, focus, selected, open/closed, loading, empty, and success where relevant.
    - The main task, conversion path, or user journey working from start to finish when the product has one.

    Controls outside the core experience may be visual-only. Do not build auth, persistence, backend/API calls, integrations, or exhaustive edge cases unless requested.

    Rules:

    - Place every image asset you generated into its position before proceeding. I repeat, replace all placeholders, including CSS/SVG placeholders, before proceeding.
    - Do not leave controls in the core experience as static chrome. Do not create new pages or routes unless the user asks for them.

10. Run the local app.

11. Capture the local app using the Browser Choice rule in [x-openai-index-d69efa7](../x-openai-index-d69efa7/SKILL.md#browser-choice).

12. Run [design-qa](../x-openai-design-qa-e2364d6/SKILL.md) as the blocking build gate.

    Steps:

    - Open the reference image and the latest prototype screenshot before writing the QA report.
    - Compare the same viewport and the same interaction state. If they do not match, capture the missing view first.
    - Save the QA report as `design-qa.md` in the project root.
    - Fix P0/P1/P2 issues, capture the app again, and repeat until the QA report says `final result: passed`.
    - Do not keep looping on P3 polish. Include any remaining P3s as follow-up iteration notes.
    - If source capture, prototype capture, or visual comparison is blocked, stop. `design-qa.md` must say `final result: blocked`.
    - Do not hand off unless `design-qa.md` exists and says `final result: passed`.

13. Handoff the app or website.

    - Only hand off after [design-qa](../x-openai-design-qa-e2364d6/SKILL.md) passes.
    - Keep the prototype running locally.
    - Keep the local preview open for the user. In ChatGPT Work Mode, tell the user to inspect the prototype in the cloud browser; do not provide a clickable local URL. In a local host such as TRAE, Claude, or Codex Desktop, provide the verified clickable local URL when it is accessible to the user. Do not deploy to Sites unless the user explicitly asks to share, publish, or deploy.
    - After the preview handoff, use the shared build handoff from `critical-overrides.md`. Do not add a different completion message.
    - Include the post-build iteration and share nudge from [critical-overrides](../../resources/plugins-6ebaff11/plugins/product-design/references/critical-overrides.md#build-handoff).
