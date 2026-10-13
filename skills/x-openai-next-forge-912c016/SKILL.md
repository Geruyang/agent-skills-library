---
name: x-openai-next-forge-912c016
description: next-forge expert guidance — production-grade Turborepo monorepo SaaS starter by Vercel. Use when working in a next-forge project, scaffolding with `npx next-forge init`, or editing @repo/* workspace packages.
metadata:
  priority: '6'
  docs: '[''https://next-forge.com/docs'', ''https://github.com/haydenbleasel/next-forge'']'
  pathPatterns: '[''pnpm-workspace.yaml'', ''apps/app/**'', ''apps/web/**'', ''apps/api/**'', ''apps/email/**'', ''apps/docs/**'', ''apps/studio/**'', ''apps/storybook/**'', ''packages/auth/**'', ''packages/database/**'', ''packages/design-system/**'', ''packages/payments/**'', ''packages/email/**'', ''packages/analytics/**'', ''packages/observability/**'', ''packages/security/**'', ''packages/ai/**'', ''packages/cms/**'', ''packages/collaboration/**'', ''packages/feature-flags/**'', ''packages/internationalization/**'', ''packages/notifications/**'', ''packages/rate-limit/**'', ''packages/seo/**'', ''packages/storage/**'', ''packages/webhooks/**'', ''packages/next-config/**'', ''packages/typescript-config/**'', ''**/keys.ts'', ''**/env.ts'', ''**/proxy.ts'', ''biome.jsonc'']'
  bashPatterns: '[''\\bnext-forge\\b'', ''\\bnpx\\s+next-forge\\b'', ''\\bpnpm\\s+migrate\\b'', ''\\bpnpm\\s+bump-deps\\b'', ''\\bpnpm\\s+bump-ui\\b'', ''\\bprisma\\s+(generate|db\\s+push|format|studio)\\b'', ''\\bstripe\\s+listen\\b'', ''\\bnpx\\s+shadcn@latest\\s+add\\b.*-c\\s+packages/design-system\\b'']'
  importPatterns: '[''@repo/auth'', ''@repo/database'', ''@repo/design-system'', ''@repo/payments'', ''@repo/email'', ''@repo/analytics'', ''@repo/observability'', ''@repo/security'', ''@repo/ai'', ''@repo/cms'', ''@repo/collaboration'', ''@repo/feature-flags'', ''@repo/internationalization'', ''@repo/notifications'', ''@repo/rate-limit'', ''@repo/seo'', ''@repo/storage'', ''@repo/webhooks'', ''@repo/next-config'', ''@t3-oss/env-nextjs'', ''@rescale/nemo'']'
  promptSignals: '{''phrases'': [''next-forge'', ''next forge'', ''@repo/''], ''allOf'': [[''monorepo'', ''saas'', ''starter''], [''turborepo'', ''clerk'', ''stripe'']], ''anyOf'': [''saas starter'', ''production monorepo'', ''keys.ts'', ''pnpm-workspace''], ''noneOf'': [''create-t3-app''], ''minScore'': 6}'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# next-forge

next-forge is a production-grade Turborepo template for building Next.js SaaS applications. It provides a monorepo structure with multiple apps, shared packages, and integrations for authentication, database, payments, email, CMS, analytics, observability, security, and more.

## Quick Start

Initialize a new project:

```bash
npx next-forge@latest init
```

The CLI prompts for a project name and package manager (bun, npm, yarn, or pnpm). After installation:

1. Set the `DATABASE_URL` in `packages/database/.env` pointing to a PostgreSQL database (Neon recommended).
2. Run database migrations: `bun run migrate`
3. Add any optional integration keys to the appropriate `.env.local` files.
4. Start development: `bun run dev`

All integrations besides the database are optional. Missing environment variables gracefully disable features rather than causing errors.

## Architecture Overview

The monorepo contains apps and packages. Apps are deployable applications. Packages are shared libraries imported as `@repo/<package-name>`.

