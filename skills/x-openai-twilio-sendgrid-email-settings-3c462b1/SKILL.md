---
name: x-openai-twilio-sendgrid-email-settings-3c462b1
description: Configure SendGrid dynamic templates (Handlebars), tracking settings (opens, clicks, subscriptions), link branding for custom tracking domains, and content types (HTML, plain text, AMP). Use when customizing SendGrid email content, tracking behavior, or branded links. Requires a SendGrid API key (SG.-prefix) — not applicable to the Twilio Email API (comms.twilio.com).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

SendGrid email settings control how your messages are constructed, personalized, and tracked. Most configuration happens in the SendGrid Console, but templates and tracking can also be managed via API.

---

## Dynamic Templates

Templates use Handlebars syntax and are managed in Console > Email API > Dynamic Templates. Template IDs start with `d-`.

**Supported Handlebars helpers:**

| Helper | Use | Example |
|--------|-----|---------|
| `if` / `unless` | Conditional | `{{#if premium}}Welcome back!{{/if}}` |
| `each` | Iteration | `{{#each items}}{{this.name}}{{/each}}` |
| `equals` / `notEquals` | Comparison | `{{#equals status "active"}}...{{/equals}}` |
| `and` / `or` | Boolean logic | `{{#and premium verified}}...{{/and}}` |
| `greaterThan` / `lessThan` | Numeric | `{{#greaterThan count 5}}...{{/greaterThan}}` |
| `length` | Array/string | `{{length items}}` |
| `formatDate` | Date format | `{{formatDate date "MM/DD/YYYY"}}` |
| `insert` | Module insert | `{{insert "module_name"}}` |

**NOT supported:** Custom helpers, inline partials, `lookup`, `log`, `with`, `blockHelperMissing`. SendGrid implements a subset of Handlebars.js.

### Template Versions

- **Dynamic templates** (IDs starting with `d-`): Support Handlebars
- **Legacy transactional templates**: Use `-substitution-` syntax — not interchangeable with Handlebars

---

## Tracking Settings

| Setting | What it does | Caveat |
|---------|-------------|--------|
| **Open tracking** | Inserts a tracking pixel | Unreliable: Apple Mail Privacy Protection inflates opens; image-blocking clients produce false negatives |
| **Click tracking** | Rewrites URLs through SendGrid's redirect | Can trigger spam filters on some domains |
| **Subscription tracking** | Adds unsubscribe footer | Required for CAN-SPAM compliance |
| **Google Analytics** | Adds UTM parameters | Only for marketing campaigns |

Configure per-message or account-wide in Console > Settings > Tracking.

---

## Link Branding (Custom Tracking Domains)

By default, click-tracked links route through `url####.ct.sendgrid.net`. Link Branding lets you use your own domain (e.g., `links.yourdomain.com`) instead, which improves deliverability and builds trust.

**Setup:** Console > Settings > Sender Authentication > Link Branding

Requires a CNAME DNS record pointing your subdomain to `sendgrid.net`. Validate via API: `GET /v3/whitelabel/links/{id}/validate`

---

## Content Type Priority

When sending multiple content types, email clients display in this priority:

1. `text/x-amp-html` (AMP — only in supporting clients, requires sender registration)
2. `text/html` (standard — most clients)
3. `text/plain` (fallback)

Always include at least `text/plain` and `text/html`.

---

## CANNOT

- **Cannot use custom Handlebars helpers** — Only the built-in set listed above.
- **Cannot guarantee open tracking accuracy** — Pixel-based tracking is fundamentally unreliable. Do not use for business-critical logic.
- **Personalizations `subject` is a plain string override** — It bypasses the template subject. To use dynamic subjects, set Handlebars variables (e.g., `{{{subject}}}`) in the Dynamic Template's subject field and pass values via `dynamic_template_data`.
- **Undefined template variables are silent** — Missing keys in `dynamic_template_data` render as empty strings with no error.

---

## Next Steps

- **Send email:** `twilio-sendgrid-email-send`
- **Delivery tracking:** `twilio-sendgrid-webhooks`
- **Manage bounces/unsubscribes:** `twilio-sendgrid-suppressions`
