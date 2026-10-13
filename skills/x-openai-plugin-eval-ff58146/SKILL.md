---
name: x-openai-plugin-eval-ff58146
description: Help engineers evaluate a local skill or plugin, explain why it scored that way, show what to fix first, measure real token usage, benchmark starter scenarios, or decide what to run next. Use when the user says things like "evaluate this skill", "give me an analysis of the game dev skill", "why did this score that way", "what should I fix first", "measure the real token usage of this skill", or "what should I run next?".
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Plugin Eval

Use this as the beginner-friendly umbrella entrypoint for local Agent Skills and plugin evaluation. First verify the `plugin-eval` CLI is installed and inspect its supported harnesses. Static analysis can run on portable skill folders; measured token/behavior benchmarks require an actually supported and authenticated runtime. Report unsupported runtime measurements as unavailable.

## Start Here

1. Resolve whether the target path is a skill, a plugin, or another local folder.
2. Prefer the chat-first router when the user speaks naturally or is not sure which command they need:

```bash
plugin-eval start <path> --request "<user request>" --format markdown
```

3. Route natural chat requests to the matching workflow:
   - "Give me an analysis of the game dev skill." -> resolve the named skill path, run `plugin-eval analyze <path> --format markdown`, then initialize a benchmark and show the setup questions needed to tailor `benchmark.json`
   - "Evaluate this skill." -> `plugin-eval analyze <path> --format markdown`
   - "Why did this score that way?" -> `plugin-eval analyze <path> --format markdown`
   - "What should I fix first?" -> `plugin-eval analyze <path> --format markdown`
   - "Explain the token budget for this skill." -> `plugin-eval explain-budget <path> --format markdown`
   - "Measure the real token usage of this skill." -> benchmark flow, then `plugin-eval measurement-plan`
   - "Help me benchmark this plugin." -> starter benchmark flow
   - "What should I run next?" -> `plugin-eval start <path> --request "What should I run next?" --format markdown`
4. If the user wants rewrite help after evaluation, route to `../x-openai-improve-skill-f2384ee/SKILL.md`.
5. If the user wants a custom rubric, route to `../x-openai-metric-pack-designer-f374525/SKILL.md`.
6. If the user names a skill instead of giving a path, resolve it locally before running commands:
   - check the current host's registered skill directories first (for example Claude Code `.claude/skills` or TRAE `.trae/skills`; verify the actual scope and install location)
   - then check any repo-local `skills/<skill-name>` directory
   - if the name is still ambiguous, ask one short clarifying question before continuing
7. When the request sounds like "analysis" rather than just "evaluate", do the fuller path:
   - run the report
   - initialize `.plugin-eval/benchmark.json`
   - surface the setup questions that will refine the starter scenarios
   - preview the dry-run command the user can execute next

## Chat Requests To Recognize

- `Give me an analysis of the game dev skill.`
- `Evaluate this skill.`
- `Evaluate this plugin.`
- `Why did this score that way?`
- `What should I fix first?`
- `Explain the token budget for this skill.`
- `Measure the real token usage of this skill.`
- `Help me benchmark this plugin.`
- `What should I run next?`

## Matching Commands

```bash
plugin-eval start <path> --request "Evaluate this skill." --format markdown
plugin-eval start <path> --request "Give me a full analysis of this skill, including benchmark setup." --format markdown
plugin-eval analyze <path> --format markdown
plugin-eval explain-budget <path> --format markdown
plugin-eval measurement-plan <path> --format markdown
plugin-eval init-benchmark <path>
plugin-eval benchmark <path> --dry-run
plugin-eval benchmark <path>
```

## Output Expectations

- Prefer the JSON result as the source of truth.
- Lead with `At a Glance`, `Why It Matters`, `Fix First`, and `Recommended Next Step`.
- Keep the `why` content terse and easy to skim.
- Call out whether budget numbers are static estimates or measured harness results.
- Show the user the exact chat phrase they can reuse next, the `plugin-eval start` command that routes it, and the first local workflow command behind it.
- When the user asks for an analysis of a named skill, do not stop at the report if benchmark setup is still missing.
- When the user is asking about a skill specifically, hand off to `../x-openai-evaluate-skill-7c0fe3f/SKILL.md`.
- When the user is asking about a plugin bundle, hand off to `../x-openai-evaluate-plugin-72b69d9/SKILL.md`.

## References

- `../../resources/plugins-6ebaff11/plugins/plugin-eval/references/chat-first-workflows.md`
- `../../resources/plugins-6ebaff11/plugins/plugin-eval/references/technical-design.md`
- `../../resources/plugins-6ebaff11/plugins/plugin-eval/references/evaluation-result-schema.md`
