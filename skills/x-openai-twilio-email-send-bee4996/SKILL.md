---
name: x-openai-twilio-email-send-bee4996
description: Use when the caller has Twilio credentials (Account SID + Auth Token or API Key SID + Secret) and needs to send email via comms.twilio.com/v1/Emails. This is Twilio-native email — NOT SendGrid. Do NOT use if the caller has a SendGrid API key (SG.-prefix) — use twilio-sendgrid-email-send instead. Covers single sends, batch sends up to 10,000 recipients, Liquid personalization, operation tracking, and error handling.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

> **Agent safety:** Always confirm recipients, subject, and content with the user before sending. Email is irreversible once delivered. Never send email autonomously without explicit user approval — especially for batch sends to multiple recipients.

**Twilio Email is a separate product from SendGrid.** Both send email, but they use different APIs, credentials, templating languages, and endpoints. If you have a SendGrid API key (`SG.`-prefix), use `twilio-sendgrid-email-send` instead.

| | Twilio Email (this skill) | SendGrid |
|---|---|---|
| **Base URL** | `https://comms.twilio.com/v1/emails` | `https://api.sendgrid.com/v3/mail/send` |
| **Auth** | Twilio Account SID + Auth Token (or API Key SID + Secret) | SendGrid API key (`SG.`-prefix) |
| **Templating** | Liquid (`{{variable}}`) | Handlebars (`{{variable}}`) |
| **Max recipients/request** | 10,000 | 1,000 |
| **Max message size** | 10MB (including attachments) | 30MB |
| **Status tracking** | Operation resource (poll `operationLocation`) | Event Webhooks (async POST) |
| **Console** | console.twilio.com | app.sendgrid.com |

---

## Prerequisites

- A Twilio account — see `twilio-account-setup` for signup and credentials
- A **Verified Sender**: an approved domain identity configured in the Twilio console that must match the `from` address domain
- Compliance with regional anti-spam regulations (CAN-SPAM, GDPR)

For a complete setup guide, see the Email Onboarding guide in the Twilio console.

---

## Authentication

The API uses **Basic Authentication** with either:
- Account SID + Auth Token
- API Key SID + API Key Secret

These are standard Twilio credentials — the same ones used for SMS, Voice, and other Twilio APIs.

---

## Send a Simple Email

`POST https://comms.twilio.com/v1/Emails`

The endpoint is **asynchronous** — it returns `202 Accepted` with an `operationId`, not a delivery confirmation.

```bash
curl -X POST "https://comms.twilio.com/v1/Emails" \
  --header "Content-Type: application/json" \
  --data '{
    "from": {
      "address": "support@example.com",
      "name": "Support Team"
    },
    "to": [
      {
        "address": "john.doe@example.com",
        "name": "John Doe"
      }
    ],
    "content": {
      "subject": "Your subject line",
      "html": "<p>Your message content in HTML format.</p>",
      "text": "Your message content in plain text."
    }
  }' \
  -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN
```

Response (`202 Accepted`):
```json
{
  "operationId": "...",
  "operationLocation": "https://comms.twilio.com/v1/Emails/Operations/..."
}
```

Poll `operationLocation` to track delivery status.

---

## Batch Sending

Send the same message to multiple recipients in a single request by adding entries to the `to` array. Maximum **10,000 recipients** per request.

```json
{
  "from": {
    "address": "support@example.com",
    "name": "Support Team"
  },
  "to": [
    {
      "address": "john.doe@example.com",
      "name": "John Doe"
    },
    {
      "address": "jane.smith@example.com",
      "name": "Jane Smith"
    }
  ],
  "content": {
    "subject": "Your subject line",
    "html": "<p>Your message content in HTML format.</p>",
    "text": "Your message content in plain text."
  }
}
```

---

## Liquid Personalization

Use Liquid templating in the `content.subject`, `content.html`, and `content.text` fields. For each variable referenced (e.g. `{{firstName}}`), provide a matching key in the `variables` object for every recipient in the `to` array.

```json
{
  "from": {
    "address": "noreply@example.com",
    "name": "Support Team"
  },
  "to": [
    {
      "address": "alice@example.com",
      "name": "Alice",
      "variables": {"firstName": "Alice", "orderId": "123"}
    },
    {
      "address": "bob@example.com",
      "name": "Bob",
      "variables": {"firstName": "Bob", "orderId": "456"}
    }
  ],
  "content": {
    "subject": "Hi {{firstName}}, your order update",
    "html": "<p>Hi {{firstName}}, order #{{orderId}} has shipped.</p>",
    "text": "Hi {{firstName}}, order #{{orderId}} has shipped."
  }
}
```

Ensure every recipient has all referenced variables defined.

---

## Operation Tracking

After submitting a send, use the Operation resource to monitor batch status.

1. Submit email via `POST /v1/emails` — response includes `operationId` and `operationLocation`
2. Poll status via `GET` to the `operationLocation` URI
3. The operation tracks progress for the entire batch

This is especially important for large recipient lists where processing is not instantaneous.

---

## Error Codes

| Status Code | Description | Action |
|-------------|-------------|--------|
| **202** | Accepted | Request accepted, Operation created. Poll `operationLocation` for status. |
| **400** | Bad Request | Malformed or ambiguous request content. Check JSON payload. |
| **401** | Unauthorized | Verify Account SID and Auth Token / API Key are correct. |
| **429** | Too Many Requests | Rate limited. Back off and retry. |
| **500** | Internal Server Error | Twilio server-side issue. Retry with backoff. |
| **503** | Service Unavailable | Temporarily unavailable. Retry after a short delay. |

Validation errors return as many issues as possible in a single response to help debug quickly.

---

## CANNOT

- **Cannot use SendGrid API keys** — Twilio Email uses Twilio Account SID + Auth Token or API Key SID + Secret. `SG.`-prefix keys do not work. Use `twilio-sendgrid-email-send` for SendGrid.
- **Cannot send more than 10,000 recipients per request** — Split into multiple requests for larger lists.
- **Cannot exceed 10MB per message** — Total size including attachments must be under 10MB (smaller than SendGrid's 30MB limit).
- **Cannot use Unicode in the `from` field** — Unicode encoding is not supported for sender addresses.
- **Cannot use Handlebars templating** — Twilio Email uses Liquid, not Handlebars. If you see `{{#if}}` or `{{#each}}`, that's Handlebars/SendGrid syntax.
- **Cannot get synchronous delivery confirmation** — The API is async. `202 Accepted` means queued, not delivered. Poll the Operation resource for status.
- **Tags total length cannot exceed 10,000 bytes** — Combined length of all tags on a request is limited.

---

## Next Steps

- **Account setup and credentials:** `twilio-account-setup`
- **SendGrid email (separate product):** `twilio-sendgrid-email-send`
- **SMS sending:** `twilio-sms-send-message`
