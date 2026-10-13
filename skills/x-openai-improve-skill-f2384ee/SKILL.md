---
name: x-openai-improve-skill-f2384ee
description: Turn plugin-eval findings into a concrete rewrite brief for an Agent Skill. Use when the user already evaluated a skill and now wants the assistant to improve it, especially after asking what to fix first.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Improve Skill

Use this skill after `plugin-eval` has already produced findings for a local skill.

## Workflow

1. Run `plugin-eval analyze <skill-path> --brief-out <brief.json>`.
2. Read the improvement brief and group work into required fixes versus recommended fixes.
3. Locate the installed `skill-creator` skill through the current host's skill catalog and read its guidance. Do not assume another user's home path. If it cannot be found, report the missing dependency before relying on its workflow.
4. Re-run the evaluation and compare before and after outputs.

## Chat Requests To Recognize

- `Improve this skill based on the evaluation.`
- `Rewrite this skill using the plugin-eval findings.`
- `What should I fix first in this skill?`

## Focus Areas

- reduce trigger and invoke token costs
- keep `SKILL.md` compact
- move bulky details into references or scripts
- improve trigger descriptions
- fix broken links and manifest/frontmatter issues

## Commands

```bash
plugin-eval analyze <skill-path> --brief-out ./skill-brief.json
plugin-eval compare before.json after.json
```

## Reference

- `../../resources/plugins-6ebaff11/plugins/plugin-eval/references/chat-first-workflows.md`
