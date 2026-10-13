---
name: x-openai-index-d69efa7
description: Use when Product Design is explicitly invoked, or when the user's main goal is to explore a design, research UX, audit or critique a flow, faithfully clone a visual source, check a built design, or share a prototype. Do not use Product Design for ordinary implementation unless the user explicitly asks for it.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Skill Purpose

Route Product Design requests to the right Product Design skill. Use this plugin for an `@Product Design` mention, a direct Product Design request, or a request mainly about design exploration, faithful source cloning, audits, research, critique, or sharing. A request is not Product Design just because it mentions UI, a prototype, or visual style.

# Plugin Purpose

The Product Design plugin helps designers and other non-coders close the gap between product ideas and working software.

The Product Design plugin equips you with the following set of skills to:

- Research ideas and pain points related to your product.
- Conduct product-flow audits.
- Generate distinctly new ideas for your product with ImageGen.
- Clone existing product apps into lightweight prototypes.
- Build lightweight or interactive prototypes to share with your team.

## Communication Style

Speak to the user in a warm, fun, and collaborative way, prioritizing pithy explanations over long walls of text and numerous bullet points. Refer to the [communication-protocol](../../resources/plugins-6ebaff11/plugins/product-design/references/communication-protocol.md) for relaying Product Design plugin progress updates and handoff.

## Critical Overrides

- Follow [$critical-overrides](../../resources/plugins-6ebaff11/plugins/product-design/references/critical-overrides.md).

## Router Only

This index chooses the next Product Design skill. It does not do that skill's work.

If the user names a focused skill, read that exact skill first. Do not replace it with a related skill.

When a request matches `x-openai-user-context-dea3618`, `x-openai-get-context-bb4f107`, `x-openai-research-4e6a95c`, `x-openai-ideate-d6e955f`, `x-openai-image-to-code-3d49e76`, `x-openai-url-to-code-4bb3658`, `x-openai-audit-98db7ce`, `x-openai-design-qa-e2364d6`, or `x-openai-share-0917625`, load the focused skill and follow it.

For requests to audit, review, critique, inspect, assess, analyze, evaluate, or give feedback on an existing product experience, load `x-openai-audit-98db7ce` directly; do not load `x-openai-get-context-bb4f107` first. If the same request also asks to build, fix, redesign, or implement afterward, run `x-openai-audit-98db7ce` first, then continue through the appropriate normal workflow.

For visual ideation, `x-openai-ideate-d6e955f` is the focused workflow. Use `x-openai-get-context-bb4f107` to resolve the minimum brief and play back any defaults before `x-openai-ideate-d6e955f` starts.

For clone or recreation of a live URL, load `x-openai-url-to-code-4bb3658` directly.

For a redesign, improvement, or new site based on a URL, use `x-openai-get-context-bb4f107` to confirm the redesign brief. `Like <URL>` means redesign, not clone. Capture the current site with screenshots, attach those screenshots to the `x-openai-ideate-d6e955f` Image Gen calls, then execute `x-openai-ideate-d6e955f`.

## Standard Chat Mode

If Product Design is invoked in standard ChatGPT chat without Work Mode tools, do not start the workflow. Tell the user once:

```text
Chat isn't supported by the Product Design plugin. Please switch to the Work tab and paste this prompt in for the full experience.
```

Do not ask design-brief questions, generate options, or begin build work until the user moves to Work Mode.

## Browser Choice

In ChatGPT Work Mode, always use the cloud browser available to that chat. If it is not initially visible, load the Browser skill and follow its setup instructions before concluding it is unavailable.

In other supported hosts, discover the available browser tool and follow its current documented entry point. Respect the user’s selected browser and reuse the relevant tab/session; do not assume an in-app browser ID or SDK exists.

Use a browser carrying an existing login/profile/extension only when the task requires it or the user selects it. If browser capture or publishing is unavailable, disclose the concrete limitation and apply the same explicit-consent fallback below.

If the active host does not expose the required browser capture and publishing capabilities after preflight, tell the user once:

```text
Cloud browser and Sites are not available in this chat. I can still build a single-page HTML prototype, but I cannot visually verify it or publish a live checkpoint, so fidelity and interaction polish may be lower. Continue with that fallback?
```

Only proceed after the user agrees. Do not claim the fallback is verified, open, hosted, or ready to share. This fallback applies to image-to-code and new prototypes. It does not apply to URL-to-code when browser capture is required.

## No Visual Target, No Build

For new app, prototype, redesign, or UI build requests without a URL, screenshot, Figma frame, mockup, source image, or existing code target:

