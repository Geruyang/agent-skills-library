---
name: x-openai-ios-memgraph-leaks-2a6e50b
description: Capture and inspect iOS leaks and memgraphs. Use when debugging leaked objects, retain cycles, memory growth, or before/after leak evidence.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# iOS Memgraph Leaks

Use this skill to prove iOS leaks from a live simulator process or an existing `.memgraph`. Pair it with `../x-openai-ios-debugger-agent-197293c/SKILL.md` when the task also needs simulator build, install, launch, UI driving, logs, or screenshots.

## Core Workflow

1. Build, launch, and drive the exact flow that should release objects.
2. Capture a memgraph from the running simulator process with `scripts/capture_sim_memgraph.sh`.
3. Summarize leaks with `scripts/summarize_memgraph_leaks.py`.
4. For each app-owned leaked type, inspect ownership with `leaks --traceTree=<address> <file.memgraph>` and grouped leak evidence.
5. Make the smallest root-cause patch, then recapture the same flow on the same simulator when possible.
6. Report proof: before/after leak counts, disappeared root types, remaining leaks, memgraph paths, and test/build results.

Do not claim a leak fix from a smaller memgraph alone. A credible fix explains the ownership path that kept the object alive and shows that the same path or type disappears after the patch.

## Capture

Prefer capturing from the simulator already used for the reproduction. Resolve the simulator UDID and app bundle identifier, then capture the running app:

```bash
SKILL_DIR="<absolute path to this loaded skill folder>"
SIM="<simulator-udid>"
BUNDLE_ID="<app.bundle.identifier>"
MEMGRAPH_DIR="$(mktemp -d "${TMPDIR:-/tmp}/codex-ios-memgraph.XXXXXX")"

"$SKILL_DIR/scripts/capture_sim_memgraph.sh" \
  --udid "$SIM" \
  --bundle-id "$BUNDLE_ID" \
  --out-dir "$MEMGRAPH_DIR"
```

Do not derive `SKILL_DIR` from the target app repo's `pwd`; installed plugins usually live outside the app being debugged. Store captures in a run-specific temp or user-chosen folder, not under `SKILL_DIR`.

If the process cannot be found, confirm the bundle identifier and use `xcrun simctl spawn "$SIM" launchctl list` to inspect running labels.

## Summarize

Summarize an existing memgraph:

```bash
"$SKILL_DIR/scripts/summarize_memgraph_leaks.py" \
  /path/to/app.memgraph \
  --trace-limit 5 \
  --out /path/to/leak-summary.md
```

Use `--trace-limit` sparingly. Trace trees are useful root-cause evidence, but large memgraphs can produce noisy output. If a trace tree says `Found 0 roots referencing`, treat it as an unreachable/self-retained leak candidate and use the summary's grouped leak tree or `leaks --groupByType <file.memgraph>` to identify the retained fields and payload chain.

## Root Cause Rules

- Identify the first app-owned leaked type in the leak output or trace.
- Determine the intended lifetime: process, session, account, view, request, or task.
- Treat lazy or deferred allocation as a scope reduction, not a leak fix, unless the original eager allocation itself violated the intended lifetime.
- Prove retain-cycle claims with either a `traceTree` ownership path or an isolated reproduction.
- For unreachable/self-cycle leaks, `traceTree` may have no root path; use `leaks --groupByType` plus source verification to find the self-retaining edge.
- Do not claim success just because total leak count went down; prove the specific type or path disappeared.
- Separate real root-cause branches from candidate/noise branches.
- Prefer deleting the retaining edge over adding broad cleanup code.

## Report

A useful leak report includes:

- the exact flow and simulator/app build
- the memgraph and summary paths
- app-owned leaked types and counts
- at least one ownership path, or grouped leak tree evidence when the object is unreachable from roots
- the smallest proposed or applied retaining-edge fix
- before/after evidence when a fix was made

If the memgraph shows only framework/runtime noise, say that and recommend the next narrower capture rather than inventing an app leak.
