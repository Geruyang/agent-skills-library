---
name: x-openai-migrate-to-codex-ac311db
description: Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Migrate to Codex

## Autonomy

Keep going until the selected migration is completely done: run the migrator, inspect the report, fix migrated Codex instructions/skills/agents/MCP config, and re-run checks without stopping to ask for confirmation of the next step. If the user has selected a target, do not ask before creating, editing, replacing, or deleting generated Codex artifacts in that target (`AGENTS.md`, `.codex/`, `.agents/`, or `~/.codex/`). Preserve unrelated existing Codex config entries in `.codex/config.toml` or `~/.codex/config.toml`, such as `notify`, `projects`, `marketplaces`, or unrelated MCP servers; do not ask about them unless they fail validation or directly conflict with the migration. Do not edit source Claude Code files (`.claude/`, `~/.claude/`, `.mcp.json`, or `.claude.json`), unrelated project code, secrets, or another repository.

## Migration Order

Run the migration in this order for each selected global or project source:

1. Track the migration with the current host's available task-list capability, using its documented schema; if none is available, maintain the checklist in the conversation. Do not create `MIGRATION_TODOS.md` or any TODO file unless the user explicitly asks. Track pending, active, and completed work and make the tasks specific to the selected artifacts. Before finishing, mark every finished step complete. Use literal source → Codex target labels, for example:
   - Inspect `.claude/commands` → Codex skills/prompts
   - Inspect `.claude/agents` → `.codex/agents`
   - Inspect `.mcp.json` → `.codex/config.toml` MCP servers
   - Inspect `.claude/settings.json` hooks → `.codex/hooks.json`
   - Migrate safe selected artifacts → Codex files
   - Validate generated `.codex/config.toml`
   - Validate generated `.codex/agents`
   - Report migrated artifacts and manual-review items

2. Read `references/differences.md` (and refresh Codex docs if its `Docs last checked` date is old).

3. Scan and inspect before writing:
   - `--scan-only` lists active and inactive source surfaces.
   - `--plan` prints staged Codex artifact paths and report rows.
   - `--doctor` summarizes readiness, manual-review work, and validation risks.

4. Convert surfaces in the same order the CLI uses:
   - instructions: `CLAUDE.md` / `AGENTS.md` to `AGENTS.md`
   - plugins: report Claude plugin trees and marketplaces as manual migration work
   - hooks: rewrite supported Claude hooks into `.codex/hooks.json` and enable `[features].codex_hooks = true`
   - skills and commands: write Codex skills under `.agents/skills/`
   - config: write `.codex/config.toml` from Claude model/sandbox settings and MCP servers, including `personality = "friendly"` when config is generated
   - subagents: write Codex custom agents under `.codex/agents/`

5. Dry-run, then write the selected target. Use `--replace` only when orphan generated skills or agents should be deleted.

6. Inspect the terminal output and `.codex/migrate-to-codex-report.txt` after real runs.

7. Review generated artifacts in this order: `AGENTS.md`, `.agents/skills/`, `.codex/config.toml`, `.codex/hooks.json`, `.codex/agents/`, then report-only plugin items.

8. Run `--validate-target` against each target after edits.

9. Re-run checks and `--dry-run` after edits.

10. Return the final migration report as one markdown table per scope that has rows. The tables cover only the non-native follow-up migration work you performed, such as skills created from slash commands, subagents, MCP servers, hooks, unsupported/local plugin notes, and manual-review caveats. Include programmatic native import rows for config, instructions, skills, or supported plugins only if you personally migrated them in this follow-up run.

    If only one scope has rows, render only the table with no heading. If multiple scopes have rows, render one heading before each table. Use `**User Config**` for user-scope rows. For project-scope rows, use the actual project folder name as the heading, for example `**northstar-support-portal**`; do not use `Current Project` as the heading. Do not add prose before or after the table output.

    Use exactly these columns:

    **northstar-support-portal**

    | Status | Item | Notes |
    | --- | --- | --- |
    | `Added` | `Slash command` pr-review | Converted into a Codex skill |
    | `Added` | `Subagent` release-lead | Added as a Codex subagent |
    | `Check before using` | `Hook` PreToolUse | Converted, but some Claude hook behavior differs in Codex |
    | `Not Added` | `Hook` Notification | Codex does not have an equivalent notification hook |
    | `Not Added` | `Plugin` team-macros | Plugin needs manual setup |

    `Status` must be `Added`, `Check before using`, or `Not Added`. Use `Added` when a Codex-facing artifact was created or changed and needs no special review. Use `Check before using` when a Codex-facing artifact was created or changed but the migration changed semantics, inferred behavior, preserved tool rules as guidance, or dropped unsupported behavior. Use `Not Added` when a source artifact was detected but no Codex-facing artifact was created. `Item` combines the artifact type and concrete item name in one cell. Artifact type must be singular: `Skill`, `Slash command`, `Subagent`, `MCP`, `Hook`, or `Plugin`. Wrap the artifact type in inline code; write the item name as plain text after it. `Notes` is always required; never leave it empty. Keep notes short, plain, and literal. Avoid internal implementation terms such as runtime expansion. Prefer phrases like `Converted into a Codex skill`, `Added as a Codex subagent`, `Added to Codex config`, `Converted into a Codex hook`, `Converted, but some Claude hook behavior differs in Codex`, `Codex does not have an equivalent notification hook`, `Plugin needs manual setup`, or `Plugin marketplace needs manual setup`.

## Self-Healing Loop

Keep looping until the selected migration is complete:

1. Run `--plan` or `--doctor`.
2. Run the migration with `--dry-run`.
3. Run the migration for real.
4. Fix every generated `## MANUAL MIGRATION REQUIRED` block and every `manual_fix_required` or `skipped` report row that can be resolved inside Codex artifacts.
5. Run `--validate-target`.
6. Re-run the migrator and validator until the report and validator have no actionable generated-artifact fixes left.

Do not edit source Claude Code files, unrelated project code, secrets, or another repository during this loop. If a report row requires source-provider changes or product judgment, leave the generated Codex artifact with clear manual guidance instead of changing the source.

## Commands

Choose the migrator command.

   ```bash
   SKILL_DIR="<absolute path to this loaded skill directory>"
   migrate_to_codex() { python3 "$SKILL_DIR/scripts/migrate-to-codex.py" "$@"; }
   ```

Inspect the migration before writing.

   ```bash
   migrate_to_codex --source ~/.claude/ --scan-only
   migrate_to_codex --source ~/.claude/ --target ~/.codex/ --plan
   migrate_to_codex --source ~/.claude/ --target ~/.codex/ --doctor
   ```

Dry-run, then run without `--dry-run`, for global and project.

   ```bash
   migrate_to_codex --source ~/.claude/ --target ~/.codex/ --dry-run
   migrate_to_codex --source ~/.claude/ --target ~/.codex/
   migrate_to_codex --source ./.claude/ --target ./.codex/ --dry-run
   migrate_to_codex --source ./.claude/ --target ./.codex/
   ```

Run the post-migration validator against each target after edits.

   ```bash
   migrate_to_codex --validate-target ~/.codex/
   migrate_to_codex --validate-target ./.codex/
   ```

Run `migrate_to_codex --help` for flags (`--scan-only`, `--plan`, `--doctor`, `--validate-target`, defaults, and so on). Deep tables and more links are in `references/differences.md`.
