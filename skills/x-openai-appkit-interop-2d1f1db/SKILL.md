---
name: x-openai-appkit-interop-2d1f1db
description: Bridge macOS SwiftUI into AppKit narrowly. Use when implementing representables, reaching NSWindow or panels, handling menus, or using the responder chain.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# AppKit Interop

## Quick Start

Use this skill when SwiftUI is close but not quite enough for native macOS behavior.
Keep the bridge as small and explicit as possible. SwiftUI should usually remain
the source of truth, while AppKit handles the imperative edge.

## Choose The Smallest Bridge

- Use pure SwiftUI when the required behavior already exists in scenes, toolbars, commands, inspectors, or standard controls.
- Use `NSViewRepresentable` when you need a specific AppKit view with lightweight lifecycle needs.
- Use `NSViewControllerRepresentable` when you need controller lifecycle, delegation, or presentation coordination.
- Use direct AppKit window or app hooks when you need `NSWindow`, responder-chain, menu validation, panels, or app-level behavior.

## Workflow

1. Name the capability gap precisely.
   - Window behavior
   - Text system behavior
   - Menu validation
   - Drag and drop
   - File open/save panels
   - First responder control

2. Pick the smallest boundary that solves it.
   - Avoid porting a whole screen to AppKit when one wrapped control or coordinator would do.

3. Keep ownership explicit.
   - SwiftUI owns value state, selection, and observable models.
   - AppKit objects stay inside the representable, coordinator, or bridge object.

4. Expose a narrow interface back to SwiftUI.
   - Bindings for editable state
   - Small callbacks for events
   - Focused bridge services only when necessary

5. Validate lifecycle assumptions.
   - SwiftUI may recreate representables.
   - Coordinators exist to hold delegate and target-action glue, not as a second app architecture.

## References

- `references/representables.md`: choosing between view and view-controller wrappers, plus coordinator patterns.
- `references/window-panels.md`: window access, utility windows, and open/save panels.
- `references/responder-menus.md`: first responder, command routing, and menu validation.
- `references/drag-drop-pasteboard.md`: pasteboard, file URLs, and desktop drag/drop edges.

## Guardrails

- Do not duplicate the source of truth between SwiftUI and AppKit.
- Do not let `Coordinator` become an unstructured dumping ground.
- Do not store long-lived `NSView` or `NSWindow` instances globally without a strong ownership reason.
- Prefer a tiny tested bridge over rewriting the feature in raw AppKit.
- If a pattern can remain entirely in `swiftui-patterns`, keep it there.

## Output Expectations

Provide:
- the exact SwiftUI limitation being crossed
- the smallest recommended bridge type
- the data-flow boundary between SwiftUI and AppKit
- the lifecycle or validation risks to watch
