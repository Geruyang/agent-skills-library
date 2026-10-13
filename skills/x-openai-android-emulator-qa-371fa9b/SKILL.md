---
name: x-openai-android-emulator-qa-371fa9b
description: Use when validating Android feature flows in an emulator with adb-driven launch, input, UI-tree inspection, screenshots, and logcat capture.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Android Emulator QA

Validate Android app flows in an emulator using adb for launch, input, UI-tree inspection, screenshots, and logs.

## When to use
- QA a feature flow in an Android emulator.
- Reproduce UI bugs by driving navigation with adb input events.
- Capture screenshots and logcat output while testing.

## Quick start
1) List emulators and pick a serial:
   - `adb devices`
2) Build and install the target variant:
   - `./gradlew :<module>:install<BuildVariant> --console=plain --quiet`
   - If unsure about task names: `./gradlew tasks --all | rg install`
3) Launch the app:
   - Resolve activity: `adb -s <serial> shell cmd package resolve-activity --brief <package>`
   - Start app: `adb -s <serial> shell am start -n <package>/<activity>`
4) Capture a screenshot for visual verification:
   - `adb -s <serial> exec-out screencap -p > /tmp/emu.png`

## adb control commands
- Tap (use UI tree-derived coordinates):
  - `adb -s <serial> shell input tap <x> <y>`
- Swipe:
  - `adb -s <serial> shell input swipe <x1> <y1> <x2> <y2>`
  - Avoid edges (start ~150-200 px from left/right) to reduce accidental back gestures.
- Text:
  - `adb -s <serial> shell input text "hello"`
- Back:
  - `adb -s <serial> shell input keyevent 4`
- UI tree dump:
  - `adb -s <serial> exec-out uiautomator dump /dev/tty`

## Coordinate picking (UI tree only)
Always compute tap coordinates from the UI tree, not screenshots.

1) Dump the UI tree to a step-specific file:
   - `adb -s <serial> exec-out uiautomator dump /dev/tty > /tmp/ui-settings.xml`
2) Find the target node and derive center coordinates (`x y`) from bounds:
   - Bounds format: `bounds="[x1,y1][x2,y2]"`
   - Helper script:
   - `python3 <path-to-skill>/scripts/ui_pick.py /tmp/ui-settings.xml "Settings"`
3) If the node is missing and there are `scrollable` elements:
   - swipe, re-dump, and re-search at least once before concluding the target is missing.
4) Tap the center:
   - `adb -s <serial> shell input tap <x> <y>`

## UI tree skeleton (helper)
Use this helper to create a compact, readable overview before inspecting full XML.

1) Dump full UI tree:
   - `adb -s <serial> exec-out uiautomator dump /dev/tty > /tmp/ui-full.xml`
2) Generate summary:
   - `python3 <path-to-skill>/scripts/ui_tree_summarize.py /tmp/ui-full.xml /tmp/ui-summary.txt`
3) Review `/tmp/ui-summary.txt` to choose likely targets, then compute exact bounds from full XML.

## Logs (logcat)
1) Clear logs:
   - `adb -s <serial> logcat -c`
2) Stream app process logs:
   - Resolve pid: `adb -s <serial> shell pidof -s <package>`
   - Stream: `adb -s <serial> logcat --pid <pid>`
3) Crash buffer only:
   - `adb -s <serial> logcat -b crash`
4) Save logs:
   - `adb -s <serial> logcat -d > /tmp/logcat.txt`

## Package shortcuts
- List installed packages:
  - `adb -s <serial> shell pm list packages`
- Filter to your namespace:
  - `adb -s <serial> shell pm list packages | rg <company_or_app_id>`
- Confirm the activity resolves before launching:
  - `adb -s <serial> shell cmd package resolve-activity --brief <package>`
