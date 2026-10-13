---
name: x-openai-twilio-sendgrid-account-setup-dd7255e
description: Set up a SendGrid account for email delivery. Covers API key creation (SG.-prefix), domain authentication (DKIM/SPF via CNAME records), Single Sender Verification for testing, SDK installation, and the relationship between SendGrid and Twilio credentials. Use before any other SendGrid skill. This skill is for SendGrid only — not the Twilio Email API (comms.twilio.com).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

SendGrid is Twilio's email delivery engine but uses a **completely separate authentication system** — SendGrid API keys (starting with `SG.`) are not Twilio API keys. You cannot use Account SID/Auth Token for SendGrid, and no Twilio MCP tools wrap SendGrid.

---

## Quickstart

1. Get your API key from [SendGrid Console > Settings > API Keys](https://app.sendgrid.com/settings/api_keys)
2. Set environment variable:

```bash
export SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

3. Install SDK:

| Language | Install | Package |
|----------|---------|---------|
| Python | `pip install sendgrid` | `sendgrid` |
| Node.js | `npm install @sendgrid/mail` | `@sendgrid/mail` (v8.x) |
| Java | Maven | `com.sendgrid:sendgrid-java` |
| C# | `dotnet add package SendGrid` | `SendGrid` |
| Ruby | `gem install sendgrid-ruby` | `sendgrid-ruby` |
| PHP | `composer require sendgrid/sendgrid` | `sendgrid/sendgrid` |
| Go | `go get github.com/sendgrid/sendgrid-go` | `sendgrid-go` |

4. Authenticate your sending domain (see below)

---

## API Key Scopes

| Scope | Use for | Risk |
|-------|---------|------|
| **Full Access** | Development only | Can do everything — never deploy with this |
| **Restricted Access** | Production | Scope to only what your app needs (e.g., Mail Send only) |
| **Billing Access** | Account management | Separate from mail operations |

A "Mail Send" restricted key can send email but cannot read suppressions, manage templates, or access stats. If you get `403 Forbidden`, check key permissions.

---

## SMTP Relay (Alternative to API)

SendGrid also supports SMTP for sending. Useful for frameworks with built-in SMTP support (e.g., Laravel, Django, Rails).

| Setting | Value |
|---------|-------|
| **Server** | `smtp.sendgrid.net` |
| **Port** | `587` (TLS) or `465` (SSL) |
| **Username** | `apikey` (literal string, not your key name) |
| **Password** | Your SendGrid API key (`SG.xxx`) |

---

## Domain Authentication (Required for Production)

Single Sender Verification is for testing only. Production requires domain authentication for deliverability.

**Setup:** SendGrid Console > Settings > Sender Authentication > Authenticate Your Domain

Create 3 CNAME DNS records:
1. `s1._domainkey.yourdomain.com` → `s1.domainkey.u1234.wl.sendgrid.net` (DKIM)
2. `s2._domainkey.yourdomain.com` → `s2.domainkey.u1234.wl.sendgrid.net` (DKIM)
3. `em1234.yourdomain.com` → `u1234.wl.sendgrid.net` (return path)

Verify via API: `GET /v3/whitelabel/domains/{id}/validate`

**DMARC:** After setting up DKIM and SPF via domain authentication, configure a DMARC DNS record (`_dmarc.yourdomain.com`) to instruct receiving servers how to handle authentication failures. Start with `p=none` for monitoring before enforcing.

**Dedicated IP (Pro+ plans):** Isolates your sending reputation. Requires an IP warming schedule — start with low volume and increase over 30 days.

---

## SendGrid and Twilio

| Twilio product | How it uses SendGrid | Sends email? |
|----------------|---------------------|-------------|
| **SendGrid** (this skill) | Direct email delivery via `api.sendgrid.com` | Yes |
| **Twilio Email API** | Direct email delivery via `comms.twilio.com/v1/emails` — uses Twilio creds, not SendGrid keys | Yes (separate product) |
| **Verify** | OTP via `channel: 'email'` | Delegates to SendGrid via Mailer config |
| **Conversations** | Tracks EMAIL as a channel type | No — logs/tracks only |
| **Flex** | Email channel for agents | Uses SendGrid for delivery |

**Servers:**
- Global: `https://api.sendgrid.com`
- EU regional: `https://api.eu.sendgrid.com`

---

## CANNOT

- **Cannot use Twilio credentials for SendGrid** — Separate API keys (`SG.`-prefix), separate Console, separate billing.
- **Cannot access SendGrid via Twilio MCP tools** — No MCP integration. Use SDK or direct REST.
- **Single Sender Verification requires re-verification on address change** — Changing the sender email requires a new verification. Use Domain Authentication for production.
- **Domain Authentication requires DNS access** — 3 CNAME records needed. If you can't modify DNS, you can't authenticate.
- **Domain Authentication API returns stale entries** — `GET /v3/whitelabel/domains` includes old invalid entries. Filter by `valid: true`.
- **API Key Secret shown only at creation** — Cannot retrieve afterward. Store immediately.

> **Security:** Your API key is shown only once at creation. Never display, log, or repeat a user's API key in responses. If a user shares their key in conversation, advise them to rotate it immediately. Store keys in a secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.), not in code or environment files committed to version control.

---

## Next Steps

- **Send email:** `twilio-sendgrid-email-send`
- **Domain settings and templates:** `twilio-sendgrid-email-settings`
- **Delivery tracking:** `twilio-sendgrid-webhooks`
- **Docs:** [SendGrid API Reference](https://www.twilio.com/docs/sendgrid/api-reference)
