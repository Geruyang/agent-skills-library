---
name: x-openai-vercel-agent-5303b1d
description: Vercel Agent guidance — AI-powered code review, incident investigation, and SDK installation. Automates PR analysis and anomaly debugging. Use when configuring or understanding Vercel's AI development tools.
metadata:
  priority: '4'
  docs: '[''https://vercel.com/docs'', ''https://sdk.vercel.ai/docs'']'
  sitemap: https://vercel.com/sitemap/docs.xml
  pathPatterns: '[''.github/workflows/vercel*.yml'', ''.github/workflows/vercel*.yaml'', ''.github/workflows/deploy*.yml'', ''.github/workflows/deploy*.yaml'', ''.github/workflows/preview*.yml'', ''.github/workflows/preview*.yaml'']'
  bashPatterns: '[''\\bvercel\\s+agent\\b'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Vercel Agent

You are an expert in Vercel Agent — AI-powered development tools built into the Vercel platform.

## What It Is

Vercel Agent is a suite of **AI-powered development tools** that leverage deep context about your codebase, deployment history, and runtime behavior. It provides automated code review, incident investigation, and SDK installation assistance.

## Capabilities

### Code Review
- Automatic PR analysis triggered on push or via `@vercel` mention in PR comments
- Multi-step reasoning: identifies security vulnerabilities, logic errors, performance issues
- Generates and validates patches in **Vercel Sandbox** (secure execution)
- Supports inline suggestions and full patch proposals

### Investigation
- Analyzes anomaly alerts by querying logs and metrics
- Finds patterns and correlations across deployment data
- Provides root cause insights
- **Requires Observability Plus** subscription

### Installation
- Auto-installs Web Analytics and Speed Insights SDKs
- Analyzes repo structure, installs dependencies, writes integration code
- Creates PRs with the changes
- **Free** (no credit cost)

## Pricing

- $0.30 per Code Review or Investigation + token costs
- $100 promotional credit for Pro teams
- Installation is free

## Configuration

Vercel Agent is configured at `https://vercel.com/{team}/{project}/settings` → **AI** section. No npm package required — it is a platform-level service.

## When to Use

- Automated security and quality checks on every PR
- Root-cause analysis when anomaly alerts fire
- Quick SDK installation for analytics/monitoring

## References

- 📖 docs: https://vercel.com/docs/agent
