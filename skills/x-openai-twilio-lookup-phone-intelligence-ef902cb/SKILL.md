---
name: x-openai-twilio-lookup-phone-intelligence-ef902cb
description: Look up phone number intelligence via Twilio Lookup v2 API. Covers number validation, line type detection (mobile/landline/VoIP), SIM swap detection, caller name, identity match, and SMS pumping risk scoring. Use this skill to validate numbers or assess fraud risk before sending messages or calls.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

Twilio Lookup validates phone numbers and provides optional intelligence packages. Basic validation is free; data packages (line type, SIM swap, etc.) are paid per lookup.

---

## Prerequisites

- Twilio account (free trial works for basic lookups)
  — New to Twilio? See `twilio-account-setup`
- Environment variables:
  - `TWILIO_ACCOUNT_SID`
  - `TWILIO_AUTH_TOKEN`
  — See `twilio-iam-auth-setup` for credential setup and best practices
- SDK: `pip install twilio` / `npm install twilio`

---

## Quickstart

**Python**
```python
import os
from twilio.rest import Client

client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

phone = client.lookups.v2.phone_numbers("+15108675310").fetch()

print(phone.valid)            # True / False
print(phone.phone_number)     # +15108675310 (E.164)
print(phone.national_format)  # (510) 867-5310
print(phone.country_code)     # US
```

**Node.js**
```node
const twilio = require("twilio");
const client = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

const phone = await client.lookups.v2.phoneNumbers("+15108675310").fetch();

console.log(phone.valid);
console.log(phone.phoneNumber);
console.log(phone.nationalFormat);
```

If `valid` is `false`, check `phone.validationErrors` for the reason.

---

## Key Patterns

### Line Type Intelligence (paid)

Identifies mobile, landline, VoIP, toll-free, etc.

**Python**
```python
phone = client.lookups.v2.phone_numbers("+15108675310").fetch(
    fields="line_type_intelligence"
)
print(phone.line_type_intelligence)
# {'type': 'mobile', 'carrier_name': 'T-Mobile USA', ...}
```

**Node.js**
```node
const phone = await client.lookups.v2.phoneNumbers("+15108675310").fetch({
    fields: "line_type_intelligence",
});
console.log(phone.lineTypeIntelligence);
```

Line types: `mobile`, `landline`, `voip`, `toll-free`, `fixedVoip`, `nonFixedVoip`, `personal`, `payphone`, `unknown`

### Multiple Packages in One Request

**Python**
```python
phone = client.lookups.v2.phone_numbers("+15108675310").fetch(
    fields="line_type_intelligence,sim_swap,caller_name"
)
```

**Node.js**
```node
const phone = await client.lookups.v2.phoneNumbers("+15108675310").fetch({
    fields: "line_type_intelligence,sim_swap,caller_name",
});
```

### Validate Before Sending

**Python**
```python
phone = client.lookups.v2.phone_numbers("+invalid").fetch()
if not phone.valid:
    print(f"Invalid number: {phone.validation_errors}")
    # Handle gracefully — do not attempt to send
```

**Node.js**
```node
const phone = await client.lookups.v2.phoneNumbers("+invalid").fetch();
if (!phone.valid) {
    console.log("Invalid number:", phone.validationErrors);
}
```

### Available Data Packages

| Package | `fields` value | Coverage | Use case |
|---------|---------------|----------|----------|
| Line Type Intelligence | `line_type_intelligence` | Worldwide | Route by line type; block VoIP |
| Caller Name | `caller_name` | US only | Show caller ID |
| SIM Swap | `sim_swap` | Select regions | Fraud detection |
| Identity Match | `identity_match` | Select regions | Verify ownership |
| SMS Pumping Risk | `sms_pumping_risk` | Worldwide | Fraud prevention |
| Reassigned Number | `reassigned_number` | US only | Check if recycled |

---

## Common Errors

| Code | Meaning | Fix |
|------|---------|-----|
| 20404 | Phone number not found | Number may be invalid or unsupported format |
| 60601 | Data package not available for this region | Check regional coverage before requesting package |

---

## CANNOT

- **Cannot look up by name or address** — Input is always a phone number. No reverse search.
- **Cannot get caller_name for non-US numbers** — Returns error 60600 (out of coverage).
- **Cannot detect conditional call forwarding** — Only unconditional forwarding is detected, and only for UK carriers.
- **Cannot guarantee SIM swap data without carrier registration** — Returns error 60606 until carrier approval is in place.
- **Cannot use Reassigned Number outside the US** — US-only dataset with monthly update cadence.
- **Cannot get real-time SMS pumping scores** — Scores are statistical models, not live traffic analysis.
- **Cannot write data** — Lookup v2 is read-only (GET only). The one exception is Line Type Override (POST/DELETE).
- **Cannot batch multiple phone numbers in one request** — One number per API call. Loop for bulk lookups.
- **Cannot avoid billing on caller_name requests that return no data** — Billed per request regardless of whether data is returned.
- **Cannot use Phone Number Quality Score or Pre-fill without provisioning** — Returns 60606. Contact Twilio sales to enable.
- **Cannot guarantee deliverability from a valid lookup** — A valid number may still be unreachable (carrier issues, ported, etc.)

---

## Next Steps

- **Send SMS after validation:** `twilio-sms-send-message`
- **Send OTP after validation:** `twilio-verify-send-otp`
