---
name: x-openai-sentry-f9f88bf
description: Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Sentry (Read-only Observability)

## Quick start

- If not already authenticated, ask the user to run `sentry auth login` or set `SENTRY_AUTH_TOKEN` as an env var.
- The CLI auto-detects org/project from DSNs in `.env` files, source code, config defaults, and directory names. Only specify `<org>/<project>` if auto-detection fails or picks the wrong target.
- Defaults: time range `24h`, environment `production`, limit 20.
- Always use `--json` when processing output programmatically. Use `--json --fields` to select specific fields and reduce output size.
- Use `sentry schema <resource>` to discover API endpoints quickly.

If the CLI is not installed, give the user these steps:
1. Install the Sentry CLI: `curl https://cli.sentry.dev/install -fsS | bash`
2. Authenticate: `sentry auth login`
3. Confirm authentication: `sentry auth status`
- Never ask the user to paste the full token in chat. Ask them to set it locally and confirm when ready.

## Core tasks (use Sentry CLI)

Use the `sentry` CLI for all queries. It handles authentication, org/project detection, pagination, and retries automatically. Use `--json` for machine-readable output.

### 1) List issues (ordered by most recent)

```bash
sentry issue list \
  --query "is:unresolved environment:production" \
  --period 24h \
  --limit 20 \
  --json --fields shortId,title,priority,level,status
```

If auto-detection doesn't resolve org/project, pass them explicitly:
```bash
sentry issue list {your-org}/{your-project} \
  --query "is:unresolved environment:production" \
  --period 24h \
  --limit 20 \
  --json
```

### 2) Resolve an issue short ID to issue detail

```bash
sentry issue view {ABC-123} --json
```

Use the short ID format (e.g., `ABC-123`), not the numeric ID.

### 3) Issue detail

```bash
sentry issue view {ABC-123}
```

### 4) Issue events

```bash
sentry issue events {ABC-123} --limit 20 --json
```

### 5) Event detail

```bash
sentry event view {your-org}/{your-project}/{event_id} --json
```

### 6) AI-powered root cause analysis

```bash
sentry issue explain {ABC-123}
```

### 7) AI-powered fix plan

```bash
sentry issue plan {ABC-123}
```

## Fallback: arbitrary API access

For endpoints not covered by dedicated CLI commands, use `sentry api`:
```bash
sentry api /api/0/organizations/{your-org}/ --method GET
```

Use `sentry schema` to discover available API endpoints:
```bash
sentry schema issues
```

## Inputs and defaults

- `org_slug`, `project_slug`: auto-detected by the CLI from DSNs, env vars, and directory names. Override with positional `{your-org}/{your-project}` if auto-detection fails.
- `time_range`: default `24h` (pass as `--period 24h`).
- `environment`: default `prod` (pass as part of `--query`, e.g., `environment:production`).
- `limit`: default 20 (pass as `--limit`).
- `search_query`: optional `--query` parameter, uses Sentry search syntax (e.g., `is:unresolved`, `assigned:me`).
- `issue_short_id`: use directly with `sentry issue view`.

## Output formatting rules

- Issue list: show title, short_id, status, first_seen, last_seen, count, environments, top_tags; order by most recent.
- Event detail: include culprit, timestamp, environment, release, url.
- If no results, state explicitly.
- Redact PII in output (emails, IPs). Do not print raw stack traces.
- Never echo auth tokens.

## Golden test inputs

- Org: `{your-org}`
- Project: `{your-project}`
- Issue short ID: `{ABC-123}`

Example prompt: "List the top 10 open issues for prod in the last 24h."
Expected: ordered list with titles, short IDs, counts, last seen.
