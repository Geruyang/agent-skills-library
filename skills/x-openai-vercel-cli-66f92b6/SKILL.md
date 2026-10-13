---
name: x-openai-vercel-cli-66f92b6
description: Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, querying metrics, managing domains, or interacting with the Vercel platform from the command line.
metadata:
  priority: '4'
  docs: '[''https://vercel.com/docs/cli'']'
  sitemap: https://vercel.com/sitemap/docs.xml
  pathPatterns: '[''vercel.json'', ''vercel.ts'', ''.vercel/**'', ''.vercelignore'', ''now.json'']'
  bashPatterns: '[''^\\s*vercel(?:\\s|$)'', ''^\\s*vc(?:\\s|$)'', ''\\bnpx\\s+vercel\\b'', ''\\bpnpm\\s+dlx\\s+vercel\\b'', ''\\bbunx\\s+vercel\\b'', ''\\byarn\\s+dlx\\s+vercel\\b'', ''\\bnpx\\s+@vercel/config\\b'']'
  promptSignals: '{''phrases'': [''check deployment'', ''check deploy'', ''deployment status'', ''deploy status'', ''vercel logs'', ''vercel metrics'', ''deployment logs'', ''deploy logs'', ''vercel inspect'', ''is it deployed'', ''deploy failing'', ''deploy failed'', ''deployment error'', ''check vercel'', ''vercel status''], ''allOf'': [[''check'', ''deployment''], [''check'', ''deploy''], [''vercel'', ''status''], [''vercel'', ''logs''], [''vercel'', ''metrics''], [''deploy'', ''error''], [''deploy'', ''failed''], [''deploy'', ''stuck'']], ''anyOf'': [''deployment'', ''deploy'', ''vercel'', ''production''], ''noneOf'': [''terraform'', ''aws deploy'', ''heroku''], ''minScore'': 6}'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Vercel CLI Skill

The Vercel CLI (`vercel` or `vc`) deploys, manages, and develops projects on the Vercel platform from the command line. Use `vercel <command> -h` for full flag details on any command.

## Critical: Project Linking

Commands must be run from the directory containing the `.vercel` folder (or a subdirectory of it). How `.vercel` gets set up depends on your project structure:

- **`.vercel/project.json`**: Created by `vercel link`. Links a single project. Fine for single-project repos, and can work in monorepos if there's only one project.
- **`.vercel/repo.json`**: Created by `vercel link --repo`. Links a repo that may contain multiple projects. Always a good idea when any project has a non-root directory (e.g., `apps/web`).

Running from a project subdirectory (e.g., `apps/web/`) skips the "which project?" prompt since it's unambiguous.

**When something goes wrong, check how things are linked first** — look at what's in `.vercel/` and whether it's `project.json` or `repo.json`. Also verify you're on the right team with `vercel whoami` — linking while on the wrong team is a common mistake.

## Quick Start

```bash
npm i -g vercel
vercel login
vercel link              # single project
# OR
vercel link --repo       # monorepo
vercel pull
vercel dev        # local development
vercel deploy     # preview deployment
vercel --prod     # production deployment
```

## Decision Tree

Use this to route to the correct reference file:

- **Deploy** → `references/deployment.md`
- **Local development** → `references/local-development.md`
- **Environment variables** → `references/environment-variables.md`
- **CI/CD automation** → `references/ci-automation.md`
- **Domains or DNS** → `references/domains-and-dns.md`
- **Projects or teams** → `references/projects-and-teams.md`
- **Logs, metrics, debugging, or accessing preview deploys** → `references/monitoring-and-debugging.md`
- **Blob storage** → `references/storage.md`
- **Integrations (databases, storage, etc.)** → `references/integrations.md`
- **Access a preview deployment** → use `vercel curl` (see `references/monitoring-and-debugging.md`)
- **CLI doesn't have a command for it** → use `vercel api` as a fallback (see `references/advanced.md`)
- **Node.js backends (Express, Hono, etc.)** → `references/node-backends.md`
- **Monorepos (Turborepo, Nx, workspaces)** → `references/monorepos.md`
- **Bun runtime** → `references/bun.md`
- **Feature flags** → `references/flags.md`
- **Advanced (API, webhooks)** → `references/advanced.md`
- **Global flags** → `references/global-options.md`
- **First-time setup** → `references/getting-started.md`

## Anti-Patterns

- **Wrong link type in monorepos with multiple projects**: `vercel link` creates `project.json`, which only tracks one project. Use `vercel link --repo` instead. When things break, check `.vercel/` first.
- **Letting commands auto-link in monorepos**: Many commands implicitly run `vercel link` if `.vercel/` doesn't exist. This creates `project.json`, which may be wrong. Run `vercel link` (or `--repo`) explicitly first.
- **Linking while on the wrong team**: Use `vercel whoami` to check, `vercel teams switch` to change.
- **Forgetting `--yes` in CI**: Required to skip interactive prompts.
- **Using `vercel deploy` after `vercel build` without `--prebuilt`**: The build output is ignored.
- **Hardcoding tokens in flags**: Use `VERCEL_TOKEN` env var instead of `--token`.
- **Disabling deployment protection**: Use `vercel curl` instead to access preview deploys.

## Related Skills in This Plugin

- **Log drains and observability vendor setup** → `⤳ skill: observability`
- **Feature flag configuration and adapter patterns** → `⤳ skill: vercel-flags`
