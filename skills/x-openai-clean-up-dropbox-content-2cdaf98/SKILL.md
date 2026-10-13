---
name: x-openai-clean-up-dropbox-content-2cdaf98
description: Clean up Dropbox content by identifying obsolete, duplicate, temporary, or unwanted files and deleting only after explicit review. Use when the user explicitly asks to delete, remove, or clean up Dropbox files or folders.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Clean Up Dropbox Content

Use this skill for careful deletion workflows in Dropbox.

## Tools

- `search`
- `list_folder`
- `get_file_metadata`
- `list_shared_links`
- `copy`
- `delete`
- `check_job_status`

## Workflow

1. Confirm the cleanup goal and scope.
2. Use `search` or `list_folder` to identify candidate content.
3. Use `get_file_metadata` to verify each deletion candidate.
4. Use `list_shared_links` when deleting shared content could affect others.
5. If the user may need rollback context, explain that the current Dropbox MCP tools do not expose revision listing or restore operations.
6. If the user wants to preserve a copy first, confirm the exact destination, call `copy`, and use `check_job_status` for any asynchronous copy job until it completes successfully.
7. After any requested copy has completed successfully, present a deletion review list and ask for explicit confirmation.
8. Call `delete` only for the exact confirmed items.
9. Use `check_job_status` for any asynchronous copy or deletion job until it completes or must be reported as pending.
10. Report every copied, deleted, skipped, pending, or failed item.

## Confirmation Required

Before deleting anything, confirm:

- Exact paths or stable identifiers
- Whether each item is a file or folder
- Whether the item appears shared
- Why it is safe to delete
- Exact copy destination, if the user wants to preserve a copy first

## Output

Before deletion, present:

- Candidate path
- Type
- Modified time when available
- Sharing status when relevant
- Copy destination when preserving a copy first
- Reason it appears safe to delete

After deletion, present:

- Copied items when relevant
- Deleted items
- Pending items and job status when relevant
- Failed items and reason
- Items skipped because they were ambiguous or risky

## Safety

Never delete based only on a broad pattern like "old files" or "duplicates" without listing exact targets. Never delete a parent folder when the user confirmed only child files. If confidence is not high, stop and ask the user to choose.

## Good Triggers

- "Delete these Dropbox files."
- "Clean up duplicate PDFs in this folder."
- "Remove obsolete draft files."
- "Delete temporary exports from Dropbox."

## Do Not Use When

- The user wants to move content to an archive. Use `organize-dropbox-folder`.
- The user wants to recover content. Explain that recovery is unavailable until the Dropbox restore tool is exposed.
- The user only wants a list of cleanup candidates and no deletion. Use `find-dropbox-content` or `inspect-dropbox-file`.
