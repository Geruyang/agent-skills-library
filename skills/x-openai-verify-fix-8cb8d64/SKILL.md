---
name: x-openai-verify-fix-8cb8d64
description: Use only when the user explicitly requests verification that a security fix remediates a reported vulnerability. Do not invoke automatically while implementing fixes, reviewing ordinary code changes, or running tests. Do not use for non-security fixes, candidate finding validation, or full repository scans.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Verify Fix

## When to Use

Invoke this skill only for an explicit request to verify a security fix, including a direct `x-openai-verify-fix-8cb8d64` invocation. A request to implement a fix or run its tests does not by itself request this skill. For other tasks, follow the user's requested workflow and response format without applying this skill's JSON result contract.

## Objective

Determine whether each supplied security finding has been fixed in the current checkout. Operate in standalone verification-only mode; do not create, modify, or delete repository files, apply patches, commit changes, write artifacts, or modify issue trackers.

## Assessment Method

Use `../../resources/plugins-6ebaff11/plugins/codex-security/references/static-finding-assessment.md` to identify the original attacker-controlled source, security control, sensitive sink, reachable path, trust boundary, counterevidence, and proof gaps. If the caller already supplied that reference in the prompt, use the supplied contents without reading it again.

## Verification Workflow

1. Establish the original vulnerability, its preconditions, affected security boundary, and legitimate behavior that must continue to work.
2. Confirm the current checkout contains the affected component. Follow moved or refactored code rather than treating a missing file, removed line, or changed function name as proof of remediation.
3. Trace the original exploit path through the current implementation and check the nearest relevant control, equivalent paths, and plausible bypasses.
4. Run the original reproducer, focused regression checks, or legitimate-behavior checks only when they can run without modifying the repository. Preserve exact static evidence when runtime checks are unavailable.
5. Return one result per supplied finding, in the requested order. Treat closed tickets, unrelated passing tests, and the absence of a new scan finding as insufficient proof.

## Result Contract

Return exactly one JSON object:

```json
{
  "results": [
    {
      "id": "finding-or-issue-id",
      "status": "fixed|still_vulnerable|inconclusive",
      "evidence": "specific current source, exploit, test, or proof-gap evidence"
    }
  ]
}
```

- Use `fixed` only when evidence proves the original security boundary is closed and legitimate behavior remains intact.
- Use `still_vulnerable` only when evidence proves the original vulnerable path remains reachable.
- Use `inconclusive` for a repository mismatch, missing original context, unavailable relevant checks, an unproven legitimate control, or another material proof gap.

Never infer a stronger verdict by weakening the read-only boundary, substituting a different vulnerability, or hiding missing evidence.
