---
name: x-openai-zoom-meeting-sdk-react-native-c3f80cf
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Zoom Meeting SDK (React Native)

Use this skill when building React Native apps that need embedded Zoom meeting join/start flows.

## Quick Links

1. **[Lifecycle Workflow](concepts/lifecycle-workflow.md)** - init -> auth -> join/start -> in-meeting -> cleanup
2. **[Architecture](concepts/architecture.md)** - JS wrapper, native bridge, iOS/Android SDK layers
3. **[High-Level Scenarios](concepts/high-level-scenarios.md)** - practical product patterns
4. **[Setup Guide](examples/setup-guide.md)** - install package + platform requirements
5. **[Join Meeting Pattern](examples/join-meeting-pattern.md)** - JWT + meetingNumber + password
6. **[Start Meeting Pattern](examples/start-meeting-pattern.md)** - ZAK-based host start
7. **[SKILL.md](SKILL.md)** - full navigation

## Core APIs (Wrapper)

From `@zoom/meetingsdk-react-native` wrapper surface:

- `initSDK(config)`
- `isInitialized()`
- `updateMeetingSetting(config)`
- `joinMeeting(config)`
- `startMeeting(config)`
- `cleanup()`

See: **[Wrapper API](references/wrapper-api.md)**

## Critical Notes

- You still need native iOS/Android Meeting SDK dependencies configured.
- `joinMeeting` and `startMeeting` return numeric status/error codes from native layer.
- For host start flow, pass `zoomAccessToken` (ZAK).
- Keep JWT generation on backend, never embed SDK secret in app.
- Current docs note React Native support up to `0.75.4`; Expo is not supported.

## Platform Guides

- **[iOS Setup](references/ios-setup.md)** - Podfile, optional ReplayKit/app group fields
- **[Android Setup](references/android-setup.md)** - Gradle dependency + options mapping
- **[Native Bridge Notes](references/native-bridge-notes.md)** - behavior differences and gotchas

## Troubleshooting

- **[Common Issues](troubleshooting/common-issues.md)**
- **[Version Drift](troubleshooting/version-drift.md)**
- **[Deprecated/Contradictions](troubleshooting/deprecated-and-contradictions.md)**

## Related Skills

- **[zoom-meeting-sdk](../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)** - parent Meeting SDK hub
- **[zoom-oauth](../x-openai-zoom-oauth-13e78b7/SKILL.md)** - auth flow and token management
- **[zoom-general](../x-openai-zoom-general-37cf44c/SKILL.md)** - cross-product architecture decisions

## Documentation Index

### Start Here

1. [SKILL.md](SKILL.md)
2. [Lifecycle Workflow](concepts/lifecycle-workflow.md)
3. [Architecture](concepts/architecture.md)
4. [Setup Guide](examples/setup-guide.md)

### Concepts

- [Lifecycle Workflow](concepts/lifecycle-workflow.md)
- [Architecture](concepts/architecture.md)
- [Auth and Token Model](concepts/auth-and-token-model.md)
- [High-Level Scenarios](concepts/high-level-scenarios.md)

### Examples

- [Setup Guide](examples/setup-guide.md)
- [Join Meeting Pattern](examples/join-meeting-pattern.md)
- [Start Meeting Pattern](examples/start-meeting-pattern.md)
- [Provider Hook Pattern](examples/provider-hook-pattern.md)

### References

- [Wrapper API](references/wrapper-api.md)
- [Android Setup](references/android-setup.md)
- [iOS Setup](references/ios-setup.md)
- [Native Bridge Notes](references/native-bridge-notes.md)
- [Official Sources](references/official-sources.md)

### Troubleshooting

- [Common Issues](troubleshooting/common-issues.md)
- [Version Drift](troubleshooting/version-drift.md)
- [Deprecated and Contradictions](troubleshooting/deprecated-and-contradictions.md)

## Operations

- [RUNBOOK.md](RUNBOOK.md) - 5-minute preflight and debugging checklist.
