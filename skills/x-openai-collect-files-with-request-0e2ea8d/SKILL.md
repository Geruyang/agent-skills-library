---
name: x-openai-collect-files-with-request-0e2ea8d
description: Create, inspect, and manage Dropbox file requests for collecting uploads from other people. Use when the user asks to collect files, request uploads, create an upload portal, check a file request, or list existing file requests.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Collect Files With Request

Use this skill to help users collect files from others through Dropbox file requests.

## Tools

First discover the connected Dropbox capabilities and inspect their schemas. The names below identify the required operations; they may have different names in another MCP connector. A verified authenticated Dropbox API/CLI route is also acceptable when it supports the same file-request operation, destination checks, and confirmation gates. If no such route is available, provide a local request specification and manual setup steps, explicitly stating that no upload link or folder was created. Never fabricate an ID, URL, or completed request.

- `create_file_request`
- `get_file_request`
- `list_file_requests`
- `create_folder`
- `get_file_metadata`
- `list_folder`

## Workflow

1. Determine whether the user wants to create a new file request, inspect one request, or list existing requests.
2. For a new request, identify the destination folder.
3. Do not use a team root, such as `/`, or the user's personal root, such as `/FirstName LastName`, as the destination. Dropbox requires the file request destination to be a child folder under that folder, such as `/FirstName LastName/Invoices`.
4. If the requested destination is a team root or the user's personal root, ask the user to confirm a child folder under that folder.
5. If the destination folder does not exist and the user wants it created, use `create_folder` only after explicit confirmation.
6. Before calling `create_file_request`, confirm the title, destination folder, deadline if applicable, and whether the request should be open or closed if that option is available.
7. Use `get_file_request` for a known raw request ID.
8. Use `list_file_requests` when the user asks for existing requests or cannot identify one.
9. After creating or finding a request, explain the request URL and where uploaded files will land.

## Confirmation Required

Before creating a file request, confirm:

- Request title
- Destination folder, confirmed to be a child folder under any requested team root or the user's personal root
- Deadline, if requested
- Any access or open/closed setting supported by the tool

Before creating a destination folder, confirm:

- Exact folder path
- Whether parent folders already exist
- That the folder is not a team root, such as `/`, or the user's personal root

## Output

Return:

- File request title
- Request URL or identifier
- Destination folder
- Status
- Deadline, if any
- Any action the user still needs to take

## Safety

Do not create folders or file requests without explicit confirmation. Do not assume uploaded files are private or reviewed; describe the destination and access implications clearly. Dropbox does not allow file requests at a team root, such as `/`, or the user's personal root; ask the user to confirm a child folder under that folder and do not retry with a guessed folder.

## Good Triggers

- "Create a Dropbox file request for vendor invoices."
- "Make an upload link for candidates to submit portfolios."
- "Show my open file requests."
- "Check the status of this file request."

## Do Not Use When

- The user wants to share existing content. Use `share-dropbox-content`.
- The user wants to organize existing files. Use `organize-dropbox-folder`.
- The user wants to recover deleted files. Route to a separately discovered Dropbox restore capability; if none is available, explain the missing capability without claiming recovery.
