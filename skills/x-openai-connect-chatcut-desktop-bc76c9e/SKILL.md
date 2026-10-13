---
name: x-openai-connect-chatcut-desktop-bc76c9e
description: Install, open, connect, or repair ChatCut Desktop when the chatcut_desktop MCP tools are missing or unavailable. Do not use from a managed agent already running inside ChatCut Desktop, or when chatcut_desktop tools are already available.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Connect ChatCut Desktop

Use the signed production Desktop app as the only source of the local MCP server
and editing skills. This plugin contains instructions only, not an installer or
MCP configuration.

If `chatcut_desktop` tools are already available, call `get_active_project` and
continue with the user's editing request. Do not reinstall the app or change MCP
configuration. If the current host is ChatCut Desktop's managed Codex agent,
stop; its project-pinned MCP and built-in skills are already authoritative.

## Download

Use only the matching official URL:

- macOS Apple Silicon: `https://api.chatcut.io/desktop/download/macos`
- macOS Intel: `https://api.chatcut.io/desktop/download/macos-x64`
- Windows x64: `https://api.chatcut.io/desktop/download/windows`

ChatCut Desktop supports macOS 13 or newer on Apple Silicon or Intel and Windows
on x64. Linux is unsupported. Do not substitute a search result, third-party
mirror, hosted ChatCut MCP, or historical `chatcut@chatcut-inc` plugin.

## Install or repair

Try to complete the ordinary platform installation for the user with the host's
narrow command approval:

1. Detect the operating system and architecture and choose the URL above.
2. Download the official artifact to a temporary directory. If ChatCut is
   already installed but will not open, inspect it before replacing it.
3. On macOS, use native tools to mount a DMG or extract a ZIP, then copy
   `ChatCut.app` to `/Applications` or the user's `Applications` directory. On
   Windows, open the downloaded installer and let the visible installer finish.
4. Open ChatCut Desktop. It registers `chatcut_desktop` and synchronizes its
   editing skills into supported integrations (including Codex) automatically. In TRAE or Claude, inspect the actual available MCP tools after launch. Do not assume this registration reached the current host or invent a connection URL; if absent, use ChatCut's official connection UI/documentation or report the integration as unavailable.

Installing outside the project sandbox or opening an installer may require host
approval. Request only the scoped operation needed for that step; never ask the
user to enable persistent Full access.

For macOS launch or code-signing failures, inspect `codesign`, Gatekeeper,
permissions, and quarantine state. Try remounting or re-extracting a fresh
official download, fixing destination permissions, or clearing stale quarantine
only after the official app's signature validates. Never modify or ad-hoc sign
the app, disable Gatekeeper, or bypass an invalid signature. On Windows, do not
bypass an invalid or unknown Authenticode publisher warning.

Retry one fresh official download if the artifact is incomplete, corrupt, for
the wrong architecture, or fails a normal copy or extraction step. Do not loop.

## User handoff

If the host cannot download, mount, extract, copy, approve, repair, or run the
installer, stop trying. Tell the user what blocked automation and give them the
exact matching official URL above so they can install and open ChatCut with the
visible operating-system flow.

After ChatCut opens, ask the user to sign in there if needed. Do not handle their
credentials or add `chatcut_desktop` to `config.toml` manually. Follow the current host's documented MCP reload/reconnect behavior after Desktop finishes connecting. In Codex, a new task may be needed; do not assume the same lifecycle in TRAE or Claude.
