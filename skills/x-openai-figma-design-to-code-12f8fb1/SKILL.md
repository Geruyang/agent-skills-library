---
name: x-openai-figma-design-to-code-12f8fb1
description: '**MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool. You MUST trigger this skill whenever the user wants to implement, build, port, or code up a Figma design as code. Example prompts (not exhaustive) are ''implement this Figma design'', ''build this screen from Figma'', ''turn this Figma into code'', ''design to code''. This skill provides critical instructions and steps to the agent on how to correctly implement Figma designs in code and must NOT be skipped.'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Implement a Figma Design as Code (Design → Code)

Use this skill to turn a Figma design into code in a target codebase. This is the **read-FROM-Figma** direction: pull design context out of Figma with `get_design_context`, then adapt it into the project's real stack. For the reverse direction — building or updating a design *in* Figma from code — use [figma-generate-design](../x-openai-figma-generate-design-dc5f3d6/SKILL.md) instead.

This skill owns the **workflow** for design-to-code. Parameter mechanics (nodeId / fileKey / branchKey extraction, URL parsing, `format`/`query` options, response shape) live on the `get_design_context` tool description itself — follow them there.

**Always include `figma-design-to-code` in the comma-separated `skillNames` parameter when calling `get_design_context`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-design-to-code`).** This is a logging parameter used to track skill usage — it does not affect execution.

## Direction and Scope

- You MUST use this skill for design → code: implementing, translating, or porting a Figma node into code.
- You MUST NOT use this skill to write to Figma.

## Workflow

### 1. Call get_design_context first

- You MUST call `get_design_context` on the target node before writing any code. It is your primary tool — a single call returns reference code, a screenshot, and contextual hints.
- You MUST NOT reach for `get_metadata` or `get_screenshot` as a substitute. Use them only to orient (e.g. picking a node) or to validate, not in place of `get_design_context`.

### 2. Treat the output as a reference, not final code

- The returned code is React + Tailwind enriched with hints. You MUST treat it as a REFERENCE, not as final code to paste verbatim.
- You MUST adapt it to the target project's language, framework, component library, styling system, and conventions. Match the surrounding code.

### 3. Reuse what the project already has

- Before writing new code, You MUST check the target project for existing components, layout patterns, and design tokens that match the design intent.
- You MUST reuse the project's existing components and tokens instead of generating new equivalents from scratch.

### 4. Honor the response hints by priority

Apply the hints in this order — earlier sources override later ones:

1. **Code Connect snippets** → use the mapped codebase component directly.
2. **Component documentation links** → follow them for usage and guidelines.
3. **Design annotations** → follow any designer notes or constraints.
4. **Design tokens (CSS variables)** → map them to the project's token system.
5. **Raw hex / absolute positioning** → loosely structured; lean on the screenshot for intent.

### 5. Reproduce images and icons faithfully

Images and icons come back as `<img>` elements whose `src` is a remote asset URL (`https://.../api/mcp/asset/...`). Apply these rules as you write the code:

- **Render every icon/image from its exported asset.** Never hand-write or inline `<svg>`/`<path>`, never author your own icon file, never drop an icon or leave a placeholder — you don't have the real vector data, so anything you draw is wrong.
- **Sourcing:** the asset URL works directly as `src` for an immediate render, but it **expires in ~7 days** — so for code you'll commit, download-and-commit the exact asset bytes, or wire a dynamic content image to the project's data source (API, CDN, or props). Never a file whose contents you authored.
- **Reuse a project icon component only if its glyph clearly matches** (a name match is not enough); otherwise use the exported asset.
- **Size explicitly:** a fixed-size container (icons are usually square, e.g. `size-[24px]`, `overflow-clip`) with BOTH width and height set, and size the leaf `<img>` to fill it (`100%` or fixed px) — never `auto`, which blows the image up to its intrinsic size.

## Error Recovery

- On a `get_design_context` error, STOP and read the message before retrying.
- If the design URL has no `node-id` (a file-only URL), ask the user for a node-specific URL — You MUST NOT guess or pass an empty `nodeId`.
- On a timeout, retry against a smaller node or selection.
- You MUST NOT silently fall back to hand-writing the screen from the screenshot alone when `get_design_context` can still provide context.
