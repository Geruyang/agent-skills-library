---
name: x-openai-intake-9640c7f
description: Use when Creative Production is explicitly invoked or mentioned without a concrete request, when the user asks what Creative Production can do, or when the user wants help getting started without enough context to choose a workflow.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Intake

Open the Creative Production app in its zero state.

This skill owns the no-brief entry point. It does not generate images, choose a production mode, or ask structured questions.

## Workflow

1. Discover an authenticated Creative Production board interface. Use `creative_production_board` only if exposed with the schema below, or a verified MCP/API equivalent that opens the same starter-grid app and returns a persistent board identifier. If neither exists, report this workflow as blocked; do not simulate the board with a file or invent a `boardId`. Call the verified open operation exactly once with the equivalent of:

```json
{
  "action": "open",
  "title": "Creative Production",
  "summary": "Start with an idea"
}
```

   Preserve the returned `boardId`; it is the only target for later actions.
2. Let the app show its starter grid.
3. Do not ask a chat question before the app appears.
4. Do not call any structured intake tool.
5. When the user selects a starter, let the app open an editable follow-up prompt. Opening the prompt must not create a placeholder.
6. After submission, resolve the installed `produce` workflow by capability and pass the existing `boardId`. Discover matching generation lifecycle operations before use; `begin_generation` and `complete_generation` are reference operation names. Begin only when generation actually starts, then complete each generated file. If the workflow or lifecycle interface is unavailable, report the blocked handoff. Never reopen that board.

## Exit

Stop after the zero-state app is visible. The next user turn or starter follow-up owns the concrete creative request and updates this same board.
