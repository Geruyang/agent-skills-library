---
name: x-openai-circleci-builds-c275496
description: Diagnose and fix failing CircleCI builds quickly and safely. Use when users ask to investigate failed CircleCI jobs, triage flaky pipelines, identify root causes from logs, and implement minimal fixes in configuration, test setup, or build-related code paths.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# CircleCI Builds

## Overview

Use this skill to turn failing CircleCI pipelines into actionable fixes with clear evidence. Prioritize fast root-cause isolation, minimal safe patches, and explicit validation criteria.

Read `references/transient-vs-deterministic.md` when deciding whether a failure should be fixed in code/config, retried, mitigated with rerun behavior, or reported as external/transient.
Read `../x-openai-circleci-config-1fdce04/references/test-results-and-splitting.md` when the failure involves missing test metadata, flaky test reruns, test splitting, or JUnit XML setup.

## Inputs To Gather

- Failing pipeline/workflow/job identifier
- Branch and commit SHA
- First failing step and key log lines
- Whether rerun on same commit reproduces failure

## Workflow

1. Identify the primary failing signal.
   - Record the first failing job and step, not every downstream failure.
2. Classify issue type.
   - Config syntax/reference issue
   - Environment/toolchain mismatch
   - Dependency/cache issue
   - Test or build regression
   - External/transient failure
3. Apply the smallest viable fix.
   - Patch only files tied to confirmed root cause.
   - Keep workaround scope narrow.
4. Validate.
   - Run highest-signal local checks when possible.
   - Define expected CircleCI success signals for the rerun.
5. Report residual risk.
   - Call out unverified assumptions and likely follow-up checks.

## Guardrails

- Do not hide deterministic failures with blanket retries.
- Avoid mixing unrelated refactors into incident fixes.
- Treat external service outages as report-and-mitigate unless user asks for deeper redesign.
- Keep confidence levels explicit when logs are incomplete.
- Do not recommend automatic reruns or flaky-test workflows until the failure is classified as plausibly transient.

## Output Contract

Provide:

1. Failure summary (pipeline/workflow/job/step).
2. Root-cause hypothesis with confidence.
3. Applied changes with file list.
4. Validation plan and expected pass signal.
5. Remaining risk.
