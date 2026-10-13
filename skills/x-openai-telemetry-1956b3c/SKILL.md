---
name: x-openai-telemetry-1956b3c
description: Add and verify lightweight macOS runtime telemetry. Use when wiring Logger events or inspecting logs for windows, sidebars, menus, and actions.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Telemetry

## Quick Start

Use this skill to add lightweight app instrumentation that helps debug behavior
without turning the codebase into a logging landfill. Prefer Apple's unified
logging APIs and verify the events after a build/run loop.

## Core Guidelines

- Prefer `Logger` from the `OSLog` framework for structured app logs.
- Give each feature a clear subsystem/category pair so runtime filtering stays easy.
- Log meaningful user and app lifecycle events: window opening, sidebar selection changes, menu commands, menu bar extra actions, sync/load milestones, and unexpected fallback paths.
- Keep info logs concise and stable. Use debug logs for noisy state details.
- Do not log secrets, auth tokens, personal data, or raw document contents.
- Add signposts only when measuring timing or performance spans; do not overinstrument by default.

## Minimal Logger Pattern

```swift
import OSLog

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}
```

Use feature-specific categories like `Windowing`, `Commands`, `MenuBar`, `Sidebar`,
`Sync`, or `Import` so logs can be filtered quickly.

## Workflow

1. Identify the behavior that needs observability.
   - Window open/close
   - Sidebar or inspector selection changes
   - Menu or keyboard command actions
   - Menu bar extra actions
   - Background load/sync/import events
   - Error and recovery paths

2. Add the smallest useful instrumentation.
   - Create one `Logger` per feature area or type.
   - Log action boundaries and key state transitions.
   - Prefer one high-signal line per user action over noisy value dumps.

3. Build and run the app.
   - Use `build-run-debug` for the build/run loop.
   - If `script/build_and_run.sh` exists, prefer `./script/build_and_run.sh --telemetry` for live telemetry checks or `./script/build_and_run.sh --logs` for broader process logs.
   - Exercise the UI or command path that should emit telemetry.

4. Read runtime logs and verify the event fired.
   - Use Console.app with a process/subsystem filter when that is the fastest manual check.
   - Use `log stream --style compact --predicate 'process == "AppName"'` for live terminal verification.
   - Prefer tighter predicates when you know the subsystem/category:
     `log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'`

5. Tighten or remove instrumentation.
   - If the event fires, keep only the logs that remain useful for future debugging.
   - If it does not fire, move the log closer to the suspected control path and rerun.

## Verification Checklist

- The app builds after telemetry changes.
- The relevant action emits exactly one clear log line or a small bounded sequence.
- The log can be filtered by process, subsystem, or category.
- No sensitive payloads are written to unified logs.
- Noisy temporary debug logs are removed or demoted before finishing.

## Guardrails

- Do not use `print` as the primary app telemetry mechanism for macOS app code.
- Do not leave a dense trail of permanent debug logs around every state mutation.
- Do not claim an event is wired correctly until you have a concrete verification path through Console, `log stream`, or captured process output.
- If the debugging task is mostly about crash/backtrace analysis rather than action telemetry, switch to `build-run-debug`.
