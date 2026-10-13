---
name: x-openai-evaluate-skill-7c0fe3f
description: Evaluate a local agent skill in engineer-friendly terms. Use when the user says "evaluate this skill", "give me an analysis of the game dev skill", "audit this skill", "why did this score that way", "what should I fix first", or asks for a skill-specific report before benchmarking it.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Evaluate Skill

Use this skill when the target is a local skill directory or `SKILL.md` file.

## Workflow

1. Treat "Evaluate this skill." as the default entrypoint.
2. If the user names a skill instead of giving a path, resolve it through the current host's installed skill catalog first, then its configured user/project skill directories and repo-local `skills/<skill-name>`. Use the actual loaded path, not a hard-coded client home directory.
3. If the user says the request in natural language first, use `plugin-eval start <skill-path> --request "<user request>" --format markdown` to show the routed path clearly.
4. Run `plugin-eval analyze <skill-path> --format markdown`.
5. Review `At a Glance`, `Why It Matters`, `Fix First`, and `Recommended Next Step` before drilling into details.
6. Explain which findings are structural, which are budget-related, and which are code-related.
7. If the user asks for an "analysis" of the skill, do not stop at the report. Also run `plugin-eval init-benchmark <skill-path>` and show the setup questions for refining the starter scenarios in `.plugin-eval/benchmark.json`.
8. If the user wants real usage numbers, switch to "Measure the real token usage of this skill." and run the benchmark flow.
9. After observed usage is available, use `plugin-eval measurement-plan <skill-path> --observed-usage <usage.jsonl> --format markdown` to recommend what to instrument or improve next.
10. If the user wants a rewrite plan, route to `../x-openai-improve-skill-f2384ee/SKILL.md`.

## Skill-Specific Priorities

- frontmatter validity
- `name` and `description` quality
- progressive disclosure and reference usage
- broken relative links
- oversized `SKILL.md` or descriptions
- helper script quality for TypeScript and Python files

## Chat Requests To Recognize

- `Evaluate this skill.`
- `Give me an analysis of the game dev skill.`
- `Audit this skill.`
- `Why did this skill score that way?`
- `What should I fix first?`
- `Measure the real token usage of this skill.`

## Commands

```bash
plugin-eval start <skill-path> --request "Evaluate this skill." --format markdown
plugin-eval analyze <skill-path> --format markdown
plugin-eval explain-budget <skill-path> --format markdown
plugin-eval measurement-plan <skill-path> --format markdown
plugin-eval init-benchmark <skill-path>
plugin-eval benchmark <skill-path> --dry-run
```

## Reference

- `../../resources/plugins-6ebaff11/plugins/plugin-eval/references/chat-first-workflows.md`
