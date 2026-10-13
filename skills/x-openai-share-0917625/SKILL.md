---
name: x-openai-share-0917625
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Share a runnable prototype using the user's preferred deployment tool.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Share

Deploy the user's runnable prototype so they can share it with others.

## Critical Overrides

- Resolve the installed Product Design router (`index`) and critical-overrides reference through the host catalog or verified source package. Those upstream sibling paths are not included here. If required policy context cannot be located, report that dependency and stop deployment rather than inventing its contents.

## User Context

Resolve the installed `user-context` capability or use context explicitly provided for this task. Run its preflight only when the verified file and shell capability exist; never assume an upstream sibling path.

Use saved product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, component refs, browser preferences, and share targets as grounding material when relevant.

Do not inspect every saved reference. Inspect only what the current task needs.

## Workflow

1. Confirm the prototype directory and the user's preferred deployment target.
2. If the user invokes Product Design with @Sites, @Vercel, or another deployment tool, treat that as the selected hosting target.
3. If the user did not choose a target, ask one question:

> Where should I deploy this: @Sites, @Vercel, or another target?

4. Before using Sites for a fresh Product Design prototype, keep the existing project intact. Run `npm run build` and `npm run test:sites`; for `mobile-app`, run `npm run check:runtime` first. Confirm `dist/client/index.html`, `dist/server/index.js`, `dist/.openai/hosting.json`, and source `.openai/hosting.json` exist. Resolve Sites hosting through the current host and hand it the verified project using the actual schema; if unavailable, report Sites deployment as blocked. Do not invoke `sites-building`, run `init-site.sh`, or replace the Product Design runtime with a Vinext starter.
5. Discover the target’s authenticated deployment MCP, CLI, or API and verify project/account scope before using its actual schema.
6. If the selected tool is not available, say that clearly and ask whether to use another target.
7. Run the deployment when possible. Do not give setup instructions if you can complete the deployment directly.
8. Return the shareable URL.
9. State any misses or manual follow-up the user still needs to do.

## Rules

- Do not deploy before the user chooses or confirms the target.
- Do not claim the prototype is shared until you have a working URL.
- If the selected tool is not available, say that clearly and ask whether to use another target.
