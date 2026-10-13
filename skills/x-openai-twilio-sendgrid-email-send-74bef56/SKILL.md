---
name: x-openai-twilio-sendgrid-email-send-74bef56
description: Send transactional and bulk email via the SendGrid v3 Mail Send API. Covers single sends, personalized batch sends with dynamic templates, scheduled sends with cancellation, attachments, and sandbox mode for testing. Use this skill when the caller has a SendGrid API key (SG.-prefix). Do NOT use this skill if the caller is using the Twilio Email API (comms.twilio.com) — that is a separate product with different credentials.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

> **Agent safety:** Always confirm recipients, subject, and content with the user before sending. Email is irreversible once delivered. Never send email autonomously without explicit user approval — especially for batch sends to multiple recipients.

All email sending goes through `POST /v3/mail/send`. This endpoint returns `202 Accepted` (queued) — NOT `200 OK` (delivered). Delivery confirmation comes asynchronously via Event Webhook. See `twilio-sendgrid-webhooks`.

---

## Basic Send

**Python**
```python
import os, sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
message = Mail(
    from_email="verified@yourdomain.com",
    to_emails="recipient@example.com",
    subject="Order Confirmation",
    html_content="<p>Your order #1234 is confirmed.</p>"
)
response = sg.send(message)
print(f"Status: {response.status_code}")  # 202 = queued
```

**Node.js**
```javascript
const sgMail = require("@sendgrid/mail");
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const [response] = await sgMail.send({
    to: "recipient@example.com",
    from: "verified@yourdomain.com",
    subject: "Order Confirmation",
    html: "<p>Your order #1234 is confirmed.</p>",
});
console.log(`Status: ${response.statusCode}`); // 202 = queued
```

---

## Personalized Batch Send with Dynamic Templates

Dynamic templates use Handlebars syntax. Template IDs start with `d-`. Create templates in SendGrid Console > Email API > Dynamic Templates.

**Python**
```python
from sendgrid.helpers.mail import Mail, To

message = Mail(
    from_email="noreply@yourdomain.com",
    to_emails=[
        To("alice@example.com", dynamic_template_data={"name": "Alice", "order_id": "123"}),
        To("bob@example.com", dynamic_template_data={"name": "Bob", "order_id": "456"}),
    ],
)
message.template_id = "d-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
sg.send(message)
```

**Node.js**
```javascript
await sgMail.send({
    from: { email: "noreply@yourdomain.com" },
    template_id: "d-xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    personalizations: [
        { to: [{ email: "alice@example.com" }], dynamic_template_data: { name: "Alice", order_id: "123" } },
        { to: [{ email: "bob@example.com" }], dynamic_template_data: { name: "Bob", order_id: "456" } },
    ],
});
```

**Recipients in the same `to` array within a single personalization can see each other.** For private sends, use separate personalizations (one per recipient).

---

## Scheduled Sends

Schedule up to 72 hours in advance. Cancellation requires a batch ID assigned *before* sending.

**Python**
```python
import time, requests

headers = {"Authorization": f"Bearer {os.environ['SENDGRID_API_KEY']}", "Content-Type": "application/json"}

# Get batch ID first
batch = requests.post("https://api.sendgrid.com/v3/mail/batch", headers=headers).json()

# Include batch_id and send_at in the message
send_at = int(time.time()) + 3600  # Unix SECONDS, not ms

# Cancel if needed (before send_at)
requests.post("https://api.sendgrid.com/v3/user/scheduled_sends",
    headers=headers,
    json={"batch_id": batch["batch_id"], "status": "cancel"})
```

---

## Attachments

Base64-encode files in the `attachments` array. Total limit: 30MB per request (~22MB before encoding overhead).

```python
import base64
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

with open("invoice.pdf", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

message = Mail(from_email="billing@yourdomain.com", to_emails="customer@example.com",
               subject="Your Invoice", html_content="<p>Invoice attached.</p>")
message.attachment = Attachment(FileContent(encoded), FileName("invoice.pdf"),
                                FileType("application/pdf"), Disposition("attachment"))
sg.send(message)
```

---

## Categories and Custom Args

**Categories** tag sends for analytics segmentation (up to 10 per message):
```python
message.category = ["transactional", "order-confirmation"]
```

**Custom Args** pass metadata through to Event Webhooks (key-value strings only):
```python
message.custom_args = {"order_id": "1234", "env": "production"}
```

These appear in webhook event payloads, enabling you to correlate delivery events back to your application data.

---

## Sandbox Mode (Testing)

Validates the request without delivering. Returns `200 OK` (not `202`).

```python
message.mail_settings = {"sandbox_mode": {"enable": True}}
response = sg.send(message)  # 200 = validated, not sent
```

---

## CANNOT

- **Cannot send more than 1,000 recipients per API call** — Hard limit. Split into multiple requests.
- **Cannot schedule sends more than 72 hours in advance** — `send_at` rejects timestamps beyond 72h.
- **Cannot cancel a send after processing** — Only scheduled messages with a pre-assigned batch ID can be cancelled.
- **Cannot use `send_at` with milliseconds** — JS `Date.now()` returns ms. Divide by 1000 or the timestamp is silently rejected (>72h).
- **The `subject` field in personalizations is a plain string override** — To use dynamic subjects, set Handlebars variables (e.g., `{{{subject}}}`) in the Dynamic Template's subject field and pass values via `dynamic_template_data`. The personalizations `subject` key bypasses the template subject entirely.
- **Undefined template variables render as empty strings** — No error for typos in `dynamic_template_data` keys. Silent failures.
- **`413 Payload Too Large` returns nginx HTML, not JSON** — Exceeding 30MB returns HTML error page. Check Content-Type before parsing.
- **Empty `content` when using `template_id`** — Omit the `content` field. If you include both, `template_id` takes precedence and `content` is ignored.

> **Agent usage:** When sending email on behalf of a user, always report back what was sent — recipients, subject, and the API response status code. Maintain an application-level audit log for all sends.

---

## Next Steps

- **Account setup and domain auth:** `twilio-sendgrid-account-setup`
- **Templates and settings:** `twilio-sendgrid-email-settings`
- **Delivery tracking via webhooks:** `twilio-sendgrid-webhooks`
- **Manage bounces and unsubscribes:** `twilio-sendgrid-suppressions`
