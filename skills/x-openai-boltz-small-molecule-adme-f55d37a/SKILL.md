---
name: x-openai-boltz-small-molecule-adme-f55d37a
description: Predict Tier-1 ADME/ADMET for small molecules with Boltz from bare SMILES — no target, no docking. Use when the user wants solubility, permeability, or lipophilicity/logD for a molecule or list of molecules. Not for ranking molecules against a protein target (use boltz-small-molecule-screen, which already returns ADME free).
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

Use this skill for standalone ADME triage on SMILES the user already has. No protein target is involved. If the user is also screening or docking those molecules against a target, prefer `boltz-small-molecule-screen` — it returns the same ADME block free as part of the screen.

1. Normalize the molecules from raw SMILES, a CSV (auto-detect the SMILES column), `.smi`, or `.txt` into the `molecules` list. Each entry is `{smiles, id?}`; the optional `id` is echoed back as `external_id` on each result so you can map results to inputs.
2. **Hard cap: 128 molecules per request.** If the list exceeds 128, split into batches of ≤128 and submit one request per batch (suffix the run name, for example `-b1`, `-b2`), then merge results. Never send more than 128 in one call — the API rejects it with `VALIDATION_ERROR: input.molecules must contain at most 128 items`.
3. Author the payload YAML or JSON, run `estimate-cost`, show the USD cost, wait for explicit confirmation. ADME is priced at **$0.01 per molecule** (size-independent); `estimate-cost` returns the authoritative total — always quote it.
4. `run` to submit and wait — ADME finishes in seconds, so it is synchronous and needs no background polling. `run` persists results locally under `--root-dir/<run-name>/`.
5. Report from `<output-root>/<run-name>/run.json` → `output.molecules[]`. For each molecule show `external_id` (or `smiles`), `solubility`, `permeability`, and `lipophilicity`. The three values live under each molecule's `adme` object. Call out any molecule with `status: failed` and its `error` (an object `{code, message}`, e.g. code `adme_enumeration_failed`, message `Invalid SMILES`) — `adme` is `null` there; one bad SMILES fails only that molecule, not the batch. Read [references/results.md](references/results.md) for the output layout and [references/api.md](references/api.md) for the payload and batching details.

ADME values are approximate estimates for triage and ranking, not absolute measurements.

## Command Pattern

```bash
# Replace placeholders with concrete absolute paths before running.
# Use a short descriptive run name, for example: adme-<library>-v1

boltz-api predictions:adme estimate-cost \
  --model adme-v1 --input @yaml:///absolute/path/payload.yaml

# `run` is synchronous (submit + wait + persist) and finishes in seconds — no background mode needed.
# Run as a normal foreground command. If the host returns a retained-process handle,
# use its documented status/wait action. Do not detach via shell backgrounding.
boltz-api predictions:adme run \
  --model adme-v1 \
  --idempotency-key "<run-name>" \
  --input @yaml:///absolute/path/payload.yaml \
  --name "<run-name>" \
  --root-dir "/absolute/path/boltz-experiments" \
  --poll-interval-seconds 5
# -> /absolute/path/boltz-experiments/<run-name>/run.json  (output.molecules[].adme)
```

Payload is just a `molecules` list — the API body field name, not the direct CLI flag. `--model adme-v1` is required.

## Always Do This

- Keep payload field names exactly as the API body names shown in `references/api.md` (`molecules`, each `{smiles, id?}`).
- Pass `--model adme-v1` on every `estimate-cost`, `run`, and `start`.
- Enforce the 128-molecule-per-request cap. Chunk larger libraries into ≤128 batches and submit each as its own run; merge the per-batch `run.json` outputs when reporting.
- Use absolute paths for the output root and payload files. Do not `cd` into the run directory; pass the same `--root-dir` and use absolute paths so later relative paths do not drift.
- Prefer one merged top-level payload via `--input @yaml:///absolute/path/payload.yaml` or `@json:///absolute/path/payload.json`. Keep `--model`, `--idempotency-key`, and `--workspace-id` top-level. Never use `@file://` or `@./`.
- Run `estimate-cost` and show the USD total before submitting. ADME is $0.01/molecule (size-independent); `estimate-cost` returns the authoritative total — always use it.
- Use the same slug as both `--idempotency-key` and `--name` so re-runs resume via `.boltz-run.json`.
- In permission-gated agents such as Claude Code, keep each Boltz call as a top-level command that starts with `boltz-api`. Prefer concrete arguments over `sh -c`, inline environment assignments, aliases, wrapper scripts, loops, or pipelines unless the user already allowed that exact command form.
- ADME `run` is synchronous and finishes in seconds, so unlike the screen/design endpoints it needs no background/non-blocking mode. Run it as a normal foreground shell command. If the host returns a retained-process handle, use the host’s documented status/wait action. Do not detach via shell backgrounding.
- Do not require or accept a protein target — ADME is structure-free. If the user wants ADME *and* binding against a target, redirect to `boltz-small-molecule-screen`.

## Escape Hatch

- Payload reference: <https://api.boltz.bio/docs/api/resources/predictions/subresources/adme/methods/start/>
- Guide: <https://api.boltz.bio/docs/guides/small-molecule-adme/>
- CLI flag names: `boltz-api predictions:adme run --help`

Read [references/api.md](references/api.md) for the `molecules` payload shape, the per-molecule output fields, the 128-molecule cap, and error handling.

## Outputs

Read `<output-root>/<run-name>/run.json` and report `output.molecules[]`. There are no structure files — ADME returns scalar/categorical values only. Read [references/results.md](references/results.md) for the local layout and per-molecule output fields; [references/api.md](references/api.md) has the full request/response schema.
