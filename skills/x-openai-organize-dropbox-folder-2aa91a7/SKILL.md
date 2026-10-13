---
name: x-openai-organize-dropbox-folder-2aa91a7
description: Organize Dropbox files and folders by creating folders, copying content, or moving content into a cleaner structure. Use when the user asks to organize, archive, consolidate, restructure, copy, or move Dropbox content.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Organize Dropbox Folder

Use this skill to safely organize Dropbox content through folder creation, copying, and moving.

## Tools

- `list_folder`
- `search`
- `get_file_metadata`
- `create_folder`
- `copy`
- `move`
- `check_job_status`

## Workflow

1. Understand the desired organization goal and target scope.
2. Use `list_folder` or `search` to inventory the relevant content.
3. Use `get_file_metadata` for items that may be moved or copied.
4. Draft a proposed change plan before any mutation.
5. If needed, create destination folders with `create_folder` after confirmation.
6. Use `copy` when preserving the original location matters or when the user says copy/duplicate.
7. Use `move` only when the user explicitly wants content relocated or archived.
8. Use `check_job_status` for any asynchronous copy or move job until it completes or must be reported as pending.
9. After changes, summarize all created, copied, moved, and pending paths.

## Confirmation Required

Before any mutation, confirm:

- Source paths
- Destination paths
- Whether the operation is copy or move
- Whether destination folders should be created
- Expected result after the operation

## Output

Before mutation, present a plan:

- Folders to create
- Files or folders to copy
- Files or folders to move
- Items that need clarification

After mutation, report:

- Successfully created folders
- Successfully copied items
- Successfully moved items
- Pending jobs and current status when relevant
- Any failures or skipped items

## Safety

Prefer copy over move when the user intent is ambiguous. Do not move shared folders or high-level team folders without extra confirmation. Do not delete anything; use `clean-up-dropbox-content` only when deletion is explicitly requested.

## Good Triggers

- "Organize these files into folders by client."
- "Archive last year's project folder."
- "Copy these assets into the launch folder."
- "Move all final PDFs into the Final folder."

## Do Not Use When

- The user only wants to search or inspect content. Use `find-dropbox-content` or `inspect-dropbox-file`.
- The user asks to delete content. Use `clean-up-dropbox-content`.
- The user asks to restore content. Explain that recovery is unavailable until the Dropbox restore tool is exposed.
