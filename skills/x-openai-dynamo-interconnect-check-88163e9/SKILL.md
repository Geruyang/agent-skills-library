---
name: x-openai-dynamo-interconnect-check-88163e9
description: Validate that a Dynamo deployment's NIXL/UCX/NCCL interconnect is ready for disaggregated serving over RDMA/NVLink. Use after recipe-runner brings a deployment up (especially disagg/multi-node) to confirm the KV transport is correct; use troubleshoot for diagnosing already-failed pods.
license: Apache-2.0
metadata:
  author: Dan Gil <dagil@nvidia.com>
  tags: '[''dynamo'', ''nixl'', ''rdma'', ''disagg'', ''validation'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Dynamo Interconnect Check

<!--
SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: CC-BY-4.0
-->

## Purpose

Confirm that the transport disaggregated serving depends on actually works. A
deployment can pass an endpoint smoke test while disagg is silently wrong: if
NIXL/UCX cannot reach the peer worker over RDMA or NVLink, KV transfer falls
back to a slow or broken path. Catch that with read-only checks before trusting
a disagg deployment or its benchmark numbers.

This skill is read-only. It never mutates the cluster and never prints secrets.

## Prerequisites

- Python 3.10+ on the operator machine.
- `kubectl exec` access to a worker pod in the target Dynamo deployment.
- Read access to the recipe directory (`recipes/<model>/<framework>/<mode>`).
- For node-capability checks: tools like `ibstat`, `nvidia-smi`, `lsmod` available in the worker pod image (missing tools are reported as `skipped`, not failures).

## When To Use

- After `dynamo-recipe-runner` deploys a **disagg** or multi-node recipe.
- Before reporting disagg throughput/latency, so numbers reflect the real
  transport.
- When agg works but disagg is slow, hangs, or returns wrong output and you
  suspect the fabric rather than the model.

For diagnosing pods that are already crashing or unschedulable, use
`dynamo-troubleshoot` first.

## Instructions

### 1. Check Transport Env Vars On The Recipe

```bash
python3 scripts/check_interconnect.py env recipes/<model>/<framework>/<mode>
```

Reports which NIXL/UCX/NCCL transport variables are set and flags
disagg-critical ones (e.g. `UCX_TLS`, `UCX_NET_DEVICES`, `NCCL_IB_HCA`) that are
absent. Missing here is only a warning — they may be baked into the image — so
confirm with the node and NIXL checks. See
`references/interconnect-env-vars.md` for what each variable does.

### 2. Check Node Capabilities

Locally on a GPU node, or inside a running worker pod:

```bash
python3 scripts/check_interconnect.py node \
  --namespace "${NAMESPACE}" --pod <worker-pod>
```

Probes (read-only) for: InfiniBand devices and Active links, GPUDirect RDMA
(`nvidia_peermem`), GDRCopy, and NVLink in the GPU topology. Missing tools are
reported as `skipped`, not failures.

### 3. Validate NIXL Reachability

```bash
python3 scripts/check_interconnect.py nixl \
  --namespace "${NAMESPACE}" --pod <worker-pod>
```

Looks for NIXL test tooling in the pod and surfaces the exact next step to run a
pairwise prefill↔decode transfer test. A full cross-pod transfer test requires
two scheduled GPU pods on the fabric.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/check_interconnect.py env` | Inspect NIXL/UCX/NCCL env vars on a recipe | positional recipe path |
| `scripts/check_interconnect.py node` | Probe InfiniBand, GPUDirect RDMA, GDRCopy, NVLink on a node or pod | `--namespace`, `--pod` |
| `scripts/check_interconnect.py nixl` | Surface NIXL transfer-test readiness for a pod | `--namespace`, `--pod` |

Invoke via the agentskills.io `run_script()` protocol:

```python
run_script("scripts/check_interconnect.py", args=["env", "recipes/qwen3-coder-480b/sglang/disagg"])
run_script("scripts/check_interconnect.py", args=["node", "--namespace", "dynamo-demo", "--pod", "qwen-worker-0"])
```

## Examples

Verify a disagg recipe's transport env shape before deploy:

```bash
python3 scripts/check_interconnect.py env recipes/qwen3-coder-480b/sglang/disagg
```

After deploy, validate a worker pod's fabric:

```bash
python3 scripts/check_interconnect.py node \
  --namespace dynamo-demo --pod qwen-worker-0
python3 scripts/check_interconnect.py nixl \
  --namespace dynamo-demo --pod qwen-worker-0
```

Equivalent through the agent protocol:

```python
run_script("scripts/check_interconnect.py", args=["nixl", "--namespace", "dynamo-demo", "--pod", "qwen-worker-0"])
```

## Output Contract

Each check returns `ok` / `warn` / `fail` / `skipped` with a one-line detail,
plus a rolled-up verdict on disagg transport readiness. Report:

- transport env vars present vs. disagg-critical ones missing
- RDMA / GPUDirect / NVLink capability status
- whether NIXL reachability was validated, and the next command if not
- a clear statement of whether disagg can be trusted, or what to fix first

## Limitations

- Read-only fabric probe; does not run a full pairwise NIXL transfer (requires two scheduled GPU pods and the in-pod NIXL test tools).
- `skipped` results for missing tools (`ibstat`, `nvidia-smi`, `lsmod`) are inconclusive, not a pass.
- Env-var check inspects the recipe text; values injected at runtime via initContainers or operator-applied envs are not detected.
- Single-node agg deployments do not exercise the transport — this skill is for disagg / multi-node validation.

## Troubleshooting

| Symptom | Likely cause | Next step |
|---|---|---|
| `env` reports all critical vars missing | Vars baked into image or injected by operator | Run the `node` check inside the worker pod to verify actual env |
| `node` reports no Active IB link | Fabric down or HCA not provisioned to the node | Contact cluster admin; verify `kubectl describe node` shows `nvidia.com/gpu` and IB labels |
| `nvidia_peermem` missing | GPUDirect RDMA module not loaded | Ask cluster admin to load `nvidia-peermem`; without it, NIXL falls back to staged copies |
| `nixl` finds no test tools | Worker image lacks NIXL test harness | Use a NIXL-enabled image or run the standalone transfer test from a debug pod |

## Benchmark

See `BENCHMARK.md` for the NVCARPS-EVAL performance report (auto-generated by the NVSkills CI pipeline). To refresh, re-run `/nvskills-ci` on an upstream PR touching this skill.

## References

- `references/interconnect-env-vars.md` — NIXL/UCX/NCCL env var catalog and IB
  capability checklist.
- Use `scripts/check_interconnect.py` for all read-only checks.
