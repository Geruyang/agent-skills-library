---
name: x-openai-sign-in-with-vercel-3d5c426
description: Sign in with Vercel guidance — OAuth 2.0/OIDC identity provider for user authentication via Vercel accounts. Use when implementing user login with Vercel as the identity provider.
metadata:
  priority: '6'
  docs: '[''https://vercel.com/docs/sign-in-with-vercel'']'
  sitemap: https://vercel.com/sitemap/docs.xml
  pathPatterns: '[''app/api/auth/**'', ''app/login/**'', ''src/app/api/auth/**'', ''src/app/login/**'', ''pages/api/auth/**'']'
  bashPatterns: '[]'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Sign in with Vercel

You are an expert in Sign in with Vercel — Vercel's OAuth 2.0 / OpenID Connect identity provider.

## What It Is

Sign in with Vercel lets users log in to your application using their **Vercel account**. Your app does not need to handle passwords, create accounts, or manage user sessions — Vercel acts as the identity provider (IdP).

## OAuth 2.0 Authorization Code Flow

```
1. User clicks "Sign in with Vercel"
2. Redirect to Vercel authorization URL
3. User grants consent on Vercel's consent page
4. Vercel redirects back with authorization code
5. Exchange code for tokens (ID Token + Access Token + Refresh Token)
```

## Tokens

| Token | Lifetime | Purpose |
|-------|----------|---------|
| **ID Token** | Signed JWT | Proves user identity (name, email, avatar) |
| **Access Token** | 1 hour | Bearer token for Vercel REST API calls |
| **Refresh Token** | 30 days | Silent re-authentication (rotates on use) |

## Configuration

1. Register your app at `https://vercel.com/dashboard/{team}/integrations/console` (the Integrations Console). Click **Create Integration** → fill in the OAuth details → note the Client ID and Client Secret.
2. Configure redirect URIs and scopes
3. Use any standard OAuth 2.0 client library (no Vercel-specific SDK required)

## When to Use

- Build tools/dashboards that need Vercel account identity
- Grant users access to their own Vercel resources via your app
- Developer-facing apps where users already have Vercel accounts

## When NOT to Use

- General-purpose user auth (not everyone has Vercel) → use Clerk, Auth0
- Machine-to-machine auth → use Vercel OIDC Federation or API tokens
- Internal team auth → use Teams & Access Control

## References

- 📖 docs: https://vercel.com/docs/sign-in-with-vercel
