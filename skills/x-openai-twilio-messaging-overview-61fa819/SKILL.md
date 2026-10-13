---
name: x-openai-twilio-messaging-overview-61fa819
description: Twilio Messaging channel overview and onboarding guide. Covers all channels (SMS, WhatsApp, RCS, Facebook Messenger), the unified Messages API, channel selection guidance, and the recommended setup sequence from first message to production monitoring. Start here before choosing a specific messaging channel.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

Twilio's Messaging platform sends and receives messages across multiple channels through a single API. All channels use `client.messages.create()` — only the address format changes.

| Channel | Address format | Rich media | Template required? | Reach | Skill |
|---------|---------------|------------|-------------------|-------|-------|
| **SMS/MMS** | `+15551234567` (E.164) | MMS: images/video, US/CA/AU only | No | Global (180+ countries) | `twilio-sms-send-message` |
| **WhatsApp** | `whatsapp:+15551234567` | Yes (images, docs, video, location) | Outside 24hr window: yes | 190+ countries | `twilio-whatsapp-send-message` |
| **RCS** | Same number (via Messaging Service) | Yes (rich cards, carousels, video) | No | US + expanding globally | `twilio-rcs-messaging` |
| **Facebook Messenger** | `messenger:{page-scoped-id}` | Yes | No | Global | — |

---

## Which Channel Should I Use?

| If you need to... | Use | Why |
|-------------------|-----|-----|
| Reach any phone number | SMS | Universal — works on every phone, no app needed |
| Send rich media globally | WhatsApp | Images, docs, video work worldwide (MMS is US/CA/AU only) |
| Send time-sensitive alerts (OTP, outages) | SMS | Highest open rates, no app dependency |
| Reach opted-in audience at lower cost | WhatsApp | No per-message fee in many markets |
| Run marketing campaigns across channels | Start with `twilio-marketing-promotions-advisor` | Planner skill handles channel mix, compliance, and fallback |
| Send transactional notifications | Start with `twilio-notifications-alerts-advisor` | Planner skill handles urgency-based channel routing |

**Not sure?** Use a Planner skill first — it will qualify your use case and recommend the right channel combination.

---

## Unified API

All channels share `messages.create()`. The only difference is the address format in `from` and `to`.

**Python**
```python
import os
from twilio.rest import Client

client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

# SMS
sms = client.messages.create(
    from_="+15017122661",
    to="+15558675310",
    body="Your order shipped."
)

# WhatsApp — same API, prefixed addresses
whatsapp = client.messages.create(
    from_="whatsapp:+15017122661",
    to="whatsapp:+15558675310",
    body="Your order shipped."
)
```

**Node.js**
```javascript
const client = require("twilio")(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

// SMS
const sms = await client.messages.create({
    from: "+15017122661",
    to: "+15558675310",
    body: "Your order shipped.",
});

// WhatsApp — same API, prefixed addresses
const whatsapp = await client.messages.create({
    from: "whatsapp:+15017122661",
    to: "whatsapp:+15558675310",
    body: "Your order shipped.",
});
```

---

## Onboarding Sequence

Set up messaging in this order. Each step builds on the previous.

### Step 1: Foundation
Get a Twilio number, send your first SMS.
- `twilio-account-setup` → `twilio-sms-send-message`

### Step 2: Sender Strategy
Create a Messaging Service and add your numbers to a sender pool. Use `messagingServiceSid` instead of `from` for all production sends — this enables geo-match, sticky sender, and unlocks compliance features.
- `twilio-messaging-services`

### Step 3: Compliance
Register for A2P 10DLC (required for US SMS traffic). Set up opt-out handling.
- `twilio-compliance-onboarding` → `twilio-compliance-traffic`

### Step 4: Protect
Enable SMS pumping protection (prevents artificial traffic inflation) and compliance toolkit (quiet hours, reassigned number detection) on your Messaging Service.
- `twilio-messaging-services` (Compliance Toolkit + SMS Pumping Protection sections)

### Step 5: Add Channels
Add WhatsApp or other channels. Use Content Templates for cross-channel message formatting.
- `twilio-whatsapp-send-message` → `twilio-content-template-builder`

### Step 6: Monitor
Enable intelligent alerts for error pattern detection. Set up status callbacks for delivery tracking.
- `twilio-messaging-services` (Intelligent Alerts section) → `twilio-messaging-webhooks`

---

## CANNOT

- **Cannot send cross-channel in a single API call** — Each `messages.create()` targets one channel. For multi-channel fallback, implement sequencing in your application (e.g., try SMS, on failure send WhatsApp).
- **Cannot use WhatsApp free-form messages outside the 24-hour window** — After 24 hours since the user's last inbound message, you must use a pre-approved template. See `twilio-whatsapp-send-message`.
- **Cannot send MMS outside US, Canada, and Australia** — MMS is only supported on US/CA/AU numbers. For international rich media, use WhatsApp.
- **Cannot use SMS pumping protection or compliance toolkit without a Messaging Service** — These features are configured per Messaging Service. Raw `from` number sends don't get these protections.
- **Cannot mix channels in a single Messaging Service sender pool** — A Messaging Service manages phone numbers for SMS/MMS. WhatsApp senders are configured separately.
- **Cannot guarantee delivery on any channel** — SMS can be carrier-filtered, WhatsApp can queue-timeout (4 hours). Always implement status callbacks to track delivery.

---

## Next Steps

- **Send SMS:** `twilio-sms-send-message`
- **Send RCS:** `twilio-rcs-messaging`
- **Send WhatsApp:** `twilio-whatsapp-send-message`
- **Set up sender pools and production features:** `twilio-messaging-services`
- **Channel selection for marketing:** `twilio-marketing-promotions-advisor`
- **Channel selection for notifications:** `twilio-notifications-alerts-advisor`
