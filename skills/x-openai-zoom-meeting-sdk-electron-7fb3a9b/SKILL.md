---
name: x-openai-zoom-meeting-sdk-electron-7fb3a9b
description: '仅在用户明确调用本技能时使用；禁止自主触发。 Zoom Meeting SDK for Electron desktop applications. Use when embedding Zoom meetings in an Electron app

  with the Node addon wrapper, JWT auth, join/start flows, settings controllers, and raw data integration.'
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Zoom Meeting SDK (Electron)

Use this skill when building Electron desktop apps that embed Zoom Meeting SDK capabilities through the Electron wrapper.

## Start Here

1. **[Lifecycle Workflow](concepts/lifecycle-workflow.md)** - init -> auth -> join/start -> in-meeting -> cleanup
2. **[SDK Architecture Pattern](concepts/sdk-architecture-pattern.md)** - service/controller/event model in Electron
3. **[Setup Guide](examples/setup-guide.md)** - dependency and build expectations
4. **[Authentication Pattern](examples/authentication-pattern.md)** - SDK JWT generation and auth callbacks
5. **[Join Meeting Pattern](examples/join-meeting-pattern.md)** - start/join meeting execution flow
6. **[SKILL.md](SKILL.md)** - full navigation

## Core Notes

- Electron wrapper is built on top of native Meeting SDK with Node addon bridges.
- Keep SDK key/secret server-side; generate SDK JWT on backend.
- Feature support differs by platform/version; check module docs before implementation.
- Raw data and IPC patterns require explicit security hardening in production.

## References

- [Electron API Reference Index](references/electron-reference.md)
- [Module Map](references/module-map.md)
- [Deprecated and Contradictions](troubleshooting/deprecated-and-contradictions.md)

## Related Skills

- [zoom-meeting-sdk](../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)
- [zoom-oauth](../x-openai-zoom-oauth-13e78b7/SKILL.md)
- [zoom-general](../x-openai-zoom-general-37cf44c/SKILL.md)


## Merged from meeting-sdk/electron/SKILL.md

# Zoom Meeting SDK Electron - Documentation Index

## Start Here

1. [SKILL.md](SKILL.md)
2. [Lifecycle Workflow](concepts/lifecycle-workflow.md)
3. [SDK Architecture Pattern](concepts/sdk-architecture-pattern.md)
4. [Setup Guide](examples/setup-guide.md)

## Concepts

- [Lifecycle Workflow](concepts/lifecycle-workflow.md)
- [SDK Architecture Pattern](concepts/sdk-architecture-pattern.md)
- [High-Level Scenarios](concepts/high-level-scenarios.md)

## Examples

- [Setup Guide](examples/setup-guide.md)
- [Authentication Pattern](examples/authentication-pattern.md)
- [Join Meeting Pattern](examples/join-meeting-pattern.md)
- [Raw Data Pattern](examples/raw-data-pattern.md)

## References

- [Electron API Reference](references/electron-reference.md)
- [Module Map](references/module-map.md)

## Troubleshooting

- [Common Issues](troubleshooting/common-issues.md)
- [Version Drift](troubleshooting/version-drift.md)
- [Deprecated and Contradictions](troubleshooting/deprecated-and-contradictions.md)

## Operations

- [RUNBOOK.md](RUNBOOK.md) - 5-minute preflight and debugging checklist.
