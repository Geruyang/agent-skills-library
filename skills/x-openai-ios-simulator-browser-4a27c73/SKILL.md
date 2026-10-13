---
name: x-openai-ios-simulator-browser-4a27c73
description: Mirror an iOS Simulator into an available local browser and render SwiftUI previews from importable Swift packages in that simulator with hot reload. Use when a user wants to watch or interact with an iOS app in the browser, see a SwiftUI preview outside Xcode Canvas, iterate live on a preview, or capture browser-visible simulator proof.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# iOS Simulator Browser

## Browser Workflow

1. Obtain an explicit Simulator UDID from the existing iOS build/run workflow or from `xcrun simctl list devices available`.
2. Start `serve-sim` in a long-running terminal pinned to that simulator. Clean up any tracked stale helper for this simulator before starting, and install a trap so the helper is cleaned up when this terminal exits:

   ```bash
   SIM="<simulator-udid>"
   cleanup_serve_sim() {
     npx --yes serve-sim@latest --kill "$SIM" >/dev/null 2>&1 || true
   }
   trap cleanup_serve_sim EXIT INT TERM HUP
   cleanup_serve_sim
   npx --yes serve-sim@latest "$SIM"
   ```

3. Open the exact local preview URL printed by `serve-sim` in an available local browser.
4. Verify that a real frame is rendering before reporting success. A loaded page alone is not proof that the simulator stream is healthy.

- Keep the terminal alive while the browser mirror is in use. When finished, stop the terminal and wait for it to exit so the trap runs.
- If the terminal disappeared or did not exit cleanly, run `npx --yes serve-sim@latest --kill "$SIM"` before starting another mirror for that simulator.
- Never run an unscoped `serve-sim --kill`; another thread may own a different simulator mirror.

## SwiftUI Preview Workflow

Use the bundled launcher when the requested previews live in an importable Swift package. Point it at the package manifest and select the target whose previews should be displayed. It generates a disposable host project outside the user's source tree, installs and launches that host in Simulator, and watches the package for edits.

```bash
node <skill-root>/scripts/swiftui-preview-browser.mjs \
  /absolute/path/to/Package.swift \
  --package-target "<target>" \
  --device "<simulator-udid>"
```

- Watch mode is enabled by default. On a Swift package source edit, the launcher rebuilds a generated dylib and hot-swaps it into the running host without relaunching the app.
- The generated host shows every preview variant discovered in the selected Swift Package target with in-simulator page controls. To show a subset instead, pass `--preview-filter <regex[, ...]>`; it matches display names and code identifiers such as `StatusRowView_Previews`.
- Once the launcher prints the selected Simulator UDID, start `serve-sim` for that same UDID and open its printed URL in the available browser.

## Support Boundary

- Support Swift Package-backed `PreviewProvider` and `#Preview` declarations through the generated host.
- Do not edit the user's `.xcodeproj`, `.xcworkspace`, `Package.swift`, schemes, or build settings to force preview support.

## Proof

For browser or preview QA, capture a browser screenshot showing the simulator frame. For hot reload QA, also report the launcher's `hot reloaded package preview ... in pid ...` output and show the changed frame after editing.
