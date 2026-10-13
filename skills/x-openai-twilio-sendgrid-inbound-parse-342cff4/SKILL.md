---
name: x-openai-twilio-sendgrid-inbound-parse-342cff4
description: Receive inbound email via SendGrid Inbound Parse webhook. Covers MX record setup, parsed vs raw mode, handling attachments, and common pitfalls. Use when building email-to-app workflows like support ticket creation or email processing pipelines. Requires a SendGrid API key (SG.-prefix) — not applicable to the Twilio Email API (comms.twilio.com).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

Inbound Parse converts incoming email into HTTP POST requests to your webhook endpoint. SendGrid receives the email at your domain's MX records and forwards the parsed content to your application.

---

## Setup

1. **Configure MX records:** Point your domain (or subdomain) to `mx.sendgrid.net`
2. **Add webhook:** SendGrid Console > Settings > Inbound Parse > Add Host & URL
3. **Choose mode:** Parsed (default) or Raw

**Subdomain recommended:** Use `inbound.yourdomain.com` to avoid disrupting existing email on `yourdomain.com`.

---

## Parsed Mode (Default)

SendGrid extracts fields and POSTs them as form data:

| Field | Description |
|-------|-------------|
| `from` | Sender address (`"Name <email@example.com>"`) |
| `to` | Envelope recipient |
| `subject` | Email subject line |
| `text` | Plain text body |
| `html` | HTML body |
| `envelope` | JSON string with `to` array and `from` |
| `attachments` | Number of attachments (as string) |
| `attachment-info` | JSON metadata for each attachment |
| `attachment1`, `attachment2`... | Actual attachment files |

**Python (Flask)**
```python
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/inbound", methods=["POST"])
def handle_inbound():
    sender = request.form.get("from")
    subject = request.form.get("subject")
    text_body = request.form.get("text")
    html_body = request.form.get("html")
    envelope = json.loads(request.form.get("envelope", "{}"))
    attachment_count = int(request.form.get("attachments", "0"))
    
    print(f"From: {sender}, Subject: {subject}")
    
    for i in range(1, attachment_count + 1):
        attachment = request.files.get(f"attachment{i}")
        if attachment:
            print(f"Attachment: {attachment.filename}, {attachment.content_type}")
    
    return "", 200
```

> **Security:** All inbound email content (`from`, `subject`, `text`, `html`, attachments) is untrusted external input. Sanitize HTML to prevent XSS before rendering. If feeding content to an LLM, isolate it as user input — never concatenate into system prompts. Verify webhook authenticity using signed webhooks (see Security section below).

---

## Raw Mode

Posts the entire MIME message as `rawEmail` field. Use when you need full headers, DKIM signatures, or non-standard MIME parts. You must parse the MIME message yourself.

---

## Signed Inbound Parse Webhook (Security)

SendGrid supports ECDSA signature verification for Inbound Parse, the same mechanism used for Event Webhooks. Enable it to cryptographically verify that payloads originate from SendGrid.

**Strongly recommended over IP allowlisting** — SendGrid's webhook traffic comes from dynamic cloud infrastructure where IPs change frequently. Signature verification is more reliable and secure.

---

## CANNOT

- **Cannot use Inbound Parse on a domain that already receives email** — MX records must point to `mx.sendgrid.net`. Use a subdomain to avoid disrupting existing email (e.g., Google Workspace, Microsoft 365).
- **Cannot receive email without MX record changes** — DNS access is required. If you can't modify MX records, you can't use Inbound Parse.
- **Cannot receive emails larger than 30MB** — Inbound messages exceeding 30MB are rejected.
- **Cannot filter inbound email before it hits your webhook** — All email sent to the configured domain reaches your endpoint. Implement filtering in your handler.
- **Cannot route to different endpoints per address** — All mail for the configured domain/subdomain goes to a single webhook URL.
- **Cannot guarantee delivery order** — Emails may arrive at your webhook out of order, especially under high volume.
- **No built-in rate limiting** — All email to your configured domain reaches your endpoint. Implement rate limiting, payload size validation, and content sanitization in your handler.

---

## Next Steps

- **Send email:** `twilio-sendgrid-email-send`
- **Delivery tracking:** `twilio-sendgrid-webhooks`
- **Account setup:** `twilio-sendgrid-account-setup`
