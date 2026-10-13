---
name: x-openai-dynamo-router-starter-6527b74
description: Start or patch Dynamo router modes and run router endpoint smoke checks. Use for round-robin, KV-aware, least-loaded, or device-aware routing setup; use recipe-runner for recipe deployment and troubleshoot for failure diagnosis.
license: Apache-2.0
metadata:
  author: Dan Gil <dagil@nvidia.com>
  tags: '[''dynamo'', ''router'', ''smoke-test'', ''bring-up'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Dynamo Router Starter

<!--
SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: CC-BY-4.0
-->

## Purpose

Make Dynamo routing feel easy by getting a baseline router mode running, enabling
KV-aware routing when appropriate, and proving the endpoint works. Keep the user
focused on exact commands and success signals, not router internals.

## Prerequisites

- Python 3.10+ with the `dynamo` package importable (`python3 -m dynamo.frontend --help` works).
- For Kubernetes runs: `kubectl` configured with access to the target namespace and a deployed Dynamo recipe.
- Network reachability to the frontend service (port-forward or direct).
- A model already loaded into at least one worker (`/v1/models` returns at least one entry).

## Required Inputs

Collect or infer:

- local Python/CLI or Kubernetes recipe path
- desired mode: `round-robin`, `kv`, `least-loaded`, `device-aware-weighted`, `direct`, or `random`
- frontend port or Kubernetes frontend service
- whether workers publish KV events; if not, use approximate KV mode
- model name for smoke requests, if `/v1/models` cannot discover it

## Instructions

### 1. Establish A Baseline

For local bring-up with already registered workers:

```bash
python3 -m dynamo.frontend --router-mode round-robin --http-port 8000
```

For Kubernetes, inspect the selected recipe `deploy.yaml` and locate the
frontend service. If the recipe is not already deployed, use
`dynamo-recipe-runner` first.

### 2. Enable KV Routing

For local frontend:

```bash
python3 -m dynamo.frontend --router-mode kv --http-port 8000
```

For Kubernetes, patch only the frontend service env:

```yaml
envs:
  - name: DYN_ROUTER_MODE
    value: kv
```

If backend workers are not publishing KV cache events, set approximate mode
instead of leaving the router waiting for events:

```yaml
envs:
  - name: DYN_ROUTER_USE_KV_EVENTS
    value: "false"
```

### 3. Smoke Test

After port-forwarding the frontend service or starting local frontend, run:

```bash
python3 scripts/check_router_health.py \
  --base-url http://127.0.0.1:8000
```

This must verify `/v1/models` and, when a model is discoverable, one
`/v1/chat/completions` request.

### 4. Compare Modes Carefully

When comparing round-robin vs KV routing:

- use the same model, workers, prompt set, concurrency, and sampling settings
- send repeated-prefix prompts if demonstrating KV reuse
- label the result as a smoke comparison unless enough benchmark samples were collected
- do not claim throughput improvement from a single chat request

If the endpoint is unhealthy or workers are missing, switch to
`dynamo-troubleshoot`.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/check_router_health.py` | Smoke-test `/v1/models` and one chat completion against a Dynamo frontend | `--base-url`, `--retries`, `--timeout` |

Invoke via the agentskills.io `run_script()` protocol:

```python
run_script("scripts/check_router_health.py", args=["--base-url", "http://127.0.0.1:8000"])
```

## Examples

Local KV-routed frontend on port 8000, then smoke-test it:

```bash
python3 -m dynamo.frontend --router-mode kv --http-port 8000 &
python3 scripts/check_router_health.py --base-url http://127.0.0.1:8000
```

Kubernetes-deployed frontend reachable via port-forward:

```bash
kubectl port-forward svc/qwen-vllm-disagg-frontend 8000:8000 -n dynamo-demo &
python3 scripts/check_router_health.py --base-url http://127.0.0.1:8000 --retries 3
```

Equivalent through the agent protocol:

```python
run_script("scripts/check_router_health.py", args=["--base-url", "http://127.0.0.1:8000", "--retries", "3"])
```

## Output Contract

Return:

- mode selected and why
- local command or Kubernetes env patch
- frontend service or URL
- smoke-test result
- any limitation, such as approximate KV mode or missing worker KV events
- next command to run for a fuller comparison

## Limitations

- Smoke test is one chat completion; it is not a benchmark. Use `dynamo-benchmark` for throughput/latency numbers.
- KV-aware mode without worker KV-event publication degrades to approximate mode; this skill flags but does not fix the underlying worker config.
- Mode comparisons require matched workloads; cross-mode latency claims need separate benchmark runs.

## Troubleshooting

| Symptom | Likely cause | Next step |
|---|---|---|
| `/v1/models` returns empty list | No worker registered with the frontend | Verify worker pods are Ready; confirm they connect to the same etcd/NATS |
| Smoke chat request times out | Frontend up, workers not serving | Switch to `dynamo-troubleshoot`; inspect worker logs |
| KV mode hangs | Workers do not publish KV cache events | Set `DYN_ROUTER_USE_KV_EVENTS=false` (approximate mode) |
| Connection refused on port-forward | Port-forward dropped or wrong service name | Re-run port-forward; verify the frontend service name matches the recipe |

## Benchmark

See `BENCHMARK.md` for the NVCARPS-EVAL performance report (auto-generated by the NVSkills CI pipeline). To refresh, re-run `/nvskills-ci` on an upstream PR touching this skill.

## References

- Read `references/router-modes.md` for the compact mode/env map.
- Use `scripts/check_router_health.py` for endpoint smoke tests.
