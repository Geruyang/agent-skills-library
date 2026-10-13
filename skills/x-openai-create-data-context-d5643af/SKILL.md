---
name: x-openai-create-data-context-d5643af
description: Create, update, inspect, or repair Data Analytics semantic layers. Use when the user asks to save data context or create a semantic layer that future Data Analytics work can inspect and cite.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Create Data Context

This skill creates and maintains semantic-layer skills for Data Analytics. A semantic-layer skill is an explicit artifact the user can inspect and cite later. It captures how future analyses should interpret the data, for example which metric definition is canonical, which dashboard or table is the best source of truth, and what caveats should be checked before answering.

Data-task routing is owned by the Data Analytics `index` skill. If the user wants Data Analytics to do work with data now, route to `index`, whether the work starts from connected sources, uploaded files, pasted tables, sample data, or an existing semantic layer. Examples include answering a metric question, building a report, or checking a dataset.

Use this skill only when the user asks to save data context or create, update, inspect, or repair a semantic layer.

## Runtime Routing

Inspect the current host's actual skill-installation, filesystem, and intake capabilities to choose intake and persistence; do not assume product-specific `surface` or `mode` fields exist. Build and validate the same canonical semantic-layer skill package before writing it to any destination.

For intake:

- Use structured intake when a supported form action is available.
- Use conversational intake for open-ended details and for runtimes without a supported form action.

Choose one persistence destination by default:

| Destination branch | Select this branch when | Action |
| --- | --- | --- |
| ChatGPT personal Skills | `surface = chatgpt_web` and the run exposes a product-backed personal Skills install surface, such as a native skill draft/upload/install action or an installable skill package preview. | Install the generated skill into the user's personal Skills library. Capture the installed skill link or Skills-library reference returned by the install surface and include it as a Markdown link in the chat response. Verify through the available Skills-library, list, or fresh-thread discovery surface when the runtime exposes one. |
| Local Agent Skills host | The user asks for local persistence and the current host has a verified writable skill directory. | Write the canonical package to the user-selected skill root, using the host's documented project or user scope. Discover that path rather than assuming a home directory. Validate the written skill and verify discovery in a fresh host context when possible. If installation is unavailable, deliver the package in the current project and state that it is not installed. |
| Portable package | The current run has no supported persistent skill destination. | Return a portable skill package or source plan and clearly state that it has not been installed persistently, including the exact persistence blocker. |

When the user requests multiple supported destinations, install the same canonical package in each authorized destination and verify each independently.

For ordinary data work, return to the Data Analytics `index` workflow.

## Skill Configuration

### Audience And Language

Write for Data Analytics users, not plugin maintainers. Explain what context would improve the current or future analysis in practical terms. Avoid implementation terms such as raw state paths, connector ids, cache, runtime, metadata, or preflight unless the user asks for debugging details.

### Source Links

When referencing sources inline, prefer clickable Markdown links over plain labels whenever a useful URL exists. Use the source title, record name, channel/thread, or meeting/date as the link text. Use plain labels only when no useful link is available.

## Semantic Layer Setup

Use this flow when the user wants to create or maintain a semantic layer. If they are not ready to create the layer yet, use the same flow to produce a short source plan for what the semantic layer needs.

The output is a visible skill or plan. Build the semantic-layer skill when enough source-backed detail exists to make it useful. When the available detail is still thin, return a practical plan that explains what source to collect next and why.

## Creating Or Updating The Layer

Create one semantic layer per coherent product, business, metric, source, or reporting area unless the user explicitly asks for a broader shared layer. Infer the area from the provided context when it is clear; ask only when the answer changes the crawl, destination, or resulting skill.

Choose the destination from `Runtime Routing` using the supported persistence mechanism exposed in the current run. For local creations, use the verified host skill root and `<area>-semantic-layer` directory, or a user-selected project delivery directory when persistent installation is unavailable. Ask before placing a generated semantic-layer skill inside a plugin.

Before crawling, build a data-source list that explains what was checked, what is missing, and which sources are lower-confidence. For direct creation or draft-file work, write it to `references/source-inventory.md`; for planning-only work, return it in chat.

Use source-backed evidence. Favor durable sources such as transformation code, tests, maintained metric docs, and verified dashboards over looser signals such as query history or team discussion. If sources disagree, keep the conflict visible instead of choosing silently.

Keep generated semantic-layer skills compact. Put detailed metric definitions, tables, query patterns, caveats, and evidence into linked references using `references/semantic-layer/skill-template.md`. Preserve provenance and avoid copying raw sensitive data, credentials, row-level examples, or long private messages into generated files.

After creating or updating a semantic-layer skill, read `references/semantic-layer/weekly-polling-automation.md` and always offer weekly refresh when the layer has a stable target path and usable `references/source-inventory.md`. Weekly refresh is optional: do not create it without explicit user approval unless the user directly asked for recurring refresh. If the offer cannot be made, state the missing prerequisite.

Return the created or updated path or installed skill link, source coverage, any user-relevant caveats or blockers, future-use guidance, iteration guidance, and the weekly refresh automation offer or prerequisite blocker so the user can cite the semantic layer directly in later prompts. Tell the user they can ask to refine definitions, add sources, update caveats, or adjust the semantic layer as their understanding changes. For ChatGPT personal Skills creations, include the installed skill link in the response.

Keep routine validation details in support artifacts unless a check failed, was unavailable, or changes how the user should rely on the semantic layer.

## Output Contract

For semantic-layer work, report what was created, updated, inspected, or repaired; source coverage; any user-relevant caveats or blockers; and the exact path or installed skill link the user can cite later. For create or update results, include the weekly refresh automation offer or the missing prerequisite that prevented the offer, and let the user know they can iterate on the semantic layer. Keep routine validation details in support artifacts. If the request is ordinary data work, say that it should be routed through `index`.
