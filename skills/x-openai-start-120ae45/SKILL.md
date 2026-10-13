---
name: x-openai-start-120ae45
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Use when starting Zoom work.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Start

Use this as the default entry skill for the plugin.

## What This Skill Does

- Classifies the request by job-to-be-done, not by product name alone
- Routes into the right implementation skill
- Pulls in product-specific Zoom references only after the route is clear
- Prevents common early mistakes, especially Meeting SDK vs Video SDK and REST API vs SDK confusion

## Routing Table

| If the user wants to... | Route to |
|---|---|
| Choose the right Zoom surface for a new project | [plan-zoom-product](../x-openai-plan-zoom-product-3b4e508/SKILL.md) |
| Set up OAuth, tokens, scopes, or app credentials | [setup-zoom-oauth](../x-openai-setup-zoom-oauth-442899b/SKILL.md) |
| Embed or customize a Zoom meeting flow | [build-zoom-meeting-app](../x-openai-build-zoom-meeting-app-c3f8e89/SKILL.md) |
| Build a bot, recorder, or real-time meeting processor | [build-zoom-bot](../x-openai-build-zoom-bot-0582b85/SKILL.md) |
| Debug a broken integration | [debug-zoom](../x-openai-debug-zoom-2565b25/SKILL.md) |

## Supporting Zoom References

Use these only after selecting the workflow:

- [general](../x-openai-zoom-general-37cf44c/SKILL.md)
- [rest-api](../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
- [meeting-sdk](../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)
- [video-sdk](../x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md)
- [webhooks](../x-openai-setup-zoom-webhooks-e8837c7/SKILL.md)
- [websockets](../x-openai-setup-zoom-websockets-c8c09ef/SKILL.md)
- [oauth](../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Operating Rules

1. Prefer one clear recommendation over a product catalog dump.
2. Ask a short clarifier only when the route is genuinely ambiguous.
3. Keep the first response architectural and actionable, then go deep.
4. Pull in deeper references only when they directly help the current decision or implementation.
