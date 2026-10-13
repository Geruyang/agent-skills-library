---
name: x-openai-circleci-config-1fdce04
description: Optimize CircleCI configuration for speed, reliability, and maintainability. Use when users ask to improve `.circleci/config.yml`, reduce CI runtime, tune caching/workspaces/parallelism, remove pipeline waste, or fix flaky pipeline behavior caused by configuration choices.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# CircleCI Config

## Overview

Use this skill to improve CircleCI performance and stability without changing product behavior. Focus on measured bottlenecks first, then implement the smallest safe config changes with clear validation criteria.

Read `references/cache-optimization.md` when the request involves `save_cache`, `restore_cache`, `persist_to_workspace`, `attach_workspace`, cache key design, dependency caching, lockfiles, or complaints about low cache hit rates, oversized caches, or wasted persistence steps.
Read `references/persisting-data.md` when the request involves choosing between caches, workspaces, and artifacts, or when data is being moved between jobs inefficiently.
Read `references/test-results-and-splitting.md` when the request involves slow test jobs, parallelism, flaky test visibility, missing JUnit XML, or `circleci tests run`.
Read `references/patterns.md` when the request involves approvals, branch/tag filters, schedules, deploy flow structure, or environment promotion patterns.

## Inputs To Gather

- `.yaml` and `.yml` files in `.circleci/` and any reusable config fragments
- Current pain points: duration, flakiness, cost, or maintainability
- Baseline metrics: slowest jobs, most frequent retries/failures, queue and run times
- Risk tolerance for structural changes

## Workflow

1. Build a baseline.
   - Identify top 1-3 longest jobs and top flaky jobs.
   - Capture before metrics (duration, pass rate, retries).
2. Remove pipeline waste.
   - Eliminate duplicate jobs/workflows.
   - Tighten branch/tag filters and workflow triggers.
3. Improve dependency and artifact flow.
   - Fix cache keys to include deterministic lockfile checks.
   - Use workspaces/artifacts to avoid rebuilding identical outputs.
   - Prefer cache scopes that are narrow, reproducible, and cheap to restore.
4. Apply safe parallelism.
   - Parallelize only proven bottlenecks.
   - Keep fan-out/fan-in readable and deterministic.
5. Validate impact.
   - Define expected metric changes and acceptance criteria before finalizing.

## Guardrails

- Prefer configuration fixes before proposing application code changes.
- Do not add blanket retries to hide deterministic failures.
- Preserve deployment safety gates while optimizing build/test stages.
- Keep changes incremental and easy to revert.
- Prefer language-specific cache directories over broad project snapshots.
- Avoid cache keys that rotate every run unless the user explicitly wants effectively write-only caches.

## Output Contract

Provide:

1. Baseline bottleneck summary.
2. Proposed or applied config changes with rationale.
3. Expected runtime/reliability impact.
4. Validation plan and rollback note.
