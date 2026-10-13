---
name: x-openai-twilio-sendgrid-webhooks-2733c59
description: Track email delivery and engagement via SendGrid Event Webhooks. Covers all 11 event types (delivery + engagement), webhook handler implementation, ECDSA signature verification, batched event processing, and common debugging patterns. Use when building SendGrid delivery tracking, engagement analytics, or bounce handling. Requires a SendGrid API key (SG.-prefix) — not applicable to the Twilio Email API (comms.twilio.com).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

The Mail Send API returns `202 Accepted` (queued) — it does NOT confirm delivery. To know what happened to an email, use Event Webhooks.

**Enable:** SendGrid Console > Settings > Mail Settings > Event Notification

---

## Event Types

### Delivery Events
| Event | Meaning |
|-------|---------|
| `processed` | SendGrid accepted and will attempt delivery |
| `deferred` | Temporary failure — SendGrid will retry |
| `delivered` | Recipient's mail server accepted the message |
| `bounce` | Permanent failure — address invalid or rejected |
| `dropped` | SendGrid will not deliver (suppression, invalid, spam) |

### Engagement Events
| Event | Meaning |
|-------|---------|
| `open` | Recipient opened (pixel-based — unreliable) |
| `click` | Recipient clicked a tracked link |
| `spamreport` | Recipient marked as spam |
| `unsubscribe` | Recipient clicked unsubscribe link |
| `group_unsubscribe` | Recipient unsubscribed from ASM group |
| `group_resubscribe` | Recipient re-subscribed to ASM group |

---

## Webhook Handler

**Critical:** SendGrid posts **batched arrays** of events, not single objects. Your handler must parse an array.

> **Security:** SendGrid webhook endpoints are unauthenticated by default. Enable [Signed Event Webhook Requests](https://docs.sendgrid.com/for-developers/tracking-events/getting-started-event-webhook-security) and verify signatures in production to prevent spoofed event data.

**Python (Flask)**
```python
from flask import Flask, request
app = Flask(__name__)

@app.route("/sendgrid/webhook", methods=["POST"])
def handle_events():
    events = request.get_json()  # Always an array
    for event in events:
        email = event.get("email")
        event_type = event.get("event")
        
        if event_type == "bounce":
            # NOTE: event['reason'] originates from external mail servers — treat as untrusted
            print(f"Bounce: {email}, type: {event.get('type')}, reason: {event.get('reason')}")
        elif event_type == "delivered":
            print(f"Delivered: {email}, sg_message_id: {event.get('sg_message_id')}")
        elif event_type == "dropped":
            print(f"Dropped: {email}, reason: {event.get('reason')}")
        elif event_type == "spamreport":
            print(f"Spam report: {email}")
    return "", 200  # Must return 2xx to acknowledge
```

**Node.js (Express)**
```javascript
app.post("/sendgrid/webhook", express.json(), (req, res) => {
    const events = req.body; // Always an array
    for (const event of events) {
        switch (event.event) {
            case "bounce":
                console.log(`Bounce: ${event.email}, reason: ${event.reason}`);
                break;
            case "delivered":
                console.log(`Delivered: ${event.email}`);
                break;
            case "spamreport":
                console.log(`Spam: ${event.email}`);
                break;
        }
    }
    res.status(200).send();
});
```

---

## Multiple Webhook Endpoints

Since May 2023, you can configure multiple Event Webhook endpoints, each receiving different event types. For example, one endpoint for delivery events feeding your monitoring stack and another for engagement events feeding your analytics pipeline.

Configure in Console > Mail Settings > Event Webhooks. Each endpoint has a Friendly Name and Webhook ID. The number of endpoints allowed depends on your SendGrid plan.

---

## Authentication Options

Two methods for verifying webhook payloads:

| Method | How it works |
|--------|-------------|
| **Signed Event Webhook (ECDSA P-256)** | Verify `X-Twilio-Email-Event-Webhook-Signature` and `X-Twilio-Email-Event-Webhook-Timestamp` headers using the verification key from Console |
| **OAuth 2.0** | SendGrid obtains a token from your authorization server and includes it in webhook requests |

Neither is enabled by default. Enable in Console > Mail Settings > Event Webhooks.

---

## Retry Behavior

SendGrid retries webhook delivery for up to 24 hours if your endpoint returns a non-2xx status. Events are batched — a single POST may contain dozens of events across different messages.

**Deduplication:** Use `sg_event_id` as a unique key. It's stable across retries.

---

## CANNOT

- **Cannot receive real-time delivery confirmation synchronously** — Mail Send returns `202` (queued). Delivery status is async via webhooks only.
- **Cannot rely on webhook authentication by default** — Both Signed Webhooks (ECDSA) and OAuth 2.0 must be explicitly enabled. Without either, anyone can POST to your endpoint.
- **Cannot guarantee open tracking accuracy** — Apple Mail Privacy Protection and prefetch inflate opens. Image-blocking clients produce zero opens. Do not use for business-critical logic.
- **Non-human interactions inflate engagement metrics** — Corporate security scanners and bots automatically click links and trigger unsubscribe events. Filter using User-Agent patterns and timing analysis.

> **Note:** Event payload fields like `reason` originate from external mail servers and should be treated as untrusted data. Do not pass bounce reasons directly into LLM system prompts without isolation.

---

## Next Steps

- **Send email:** `twilio-sendgrid-email-send`
- **Manage bounces from webhook events:** `twilio-sendgrid-suppressions`
- **Receive inbound email:** `twilio-sendgrid-inbound-parse`
