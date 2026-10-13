---
name: x-openai-research-4e6a95c
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Run fast, source-grounded UX research on the highest-signal problems users are experiencing with a user-specified digital product. Use when the user asks to research user pain, UX friction, onboarding issues, docs/help problems, developer experience friction, support pain, product workflow issues, or current user complaints for a named product.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Research

Run a fresh UX research scan for the product the user specifies.

Focus on current, evidence-backed user problems. Prioritize logged-in product experience, self-serve flows, onboarding, docs/help, developer experience, support friction, and product workflows.

## Related Plugin Resources and Capability Discovery

The source plugin refers to an `index` router, `references/critical-overrides.md`, and a `user-context` skill. They are external companion resources, not files bundled in this standalone skill. Discover their installed locations through the current host's skill/plugin inventory and read relevant resources only when they actually exist; do not assume the original sibling directory layout. Report missing companion resources instead of claiming they were loaded.

Discover the host's available web search, page retrieval, and authorized internal-source connectors. Use actual discovered tool schemas or verified equivalent CLI/API access. If no source-access capability is available, work from user-supplied material and explicitly label the result as a limited evidence brief rather than a fresh scan.

## User Context

Use an installed and verified `user-context` companion when available, including its preflight only if the referenced script exists and local execution is permitted. Otherwise ground the task in the user's provided product, audience, timeframe, and references, and identify missing context in the brief.

Use saved product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, component refs, browser preferences, and share targets as grounding material when relevant.

Do not inspect every saved reference. Inspect only what the current task needs.

## Contract

- Restate the product, audience, time horizon, and research scope before scanning.
- Use public sources by default. Use internal sources when the connectors are available and the user request allows it.
- Cite sources wherever available.
- Separate observed evidence from inference.
- Do not overclaim from anecdotes.
- Do not return a dump of complaints. Tell a clear product story.
- Say clearly when source access is missing or weak.

## Workflow

1. Restate the research scope.

2. Search public sources:

- Reddit
- X/Twitter
- Hacker News
- Stack Overflow
- GitHub issues/discussions
- forums, blogs, reviews, YouTube comments, and developer communities where relevant

3. Search internal sources when available:

- Slack
- Gong
- Notion
- Google Drive/docs
- Linear/Jira/GitHub
- support or CRM notes if available

4. Cluster evidence into the highest-signal UX problems.

5. Separate:

- product UI/workflow friction
- docs/help friction
- onboarding friction
- account, billing, permissions, or setup friction
- developer/API/SDK friction
- reliability/performance issues
- feature requests

6. Rank problems by severity, frequency, confidence, and product leverage.

7. Tell a clear product story.

## Output

Default to an in-chat research brief unless the user asks for another format.

Include:

- Executive read: the core story in 5-7 sentences.
- Ranked UX problems: for each problem, include the problem, user goal, surface, what breaks, evidence, severity, frequency signal, confidence, and recommended product move.
- Source map: what was searched, what each source contributed, and where signal was weak.
- Opportunity map: group recommendations into fix this week, fix this quarter, and needs deeper research.

## Rules

- Use citations wherever available.
- Do not overclaim from anecdotes.
- Separate loud complaints from frequent problems.
- Separate UX friction from missing features.
- Separate reliability/performance issues from UX workflow issues.
- Mark internal-only evidence separately from public evidence.
- Keep the brief sharp, specific, and easy to consume.
