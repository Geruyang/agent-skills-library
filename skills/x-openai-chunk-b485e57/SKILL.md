---
name: x-openai-chunk-b485e57
description: Use CircleCI Chunk for AI-assisted CI/CD work through either the Chunk web UI or the chunk-cli. Trigger this skill when users ask to set up Chunk, troubleshoot or fix failing builds with Chunk, configure Chunk environments, schedule/proactively run Chunk tasks, or use chunk-cli commands such as init, validate, build-prompt, auth, sandbox, task, and skill install.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Chunk

## Overview

Use this skill to choose the best Chunk workflow (UI or CLI), then execute it with clear prechecks and safe defaults. Keep responses action-oriented and grounded in verified commands and setup requirements.

## Workflow

1. Classify the request path.
- Use UI path for org setup, model-provider onboarding, fix buttons, or environment selection in the CircleCI app.
- Use CLI path for terminal-based project setup, validation hooks, prompt/context generation, sandbox operations, or scripted task execution.
- Use mixed path when users want UI setup plus CLI execution in the same flow.
2. Gather minimum context.
- Confirm repository/project, branch, and whether GitHub integration is in place.
- Confirm whether the user is using CircleCI-managed model provider or bring-your-own keys.
- For CLI operations, confirm local OS compatibility and required tokens/auth.
3. Execute using the matching reference.
- For UI/setup flows, load [chunk-ui.md](references/chunk-ui.md).
- For CLI flows, load [chunk-cli.md](references/chunk-cli.md).
4. Close with verification.
- State what was configured or run, what remains blocked, and the next safest command or UI action.

## Guardrails

- Treat Chunk features as beta unless the user confirms otherwise.
- Never expose or log secret values (API keys, tokens, bearer credentials).
- Do not invent `chunk` subcommands or flags; stick to documented command families.
- If sandbox features are requested, call out private preview status and any access gate.
- If a task depends on org-level prerequisites (GitHub App install, org toggles, contexts), verify those first.

## Reference Map

- [chunk-ui.md](references/chunk-ui.md): CircleCI app setup, provider onboarding, fix buttons, environment file/setup, and operational troubleshooting.
- [chunk-cli.md](references/chunk-cli.md): Installation, command map, quick-start flows, auth/env variables, and platform constraints.

## Output Contract

Provide:

1. Path chosen (UI, CLI, or mixed) and why.
2. Steps executed with exact command/UI actions.
3. Required prerequisites not yet met.
4. Concrete next action to finish the user’s goal.
