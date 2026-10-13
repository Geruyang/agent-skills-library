---
name: x-openai-share-dropbox-content-5437ab8
description: Share Dropbox files or folders by creating shared links, inspecting existing shared links, or explaining current shared-link state. Use only when the user explicitly asks to create a shared link, check access, or inspect a Dropbox shared link.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Share Dropbox Content

Use this skill to create or inspect Dropbox shared links and explain shared-link state.

## Tools

- `create_shared_link`
- `list_shared_links`
- `get_shared_link_metadata`
- `get_file_metadata`
- `search`
- `list_folder`

## Workflow

1. Identify the target file or folder.
2. If the target is ambiguous, use `search` or `list_folder` and ask the user to choose.
3. Use `get_file_metadata` to confirm the exact target.
4. Use `list_shared_links` when checking current sharing state or before creating a new link if existing links matter; continue while the response indicates has_more or returns a cursor before treating the existing-link state as complete.
5. Use `get_shared_link_metadata` when the user provides or asks about a specific shared link.
6. Before calling `create_shared_link`, summarize the exact sharing plan and ask for explicit confirmation.
7. After sharing, report the resulting URL, effective access settings, and any warnings or partial failures.
8. If the user asks to add viewers, add recipients, or share directly with named people, explain that recipient-sharing is unavailable until those MCP tools are available. Offer to create a shared link instead when appropriate.

## Confirmation Required

Before creating a shared link, confirm:

- Exact target file or folder
- Link/access settings requested by the user
- Expiration, password, or download settings when supported

## Output

After a successful action, include:

- Shared link URL
- Whether the link was newly created or reused
- Effective access settings
- Any warning that existing link settings differ from requested settings
- Whether shared-link pagination was complete when existing links were checked

## Safety

Never create a link automatically after finding, downloading, or creating content. Do not claim access was granted to named recipients or viewers; recipient-sharing tools are not available.

## Good Triggers

- "Create a share link for this Dropbox folder."
- "Create a link to this file."
- "Check who can access this Dropbox link."
- "Send me a share link for the launch deck."

## Do Not Use When

- The user only wants to find a file. Use `find-dropbox-content`.
- The user only wants metadata or content summary. Use `inspect-dropbox-file`.
- The user wants to collect uploads from others. Use `collect-files-with-request`.
- The user wants to add viewers or share directly with named recipients. Explain that recipient-sharing is unavailable until the required MCP tools are exposed.
