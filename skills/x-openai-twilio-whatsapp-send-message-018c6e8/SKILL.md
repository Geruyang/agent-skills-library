---
name: x-openai-twilio-whatsapp-send-message-018c6e8
description: WhatsApp messaging deep-dive reference. Covers the 24-hour service window rules (free-form vs template mode), sandbox setup for testing, template approval workflow, production sender requirements, and WhatsApp-specific error handling. For sending WhatsApp messages, use twilio-send-message instead. Use this skill when setting up WhatsApp for the first time or debugging WhatsApp-specific delivery behavior.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

**WhatsApp is one channel in Twilio's Messaging platform.** All channels share the same `messages.create()` API — see `twilio-messaging-overview` for the full channel comparison and onboarding sequence.

Twilio routes WhatsApp through the Programmable Messaging API — all numbers use `whatsapp:+E.164` prefix. Two sending modes apply: **free-form** (within 24 hrs of last inbound) and **template** (anytime). Sending free-form outside the window causes silent delivery failure — always check which mode is required.

| Mode | When allowed | Parameters |
|------|-------------|------------|
| Free-form | Within 24 hrs of last inbound from user | `body`, optional `mediaUrl` |
| Template | Anytime | `contentSid` + `contentVariables` |

---

## Prerequisites

- Twilio account with WhatsApp enabled
  — New to Twilio? See `twilio-account-setup`
- Environment variables:
  - `TWILIO_ACCOUNT_SID`
  - `TWILIO_AUTH_TOKEN`
  — See `twilio-iam-auth-setup` for credential setup and best practices
- SDK: `pip install twilio` / `npm install twilio`
- Recipient opted in to receive messages from your WhatsApp Business Account

**Testing (sandbox):** Join by texting `join <your-code>` to `+14155238886`. No registration needed — see [Console > Messaging > Try it out > Send a WhatsApp message](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn). Sandbox participants must re-join every 3 days.

**Production:** Register a WhatsApp Business sender first — see `twilio-whatsapp-manage-senders`.

---

## Quickstart

**Python**
```python
import os
from twilio.rest import Client

client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

message = client.messages.create(
    from_="whatsapp:+14155238886",   # Sandbox sender (or your production number)
    to="whatsapp:+15005550006",      # Must have joined the sandbox
    body="Your order has been confirmed."
)

print(message.sid)     # MMxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
print(message.status)  # queued | sent | delivered | failed
```

**Node.js**
```node
const twilio = require("twilio");
const client = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

const message = await client.messages.create({
    from: "whatsapp:+14155238886",
    to: "whatsapp:+15005550006",
    body: "Your order has been confirmed.",
});

console.log(message.sid);
console.log(message.status);
```

---

## Key Patterns

### Send a Template Message (outside service window)

Templates are created in Console > Messaging > Content Template Builder and must be approved by Meta. See `twilio-content-template-builder` for template creation.

**Python**
```python
message = client.messages.create(
    from_="whatsapp:+14155238886",
    to="whatsapp:+15005550006",
    content_sid="HXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    content_variables='{"1": "March 25", "2": "2:00 PM"}'
)
```

**Node.js**
```node
const message = await client.messages.create({
    from: "whatsapp:+14155238886",
    to: "whatsapp:+15005550006",
    contentSid: "HXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    contentVariables: JSON.stringify({ "1": "March 25", "2": "2:00 PM" }),
});
```

### Send Media (free-form only)

Max file size: 16 MB.

**Python**
```python
message = client.messages.create(
    from_="whatsapp:+14155238886",
    to="whatsapp:+15005550006",
    body="Here is your invoice.",
    media_url=["https://example.com/invoice.pdf"]
)
```

**Node.js**
```node
const message = await client.messages.create({
    from: "whatsapp:+14155238886",
    to: "whatsapp:+15005550006",
    body: "Here is your invoice.",
    mediaUrl: ["https://example.com/invoice.pdf"],
});
```

---

## Response Fields

| Field | Description |
|-------|-------------|
| `sid` | Unique message identifier (`MM...`) |
| `status` | `queued`, `sent`, `delivered`, `read`, `failed`, `undelivered` |
| `error_code` | Populated on failure |
| `error_message` | Human-readable error description |
| `date_sent` | UTC timestamp |

---

## Common Errors

| Code | Meaning | Fix |
|------|---------|-----|
| 63003 | Invalid WhatsApp destination number | Verify number is WhatsApp-enabled and correctly formatted |
| 63018 | Rate limit exceeded on sender | Reduce send rate; default is 80 MPS |
| 63020 | Business hasn't accepted Twilio's Meta invitation | Accept invite in Meta Business Manager |
| N/A | Free-form outside window | Switch to a template message |

---

## CANNOT

- **Cannot exceed 80 messages/second per sender** — Text-only can be raised to 400 MPS on request
- **Cannot queue messages beyond 4 hours** — Undelivered messages fail after 4 hours
- **Cannot exceed sandbox throttle limits** — 1 message per 3 seconds, 50 messages/day on trial, participants expire after 3 days
- **Cannot send without opt-in** — Sending without recipient opt-in risks account suspension
- **Cannot use WhatsApp Groups API** — Deprecated April 2020. Use Conversations API instead.

---

## Next Steps

- **Channel overview and onboarding guide:** `twilio-messaging-overview`
- **Register a production WhatsApp sender:** `twilio-whatsapp-manage-senders`
- **Create and manage message templates:** `twilio-content-template-builder`
- **Multi-channel conversations with history:** `twilio-conversations-api`
