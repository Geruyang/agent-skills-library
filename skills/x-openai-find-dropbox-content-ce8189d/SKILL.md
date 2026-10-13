---
name: x-openai-find-dropbox-content-ce8189d
description: Find Dropbox files and folders relevant to a user request. Use when the user asks to search Dropbox, find a document, locate recent files, browse a folder, identify likely source files, or narrow down where content lives before reading, sharing, organizing, or restoring it.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Find Dropbox Content

Use this skill to locate relevant Dropbox files and folders without changing anything.

## Tools

Discover authenticated Dropbox search, folder-listing, and metadata operations. The names `search`, `list_folder`, and `get_file_metadata` below are reference names. Bind them to actual MCP/CLI/API schemas, including separate continuation endpoints when required. If required access is missing, stop that operation and report the dependency.

## Workflow

1. Clarify the search target only if the user request is too broad to act on.
2. Use `search` for broad keyword, title, file type, or natural-language searches.
3. When `search` returns a cursor and more results are needed, use the discovered search-continuation operation and documented cursor arguments.
4. Use `list_folder` with `recursive=false` when the user names a folder or wants to browse a location.
5. When `list_folder` returns a cursor and more folder results are needed, use the discovered folder-continuation operation and documented cursor arguments.
6. Use `get_file_metadata` for strong candidates before presenting a final recommendation.

## Output

Return the best matches first. For each result, include:

- Name
- Object type: file or folder
- Path or stable identifier
- Modified time when available
- Why it matched the request
- Any ambiguity or confidence caveat

## Safety

Do not create, copy, move, delete, restore, download, or share content. If the user asks to take one of those actions after finding content, resolve the relevant installed Dropbox skill or verified capability.

## Good Triggers

- "Find the Q4 planning deck in Dropbox."
- "Search Dropbox for onboarding docs."
- "What files are in this folder?"
- "Find recent PDFs about the launch plan."
- "Where is the customer contract?"

## Do Not Use When

- The user already provided an exact file and wants its content inspected. Resolve an installed inspection skill or authorized Dropbox content-reading capability.
- The user explicitly asks to create a shared link. Resolve an installed sharing skill or verified Dropbox shared-link operation.
- The user asks to add viewers or share directly with named recipients. Explain that recipient-sharing is unavailable until an authorized Dropbox MCP/API capability for that action is available.
- The user asks to restore or recover content. Explain that recovery is unavailable until an authorized Dropbox restore operation is available.
