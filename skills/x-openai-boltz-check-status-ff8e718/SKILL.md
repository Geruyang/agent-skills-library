---
name: x-openai-boltz-check-status-ff8e718
description: Boltz job status and result recovery. Use when listing jobs, checking progress, resuming downloads, recovering results, or downloading an existing job ID. Not for starting new jobs.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Workflow

If `boltz-api` is missing from `PATH`, use `boltz-cli-setup` for install/update guidance before retrying.
If a command reports missing or expired authentication, use `boltz-cli-setup` to start `boltz-api auth login --device-code` before retrying; do not ask permission first.
If the agent host sandbox blocks `boltz-api` install/auth/API calls, use `boltz-cli-setup` to request the host sandbox bypass/escalation needed for user-wide CLI install, browser login, credential storage, temp files, or API access before retrying.

Use this skill to recover state across sessions and to inspect or download results for prior Boltz jobs. No payload authoring — this skill only calls `list` / `retrieve` / `download-results` / `download-status`.

Use four modes:

1. Local progress: if the user knows the run name / run dir, prefer `download-status` before remote API calls.
2. List recent jobs: enumerate all six resources, merge, and sort by `created_at` descending.
3. Retrieve one job: use the job ID prefix when known; otherwise probe resources until one succeeds.
4. Resume/download results: run `download-results` with the original run name when possible. Never run `start` again to resume.

ADME jobs use the prefix `adme_pred_*` and show up in Modes 1-2 (`list` / `retrieve`) like the others. ADME has **no** `download-results`/archive step, so Modes 3-4 don't apply — recover its scores by re-running `retrieve` (read `output.molecules[]`) or from the local `run.json`.

Read [references/resume.md](references/resume.md) before recovering a dropped session, mapping job ID prefixes, or choosing a run name for `download-results`. Read [references/api.md](references/api.md) for per-resource `list` columns, `retrieve` fields, and result semantics.

## Command Pattern

```bash
# Replace placeholders with concrete absolute paths before running.

# Local helper: inspect local checkpoint state without API calls.
boltz-api --format json download-status \
  --name "<run-name>" \
  --root-dir "/absolute/path/boltz-experiments"

# Mode 1: list recent jobs across all 6 resources.
# Note: the CLI emits one JSON object per record (streamed, no {data:[]} wrapper).
# --limit is per-page and the CLI auto-paginates, so cap each explicit command with head.
boltz-api predictions:structure-and-binding list --limit 20 --format jsonl | head -20
boltz-api predictions:adme list --limit 20 --format jsonl | head -20
boltz-api small-molecule:library-screen list --limit 20 --format jsonl | head -20
boltz-api small-molecule:design list --limit 20 --format jsonl | head -20
boltz-api protein:library-screen list --limit 20 --format jsonl | head -20
boltz-api protein:design list --limit 20 --format jsonl | head -20

# Mode 2: retrieve by ID. Pick the resource from the ID prefix in the workflow
# notes above. If the prefix is unknown, run these one at a time until one succeeds.
boltz-api predictions:structure-and-binding retrieve --id "<job-id>" --format json
boltz-api predictions:adme retrieve --id "<job-id>" --format json
boltz-api small-molecule:library-screen retrieve --id "<job-id>" --format json
boltz-api small-molecule:design retrieve --id "<job-id>" --format json
boltz-api protein:library-screen retrieve --id "<job-id>" --format json
boltz-api protein:design retrieve --id "<job-id>" --format json

# Mode 3: resume download. Use the agent runtime's managed long-running command mode.
boltz-api download-results \
  --id "<job-id>" --name "<run-name>" \
  --root-dir "/absolute/path/boltz-experiments" \
  --poll-interval-seconds 30
```

## Always Do This

- If the user has a run name / slug or run dir and only wants local downloader state, prefer `download-status` before `retrieve`.
- Use an absolute output root and keep passing it through `--root-dir`. Do not `cd` into the run directory; that makes later relative paths point at the run directory instead of the user's workspace.
- On an unfamiliar job ID, run Mode 2 (retrieve) before Mode 3 (download) so you capture `idempotency_key`.
- Prefer the original run-name slug over the job ID as `--name` — it resumes into the existing dir with cursor.
- In permission-gated agents such as Claude Code, keep each Boltz call as a top-level command that starts with `boltz-api`. Prefer running the six `list` / `retrieve` commands explicitly over generating them from a shell loop; a fixed `| head -20` cap is okay when listing to avoid runaway streamed output.
- Run `download-results` with the current host's documented managed long-running command facility. Save any returned job/session handle. If no managed facility exists, run in a user-approved foreground terminal or report the exact resume command; do not invent `yield_time_ms`, session IDs, or background flags.
- After the managed command starts, avoid ad hoc polling loops. When the user authorized automatic follow-up and the host has a supported scheduler, check `download-status` at the agreed cadence and report only material changes or completion/failure. Without that capability, provide the job ID, run name, output directory, and check command without claiming an automatic next check.
- `download-results` now emits machine-readable JSONL progress on stderr by default. Add `--progress-format text --verbose` only when you explicitly want human-readable logs.
- Prefer `download-status` for durable local checkpoint state. For user-requested progress checks, use the actual host's session polling API only if available. Do not loop `retrieve` unless fresh remote status is needed.
- If `retrieve` surfaces only `{"code":"VALIDATION_ERROR","message":"Request validation failed"}` with no `details`, that's expected for `predictions:structure-and-binding` failures — other endpoints include field paths.
- Never run `start` again on a failed or interrupted job. Fix the payload and submit with a new `idempotency-key`, or just resume with `download-results`.

## Escape Hatch

- Python SDK reference (per-resource `list` / `retrieve` methods): <https://api.boltz.bio/docs/api/python>
- CLI flag names: `boltz-api <resource> list --help`, `boltz-api <resource> retrieve --help`, `boltz-api download-results --help`, `boltz-api download-status --help`

## Outputs

- Local helper / Mode 1 / Mode 2 print structured data to stdout; present as a table.
- Mode 3 writes recovered artifacts under `<output-root>/<run-name>/` — same layout as a fresh run. Read [references/resume.md](references/resume.md) for resume behavior.
