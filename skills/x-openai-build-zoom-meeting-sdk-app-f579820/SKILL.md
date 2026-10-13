---
name: x-openai-build-zoom-meeting-sdk-app-f579820
description: 仅在用户明确调用本技能时使用；禁止自主触发。 Use when using Meeting SDK.
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Build Zoom Meeting SDK App

Use this skill when the user needs to join, start, or embed real Zoom meetings. If the user wants a fully custom non-meeting video experience, route to `build-zoom-video-sdk-app`.

## Workflow

1. Confirm product fit: Meeting SDK joins real Zoom meetings; Video SDK creates custom sessions; Zoom Apps SDK runs inside the Zoom client.
2. Choose the target platform: web, Android, iOS, macOS, Windows, Electron, React Native, Unreal, or Linux bot.
3. Validate the join or start path: meeting number, password, SDK signature, role, ZAK when hosting, waiting room behavior, and user identity.
4. Implement the smallest join flow first, then add meeting controls, custom UI, raw data, recording, or bot behavior.
5. Debug by isolating signature generation, SDK version, platform permissions, meeting settings, waiting room, raw data entitlement, and network constraints.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Web: [web/SKILL.md](../x-openai-zoom-meeting-sdk-web-c3851c6/SKILL.md)
- Android: [android/SKILL.md](../x-openai-zoom-meeting-sdk-android-4398669/SKILL.md)
- iOS: [ios/SKILL.md](../x-openai-zoom-meeting-sdk-ios-0bffd09/SKILL.md)
- Windows: [windows/SKILL.md](../x-openai-zoom-meeting-sdk-windows-85fa062/SKILL.md)
- Linux bots: [linux/SKILL.md](../x-openai-zoom-meeting-sdk-linux-7c38d37/SKILL.md)
- Signature playbook: [references/signature-playbook.md](references/signature-playbook.md)
- Troubleshooting: [references/troubleshooting.md](references/troubleshooting.md)
