---
name: x-openai-figma-swiftui-f38db47
description: SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a Figma design into SwiftUI (design → code), or pushing SwiftUI views / screens / tokens back into a Figma file (code → design). Triggers on phrases like 'implement this Figma design in SwiftUI', 'build this screen in Swift', 'push this SwiftUI view to Figma', 'mirror my Swift code in a Figma file', or whenever a Figma URL appears alongside `.swift` files / an `.xcodeproj`. Routes to a direction-specific reference doc; loads alongside `figma-use` for the code → design path.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Figma ↔ SwiftUI

Translation between Figma designs and SwiftUI code, both directions. This file is a router — actual guidance lives in the references below.

## Discover the Figma capabilities

Inspect the current host's available Figma MCP/API tools and their schemas first. Names such as `get_design_context`, `use_figma`, `get_metadata`, and `upload_assets` below are the original integration's capability identifiers, not guaranteed tools on every host. Use verified equivalents only when they provide the required node data, screenshots, symbol mappings, or authorized document writes. In particular, do not assume a read-only Figma REST connection can execute `use_figma` scripts or its helper extensions.

Resolve companion skills by their original role through the installed catalog/export manifest; the original sibling links in the references may need that mapping after export. When a required read capability or exact symbol/font mapping is missing, report the gap and use a user-provided design export only to the extent it supports the same evidence. When writes are unavailable, deliver local SwiftUI code, token mappings, and a design specification as applicable, clearly stating that the Figma file has not been updated. The workflow below and its references apply only to capabilities actually discovered.

## Pick the direction

| Direction | Trigger | Reference |
|---|---|---|
| **Design → code** | User wants SwiftUI in their iOS project from a Figma file/frame | [references/design-to-code.md](references/design-to-code.md) |
| **Code → design** | User wants to push SwiftUI views / screens / tokens into a Figma file | [references/code-to-design.md](references/code-to-design.md) |

If the request is ambiguous — a Figma URL and `.swift` files both present, no verb makes it clear — ask the user which direction before loading a reference.

## Shared context (applies to both directions)

These points hold regardless of direction; the direction-specific references assume them.

1. **`get_design_context` is the read tool for Figma.** Pass `clientLanguages: "swift"` and `clientFrameworks: "swiftui"` so the response is framed as Swift. URL → tool args: `figma.com/design/:fileKey/:fileName?node-id=:nodeId` → use `fileKey`, replace `-` with `:` in `nodeId`. For `figma.com/design/:fileKey/branch/:branchKey/:fileName`, use `branchKey` as `fileKey`.
2. **The React+Tailwind in `get_design_context` output is a structural reference, not a literal source.** It approximates the visual. Never transliterate `position: absolute` / pixel frames / `mix-blend-mode` stacks into SwiftUI or into Figma — the screenshot is the source of truth in both directions.
3. **iOS HIG semantic colors are tokens, not hex.** `var(--backgrounds/primary, …)`, `var(--labels/secondary, …)`, `var(--separators/non-opaque, …)` etc. map to `Color(.systemBackground)`, `Color.secondary`, `Color(.separator)` in SwiftUI, and to variables in a semantic collection in Figma. Keep the mapping; drop the literal RGBA.
4. **SF Symbols round-trip by name in both directions — never by codepoint.** Design → code: `get_design_context` substitutes Figma's SF Symbol glyph runs back into `<SFSymbol>{Image(systemName: "...")}</SFSymbol>` wrappers in the response. Use those names verbatim. Code → design: call `figma.util.getSfSymbolCharacter(name)` inside `use_figma` to convert a symbol name to the matching character — never look up codepoints by hand.
5. **Recognize the underlying iOS pattern, not the literal node / view name.** The same patterns recur in both directions: large title + back chevron + trailing action = `NavigationStack` chrome; bottom row of icon+label pairs = `TabView`; repeating same-height rows with leading/trailing chrome = `List`. Match those system patterns rather than rebuilding them from primitives.
6. **For code → design, `use_figma` is the API.** Always load [`figma-use`](../x-openai-figma-use-678d26c/SKILL.md) before any `use_figma` call. If the task involves building a full screen, also load [`figma-generate-design`](../x-openai-figma-generate-design-dc5f3d6/SKILL.md); if it involves building components or a design system, also load [`figma-generate-library`](../x-openai-figma-generate-library-7be021d/SKILL.md).

## References

| Doc | When to load |
|---|---|
| [references/design-to-code.md](references/design-to-code.md) | Translating a Figma design / frame into SwiftUI |
| [references/code-to-design.md](references/code-to-design.md) | Pushing SwiftUI views / screens / tokens into Figma |
