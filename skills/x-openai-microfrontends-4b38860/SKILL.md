---
name: x-openai-microfrontends-4b38860
description: Guide for building, configuring, and deploying microfrontends on Vercel. Use this skill when the user mentions microfrontends, multi-zones, splitting an app across teams, independent deployments, cross-app routing, incremental migration, composing multiple frontends under one domain, microfrontends.json, @vercel/microfrontends, the microfrontends local proxy, or path-based routing between Vercel projects. Also use when the user asks about shared layouts across projects, navigation between microfrontends, fallback environments, asset prefixes, or feature flag controlled routing.
metadata:
  priority: '7'
  docs: '[''https://vercel.com/docs/microfrontends'']'
  pathPatterns: '[''microfrontends.json'', ''microfrontends.jsonc'', ''apps/*/microfrontends.json'', ''apps/*/microfrontends.jsonc'']'
  bashPatterns: '[''\\bvercel\\s+microfrontends\\b'', ''\\bvercel\\s+mf\\b'', ''\\bnpm\\s+(install|i|add)\\s+[^\\n]*@vercel/microfrontends\\b'', ''\\bpnpm\\s+(install|i|add)\\s+[^\\n]*@vercel/microfrontends\\b'', ''\\bbun\\s+(install|i|add)\\s+[^\\n]*@vercel/microfrontends\\b'', ''\\byarn\\s+add\\s+[^\\n]*@vercel/microfrontends\\b'']'
  importPatterns: '[''@vercel/microfrontends'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Vercel Microfrontends
Split a large application into independently deployable units that render as one cohesive app. Vercel handles routing on its global network using `microfrontends.json`.

**Core concepts:** default app (has `microfrontends.json`, serves unmatched requests) · child apps (have `routing` path patterns) · asset prefix (prevents static-asset collisions) · independent deployments.

**Frameworks:** Next.js (App Router + Pages Router), SvelteKit, React Router, Vite — all via `@vercel/microfrontends`.

**CLI (`vercel microfrontends` / `vercel mf`):**
- `create-group` — create a new group; interactive by default, or fully non-interactive with `--non-interactive` (options: `--name`, `--project` (repeatable), `--default-app`, `--default-route`, `--project-default-route` (repeatable, format: `<project>=<route>`, required for each non-default project in non-interactive mode), `--yes` to skip confirmation prompt); note: `--non-interactive` is blocked if adding the projects would exceed the free tier limit — the user must confirm billing changes interactively
- `add-to-group` — add the current project to an existing group; requires interactive terminal (options: `--group`, `--default-route`)
- `remove-from-group` — remove the current project from its group; requires interactive terminal (option: `--yes` skips project-link prompt only)
- `delete-group` — delete a group and all its settings, irreversible; requires interactive terminal (option: `--group` to pre-select group)
- `inspect-group` — retrieve group metadata (project names, frameworks, git repos, root dirs); useful for automating setup (options: `--group`, `--format=json`, `--config-file-name`)
- `pull` — pull remote `microfrontends.json` for local development (option: `--dpl`)
- `microfrontends proxy` — local dev proxy · `microfrontends port` — print auto-assigned port

## Finding Detailed Information

This skill includes detailed reference docs in the `references/` directory. **Do not read all references upfront.** Instead, search or grep the relevant file when the user asks about a specific topic:

| Topic | Reference file |
|---|---|
| Getting started, quickstart, framework setup, `microfrontends.json` schema, fields, naming, examples | `references/configuration.md` |
| Path expressions, asset prefixes, flag-controlled routing, middleware | `references/path-routing.md` |
| Local proxy setup, polyrepo config, Turborepo, ports, deployment protection | `references/local-development.md` |
| Inspecting groups (`inspect-group`), adding/removing projects, fallback environments, navigation, observability | `references/managing-microfrontends.md` |
| Testing utilities (`validateMiddlewareConfig`, `validateRouting`, etc.), debug headers, common issues | `references/troubleshooting.md` |
| Deployment protection, Vercel Firewall, WAF rules for microfrontends | `references/security.md` |

When the user asks about a specific topic, use grep or search over the relevant reference file to find the answer without loading all references into context.
