---
name: x-openai-twilio-sendgrid-engagement-quality-75891ed
description: Monitor email program health with SendGrid Engagement Quality (SEQ) scores. Covers the SEQ API endpoints, the 5 scoring metrics (engagement recency, open rate, bounce classification, bounce rate, spam rate), eligibility requirements, and interpreting scores for deliverability improvement. Use when diagnosing SendGrid deliverability issues or monitoring sender reputation. Requires a SendGrid API key (SG.-prefix) — not applicable to the Twilio Email API (comms.twilio.com).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Overview

SendGrid Engagement Quality (SEQ) scores measure how "wanted" your email is by recipients. Higher scores (1-5 scale) correlate with better inbox placement. SEQ is a diagnostic tool — it tells you where your email program is healthy and where it needs improvement.

**Key insight:** SEQ scores are correlated with deliverability. A higher score means more emails land in inboxes, not spam folders.

---

## Eligibility Requirements

Your account must meet ALL conditions to receive scores:
1. **Pro or Premier Email API plan** — SEQ is not available on Free or Essentials plans
2. **Open tracking enabled** in SendGrid settings
3. **Minimum 1,000 messages sent** in the previous 30 days

If not eligible, the `score` and `metrics` fields are omitted from API responses entirely.

---

## The 5 Metrics

All scores range from **1 (poor) to 5 (excellent)**.

| Metric | What it measures | How to improve |
|--------|-----------------|---------------|
| **engagement_recency** | Are you sending to an engaged audience? Based on how regularly messages are opened and clicked. | Remove inactive subscribers. Implement re-engagement campaigns before pruning. |
| **open_rate** | Degree to which your audience opens your messages. | Improve subject lines. Segment audiences by engagement level. |
| **bounce_classification** | Rejection by mailbox providers due to reputation or spam-like content. | Fix content triggering spam filters. Warm IPs properly. Monitor domain reputation. |
| **bounce_rate** | Are you sending to addresses that don't exist? Based on permanent bounces to invalid mailboxes. | Implement double opt-in. Clean lists quarterly. Use Email Validation API before sending. |
| **spam_rate** | Are recipients marking your email as spam? Based on recipients who open then report spam. | Only send to opted-in recipients. Make unsubscribe easy. Match content to expectations set at signup. |

**Note:** The overall `score` is NOT a simple average of the 5 metrics — the weighting formula is opaque. A single low metric (e.g., spam_rate = 1) can drag the overall score significantly.

---

## API Endpoints

### Get Your Scores (Date Range)

`GET /v3/engagementquality/scores`

| Parameter | Required | Description |
|-----------|----------|-------------|
| `from` | Yes | Start date (YYYY-MM-DD, UTC) |
| `to` | Yes | End date (YYYY-MM-DD, UTC) |

**Python**
```python
import os, requests

headers = {"Authorization": f"Bearer {os.environ['SENDGRID_API_KEY']}"}
response = requests.get(
    "https://api.sendgrid.com/v3/engagementquality/scores",
    params={"from": "2026-04-01", "to": "2026-04-23"},
    headers=headers
)

if response.status_code == 200:
    for entry in response.json()["result"]:
        print(f"Date: {entry['date']}, Score: {entry.get('score', 'N/A')}")
        metrics = entry.get("metrics", {})
        for metric, value in metrics.items():
            print(f"  {metric}: {value}")
elif response.status_code == 202:
    print("Scores not yet calculated — try again later")
```

### Get Subuser Scores (Single Date)

`GET /v3/engagementquality/subusers/scores`

| Parameter | Required | Description |
|-----------|----------|-------------|
| `date` | Yes | Date (YYYY-MM-DD, UTC) |
| `limit` | No | Results per page (default 1000, max 1000) |
| `after_key` | No | Pagination cursor |

Returns paginated results with `_metadata.next_params.after_key` for pagination.

---

## Response Patterns

**200 OK** — Scores available:
```json
{
    "result": [{
        "user_id": "12345",
        "username": "myaccount",
        "date": "2026-04-22",
        "score": 4,
        "metrics": {
            "engagement_recency": 4,
            "open_rate": 5,
            "bounce_classification": 3,
            "bounce_rate": 4,
            "spam_rate": 5
        }
    }]
}
```

**202 Accepted** — Scores are calculated asynchronously. Not yet available for the requested date. Retry later.

**Score or metrics omitted** — Account/subuser is not eligible (open tracking off or <1,000 sends in 30 days).

---

## CANNOT

- **Cannot get scores without open tracking enabled** — This is a hard prerequisite. No tracking = no score.
- **Cannot get scores with fewer than 1,000 messages in 30 days** — Low-volume senders are ineligible.
- **Cannot query more than 90 days in the past** — Date range is limited to the last 90 days.
- **Cannot get real-time scores** — Scores are calculated asynchronously (daily). A `202` response means "not ready yet."
- **Cannot determine the exact weighting formula** — The overall score is not a simple average. Individual metric weights are not published.
- **Email Validation API is a separate paid feature** — Referenced in bounce_rate improvement guidance, but requires Pro or Premier plan. Not included in base plan.
- **Subuser endpoint accepts only a single date** — Not a date range. Query one day at a time.

---

## Next Steps

- **Improve bounce rate:** `twilio-sendgrid-suppressions`
- **Track delivery events:** `twilio-sendgrid-webhooks`
- **Account setup:** `twilio-sendgrid-account-setup`
