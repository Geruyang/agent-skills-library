---
name: x-openai-inspect-dropbox-file-b92b791
description: Inspect a Dropbox file or folder by checking metadata, shared links, and file content when needed. Use when the user asks what a file is, whether it is shared, when it changed, what access links exist, or asks to read/analyze a Dropbox file.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## Reviewed capability mapping (TRAE / Claude)

Discover Dropbox metadata, search/list, download/fetch, and shared-link inspection through the current MCP catalog or documented Dropbox API. Tool names below identify operations; use the actual exposed names and schemas. Keep this workflow read-only. Missing access to an operation blocks that operation, not a fabricated fallback or mutation.

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Inspect Dropbox File

Use this skill to understand a Dropbox file or folder before summarizing, comparing, sharing, restoring, or organizing it.

## Tools

- `get_file_metadata`
- `fetch`
- `list_shared_links`
- `get_shared_link_metadata`
- `search`
- `list_folder`

## Workflow

1. Identify the target file or folder from the user request.
2. If the target is ambiguous, use `search` or `list_folder` to find likely matches.
3. Call `get_file_metadata` for the chosen item.
4. If the user asks about content, summary, extraction, or analysis, use `fetch` for files.
5. If the user asks about version history or rollback options, inspect the connected Dropbox tool catalog for revision-listing support. Use an authorized read-only equivalent when available; otherwise report the missing revision-listing capability. Restoration remains outside this read-only workflow.
6. If the user asks about sharing or access, use `list_shared_links`; continue while the response indicates has_more or returns a cursor before claiming the shared-link listing is complete.
7. If the user provides a Dropbox shared link or asks about a specific link, use `get_shared_link_metadata`.

## Output

Summarize only the details relevant to the user request. Include:

- Name and path
- File or folder type
- Size and modified time when available
- Sharing/link status when relevant, including whether shared-link pagination is complete
- Version-history limitation when relevant
- Fetched content summary when relevant
- Recommended next action, if the user asked for one

## Safety

This is a read-only workflow. Do not create links, change sharing, copy, move, delete, or restore content. If the user asks for a mutation, explain the intended action and switch to the relevant Dropbox skill.

## Good Triggers

- "What is this Dropbox file?"
- "Summarize this file."
- "Check whether this folder is shared."
- "Show me the revision history."
- "When was this document last updated?"

## Do Not Use When

- The user only wants to search or browse. Use `find-dropbox-content`.
- The user wants to create a shared link or inspect shared-link state. Use `share-dropbox-content`.
- The user wants to add viewers or share directly with named recipients. Explain that recipient-sharing is unavailable until the required MCP tools are exposed.
- The user wants to restore a revision. Explain that recovery is unavailable until the Dropbox restore tool is exposed.
