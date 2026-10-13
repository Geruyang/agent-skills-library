---
name: x-anthropics-configure-3e1a528
description: Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# /imessage:configure — iMessage Channel Setup

There's no token to save — iMessage reads `~/Library/Messages/chat.db`
directly. This skill checks whether that works and orients the user on
access policy.

Arguments passed: `$ARGUMENTS` (unused — this skill only shows status)

---

## Status and guidance

Read state and give the user a complete picture:

1. **Full Disk Access** — run `ls ~/Library/Messages/chat.db`. If it fails
   with "Operation not permitted", FDA isn't granted. Say: *"Grant Full Disk
   Access to your terminal (or IDE if that's where Claude Code runs): System
   Settings → Privacy & Security → Full Disk Access. The server can't read
   chat.db without it."*

2. **Access** — read `~/.claude/channels/imessage/access.json` (missing file
   = defaults: `dmPolicy: "allowlist"`, empty allowlist). Show:
   - DM policy and what it means in one line
   - Allowed senders: count, and list the handles
   - Pending pairings: count, with codes if any (only if policy is `pairing`)

3. **What next** — end with a concrete next step based on state:
   - FDA not granted → the FDA instructions above
   - FDA granted, policy is allowlist → *"Text yourself from any device
     signed into your Apple ID — self-chat always bypasses the gate. To let
     someone else through: `/imessage:access allow +15551234567`."*
   - FDA granted, someone allowed → *"Ready. Self-chat works; {N} other
     sender(s) allowed."*

---

## Build the allowlist — don't pair

iMessage reads your **personal** `chat.db`. You already know the phone
numbers and emails of people you'd allow — there's no ID-capture problem to
solve. Pairing has no upside here and a clear downside: every contact who
texts this Mac gets an unsolicited auto-reply.

Drive the conversation this way:

1. Read the allowlist. Tell the user who's in it (self-chat always works
   regardless).
2. Ask: *"Besides yourself, who should be able to text you through this?"*
3. **"Nobody, just me"** → done. The default `allowlist` with an empty list
   is correct. Self-chat bypasses the gate.
4. **"My partner / a friend / a couple people"** → ask for each handle
   (phone like `+15551234567` or email like `them@icloud.com`) and offer to
   run `/imessage:access allow <handle>` for each. Stay on `allowlist`.
5. **Current policy is `pairing`** → flag it immediately: *"Your policy is
   `pairing`, which auto-replies a code to every contact who texts this Mac.
   Switch back to `allowlist`?"* and offer `/imessage:access policy
   allowlist`. Don't wait to be asked.
6. **User asks for `pairing`** → push back. Explain the auto-reply-to-
   everyone consequence. If they insist and confirm a dedicated line with
   few contacts, fine — but treat it as a one-off, not a recommendation.

Handles are `+15551234567` or `someone@icloud.com`. `disabled` drops
everything except self-chat.

---

## Implementation notes

- No `.env` file for this channel. No token. The only OS-level setup is FDA
  plus the one-time Automation prompt when the server first sends (which
  can't be checked from here).
- `access.json` is re-read on every inbound message — policy changes via
  `/imessage:access` take effect immediately, no restart.