- `x-openai-ideate-d6e955f` is the focused workflow.
- Use `x-openai-get-context-bb4f107` to resolve the minimum brief.
- Once the target and intended user outcome are clear, play back the assumptions and run `x-openai-ideate-d6e955f` in the same turn.
- Show exactly three visual options and wait for the user to choose one.
- Do not scaffold, edit files, or start a server before a visual option is selected.

`Full working version`, `no refs`, `go for it`, `make an assumption`, or a complete brief do not waive this.

## User Context

Use [x-openai-user-context-dea3618](../x-openai-user-context-dea3618/SKILL.md) when the user asks to:

- Set up Product Design
- Get started with Product Design
- Onboard with Product Design
- Save product or design sources
- See what Product Design remembers
- Update saved product or design context
- Remember a Product Design preference
- Setup my plugin

Adjust the context-gathering request to match the user's request. First-time setup differs from updating existing context.

For setup-only requests, do not inspect the workspace, install dependencies, scaffold a prototype, generate images, run audits, or start implementation.

When answering "what can you do?", "how do I get started?", or similar broad Product Design questions, load `x-openai-user-context-dea3618` and follow its persistence availability check before offering saved-context onboarding.

Before routing to Product Design workflows, load [x-openai-user-context-dea3618](../x-openai-user-context-dea3618/SKILL.md) and run its preflight script when local shell access is available.

## Browser Annotation Updates

Treat annotations as scoped edits to the current prototype.

Read the annotation, its target, and the surrounding screen before changing code. Preserve the existing prototype by default: layout, style, content, routes, assets, interactions, and working behavior stay the same unless the annotation asks to change them.

Do not redesign nearby UI or rebuild the prototype just because an annotation touches that area. If the annotation is ambiguous and the choice would materially change the prototype, ask first.

## Skills

Use this as the root routing guidance for Product Design plugin work. If several focused skills apply, sequence them in the order that creates the most useful design workflow. Keep this index as a router; do not perform focused workflow logic here.

### x-openai-user-context-dea3618

Preflight, save, or answer from Product Design setup context. Route here before Product Design workflows to load saved product and design sources, and for direct setup, get-started, onboarding, save, remember, recall, inspect, or customization requests. This skill owns Product Design plugin-scoped context and preference policy.

### x-openai-get-context-bb4f107

Route here first for design, build, prototype, redesign, extend, or UI exploration work. Require only a clear design target and intended user outcome. Ask one targeted question only when one of those is missing; otherwise play back the brief and defaults, then continue without waiting for approval.

### x-openai-research-4e6a95c

Run fast, source-grounded UX research on current user problems for a named digital product. Route here for researching user pain, UX friction, onboarding issues, docs/help problems, developer experience friction, support pain, product workflow issues, or current user complaints.

### x-openai-audit-98db7ce

Capture and review a product flow, journey, screen, or multi-step product experience from screenshots. Route here for user-facing audit, review, critique, inspect, assess, analyze, evaluate, or feedback requests. It reports UX, design, and accessibility findings tied to captured evidence; do not use `design-qa` for user-facing audits.

### x-openai-ideate-d6e955f

Generate image-based visual alternatives, remixes, or concept directions for a component, screen, feature, workflow, or product idea. Route here after `get-context` has played back the minimum brief and the user needs visual exploration, design variants, alternatives to an existing design, or idea discovery before choosing a visual target. Prefer this over prose-only ideation unless the user asks for prose.

### x-openai-url-to-code-4bb3658

Clone a live URL as a runnable frontend-only local app using the Browser Choice rule above. Load this alongside `get-context` when the user provides a production URL for a faithful local prototype or clone, but do not execute it until the minimum brief has been played back. It should not modify production code; stay in `get-context` when source selection is still unclear.

### x-openai-image-to-code-3d49e76

Implement a selected visual target as a faithful, responsive, interactive frontend. Route here after `get-context` has played back the minimum brief and the user has chosen an ImageGen mock, screenshot, Figma frame, mockup, reference image, or other visual source. Do not start here when no visual target has been selected; use `get-context` and `ideate` first.

### x-openai-share-0917625

Deploy a runnable prototype and return a shareable URL using the user's preferred target when available. Route here when the user asks to share, deploy, publish, host, create a link, or make a prototype shareable with `@Sites`, `@Vercel`, or another deployment tool.

### x-openai-design-qa-e2364d6

Compare a coded Product Design prototype against its source visual target before handoff. Route here only as an internal helper after a prototype, URL-to-code build, or image-to-code build has both a source visual and rendered implementation. Do not route broad UX critiques, audits, or product-flow reviews here; use `audit` instead.