**Apps** (in `/apps/`):

| App | Port | Purpose |
|-----|------|---------|
| `app` | 3000 | Main authenticated SaaS application |
| `web` | 3001 | Marketing website with CMS and SEO |
| `api` | 3002 | Serverless API for webhooks, cron jobs |
| `email` | 3003 | React Email preview server |
| `docs` | 3004 | Documentation site (Mintlify) |
| `storybook` | 6006 | Design system component workshop |
| `studio` | 3005 | Prisma Studio for database editing |

**Core Packages**: `auth`, `database`, `payments`, `email`, `cms`, `design-system`, `analytics`, `observability`, `security`, `storage`, `seo`, `feature-flags`, `internationalization`, `webhooks`, `cron`, `notifications`, `collaboration`, `ai`, `rate-limit`, `next-config`, `typescript-config`.

For detailed structure, see `references/architecture.md`.

## Key Concepts

### Environment Variables

Environment variable files live alongside apps and packages:

- `apps/app/.env.local` — Main app keys (Clerk, Stripe, etc.)
- `apps/web/.env.local` — Marketing site keys
- `apps/api/.env.local` — API keys
- `packages/database/.env` — `DATABASE_URL` (required)
- `packages/cms/.env.local` — BaseHub token
- `packages/internationalization/.env.local` — Languine project ID

Each package has a `keys.ts` file that validates environment variables with Zod via `@t3-oss/env-nextjs`. Type safety is enforced at build time.

### Inter-App URLs

Local URLs are pre-configured:

- `NEXT_PUBLIC_APP_URL=http://localhost:3000`
- `NEXT_PUBLIC_WEB_URL=http://localhost:3001`
- `NEXT_PUBLIC_API_URL=http://localhost:3002`
- `NEXT_PUBLIC_DOCS_URL=http://localhost:3004`

Update these to production domains when deploying (e.g., `app.yourdomain.com`, `www.yourdomain.com`).

### Server Components First

`page.tsx` and `layout.tsx` files are always server components. Client interactivity goes in separate files with `'use client'`. Access databases, secrets, and server-only APIs directly in server components and server actions.

### Graceful Degradation

All integrations beyond the database are optional. Clients use optional chaining (e.g., `stripe?.prices.list()`, `resend?.emails.send()`). If the corresponding environment variable is not set, the feature is silently disabled.

## Common Tasks

### Running Development

```bash
bun run dev                  # All apps
bun dev --filter app         # Single app (port 3000)
bun dev --filter web         # Marketing site (port 3001)
```

### Database Migrations

After changing `packages/database/prisma/schema.prisma`:

```bash
bun run migrate
```

This runs Prisma format, generate, and db push in sequence.

### Adding shadcn/ui Components

```bash
npx shadcn@latest add [component] -c packages/design-system
```

Update existing components:

```bash
bun run bump-ui
```

### Adding a New Package

Create a new directory in `/packages/` with a `package.json` using the `@repo/<name>` naming convention. Add it as a dependency in consuming apps.

### Linting and Formatting

```bash
bun run lint                 # Check code style (Ultracite/Biome)
bun run format               # Fix code style
```

### Testing

```bash
bun run test                 # Run tests across monorepo
```

### Building

```bash
bun run build                # Build all apps and packages
bun run analyze              # Bundle analysis
```

### Deployment

Deploy to Vercel by creating separate projects for `app`, `web`, and `api` — each pointing to its respective root directory under `/apps/`. Add environment variables per project or use Vercel Team Environment Variables.

For detailed setup and customization instructions, see:

- `references/setup.md` — Installation, prerequisites, environment variables, database and Stripe CLI setup
- `references/packages.md` — Detailed documentation for every package
- `references/customization.md` — Swapping providers, extending features, deployment configuration
- `references/architecture.md` — Full monorepo structure, Turborepo pipeline, scripts
