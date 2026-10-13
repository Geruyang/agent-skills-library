---
name: x-openai-publish-artifact-to-sites-3c24489
description: Publish a validated Data Analytics report or dashboard artifact through Sites. Use automatically for durable artifacts in any positively identified Work Mode when the full Sites lifecycle is callable, or in ChatGPT Desktop outside Work Mode only after an explicit Sites request or acceptance of the optional post-handoff sharing offer.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Publish Artifact To Sites

Use this skill after the report or dashboard workflow produces a complete canonical manifest and bounded snapshot and `validate_artifact` succeeds. It publishes the Data Analytics reader runtime as a Sites-hosted snapshot; it does not add live source connections to the Site.

## Routing Contract

- In any positively identified Work Mode, a durable report or dashboard request selects Sites automatically when the full Sites building and hosting lifecycle is callable. Do not ask for another delivery choice or publish confirmation.
- In ChatGPT Desktop outside Work Mode, use this skill only after the user explicitly requests Sites or explicitly accepts the optional coworker-sharing offer made after a successful final MCP artifact handoff. A report or dashboard request alone does not authorize publishing there.
- If the full Sites lifecycle is not callable in Work Mode, use the self-contained HTML fallback selected by the owning report or dashboard workflow.

For TRAE, Claude, or any runtime outside the positively identified Work Mode branches, use this publishing workflow only for an explicit Sites publish request and only after discovering authenticated Sites tools for the complete lifecycle. If unavailable, report the missing publishing capability; retain the validated local artifact and follow the consent rules below for any alternative delivery.

## Workflow

1. Confirm that `$sites-building` and `$sites-hosting` are both callable for the full Sites create, checkpoint, and deployment lifecycle.
2. Invoke `$sites-building` to create or reopen one worker-starter checkout per logical report or dashboard. For a new Site, select the worker starter (`--starter worker`). Reuse that Site for later versions.
3. Read the Site's current access policy with the Sites connector. Treat a workspace Site as verifiably owner-only only when it is `custom`, has exactly one `allowed_account_user_id`, its sole `allowed_users` entry has the same account-user id and a non-empty email, and it has no allowed groups. If the user asked to widen reader access, defer that access change until after the package is exported so the verified creator seed is not lost. Do not infer a creator from an already-shared reader allowlist.
4. Call `export_artifact_package` with the validated payload, the Sites project id in the compatibility field `site_creator_project_id`, and the returned checkout path as `output_dir`. When the current workspace policy is verifiably owner-only, pass its sole resolved email as `site_editor_email`; the exporter hashes it before writing source. Otherwise omit the field so an existing editor seed or explicit disabled state is preserved. Pass `site_editor_email: null` only when the user explicitly asks to disable presentation editing. After export succeeds, apply any reader-access change the user explicitly requested, then checkpoint and deploy with the same approval boundary.
5. Verify that every returned source/schema/hosting path is inside the checkout, and separately verify that the hosting metadata contains the resolved project id. Presentation editing requires the logical D1 binding `DB`; do not replace another binding name. A read-only export may omit `database_schema_path`.
6. Checkpoint the checkout through `$sites-building`, then invoke `$sites-hosting` to poll the deployment to a terminal state.
7. Return the Sites URL and artifact snapshot timestamp, and state that the published data is a snapshot rather than a live connection. When presentation editing is enabled, state that only the seeded creator can edit title/text/layout, delete blocks, or launch refresh and export handoffs; saved presentation overrides remain in Sites rather than syncing back to ChatGPT Desktop.

## Fallbacks And Failures

- If the full Sites lifecycle is unavailable or publishing fails after one targeted retry in Work Mode, automatically switch to the owning workflow's self-contained HTML mode, state the failed stage briefly, and do not claim that a Site was published.
- If the user explicitly requested only Sites, report the blocker instead of switching surfaces without their consent.
