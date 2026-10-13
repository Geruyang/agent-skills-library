---
name: x-openai-agent-browser-ee27e33
description: Browser automation CLI for AI agents. Use when the user needs to interact with websites, verify dev server output, test web apps, navigate pages, fill forms, click buttons, take screenshots, extract data, or automate any browser task. Also triggers when a dev server starts so you can verify it visually.
metadata:
  priority: '3'
  docs: '[''https://openai.com/index/introducing-codex/'']'
  pathPatterns: '[''agent-browser.json'', ''playwright.config.*'', ''e2e/**'', ''tests/e2e/**'', ''test/e2e/**'', ''cypress/**'', ''cypress.config.*'']'
  bashPatterns: '[''\\bagent-browser\\b'', ''\\bnext\\s+dev\\b'', ''\\bnpm\\s+run\\s+dev\\b'', ''\\bpnpm\\s+dev\\b'', ''\\bbun\\s+run\\s+dev\\b'', ''\\byarn\\s+dev\\b'', ''\\bvite\\b'', ''\\bnuxt\\s+dev\\b'', ''\\bvercel\\s+dev\\b'', ''\\blocalhost:\\d+'', ''\\b127\\.0\\.0\\.1:\\d+'', ''\\bcurl\\s+.*localhost'', ''\\bopen\\s+https?://'', ''\\bplaywright\\b'', ''\\bcypress\\b'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Browser Automation with agent-browser

When a dev server is running or the user asks to verify, test, or interact with a web page, use `agent-browser` to automate the browser.

## Core Workflow

Every browser automation follows this pattern:

1. **Navigate**: `agent-browser open <url>`
2. **Snapshot**: `agent-browser snapshot -i` (get element refs like `@e1`, `@e2`)
3. **Interact**: Use refs to click, fill, select
4. **Re-snapshot**: After navigation or DOM changes, get fresh refs

```bash
agent-browser open http://localhost:3000
agent-browser wait --load networkidle
agent-browser snapshot -i
```

## Dev Server Verification

When a dev server starts, use agent-browser to verify it's working:

```bash
# After starting a dev server (next dev, vite, etc.)
agent-browser open http://localhost:3000
agent-browser wait --load networkidle
agent-browser screenshot dev-check.png
agent-browser snapshot -i
```

## Command Chaining

Commands can be chained with `&&`. The browser persists between commands via a background daemon.

```bash
agent-browser open http://localhost:3000 && agent-browser wait --load networkidle && agent-browser snapshot -i
```

## Essential Commands

```bash
# Navigation
agent-browser open <url>              # Navigate (aliases: goto, navigate)
agent-browser close                   # Close browser

# Snapshot
agent-browser snapshot -i             # Interactive elements with refs
agent-browser snapshot -i -C          # Include cursor-interactive elements
agent-browser snapshot -s "#selector" # Scope to CSS selector

# Interaction (use @refs from snapshot)
agent-browser click @e1               # Click element
agent-browser fill @e2 "text"         # Clear and type text
agent-browser type @e2 "text"         # Type without clearing
agent-browser select @e1 "option"     # Select dropdown option
agent-browser check @e1               # Check checkbox
agent-browser press Enter             # Press key
agent-browser scroll down 500         # Scroll page

# Get information
agent-browser get text @e1            # Get element text
agent-browser get url                 # Get current URL
agent-browser get title               # Get page title

# Wait
agent-browser wait @e1                # Wait for element
agent-browser wait --load networkidle # Wait for network idle
agent-browser wait --url "**/page"    # Wait for URL pattern
agent-browser wait 2000               # Wait milliseconds

# Capture
agent-browser screenshot              # Screenshot to temp dir
agent-browser screenshot --full       # Full page screenshot
agent-browser screenshot --annotate   # Annotated screenshot with numbered labels
agent-browser pdf output.pdf          # Save as PDF

# Diff (compare page states)
agent-browser diff snapshot           # Compare current vs last snapshot
agent-browser diff screenshot --baseline before.png  # Visual pixel diff
```

## Common Patterns

### Form Submission

```bash
agent-browser open http://localhost:3000/signup
agent-browser snapshot -i
agent-browser fill @e1 "Jane Doe"
agent-browser fill @e2 "jane@example.com"
agent-browser click @e5
agent-browser wait --load networkidle
```

### Authentication with State Persistence

```bash
# Login once and save state
agent-browser open http://localhost:3000/login
agent-browser snapshot -i
agent-browser fill @e1 "$USERNAME"
agent-browser fill @e2 "$PASSWORD"
agent-browser click @e3
agent-browser wait --url "**/dashboard"
agent-browser state save auth.json

# Reuse in future sessions
agent-browser state load auth.json
agent-browser open http://localhost:3000/dashboard
```

### Data Extraction

```bash
agent-browser open http://localhost:3000/products
agent-browser snapshot -i
agent-browser get text @e5
agent-browser get text body > page.txt
```

### Visual Debugging

```bash
agent-browser --headed open http://localhost:3000
agent-browser highlight @e1
agent-browser record start demo.webm
```

## Ref Lifecycle (Important)

Refs (`@e1`, `@e2`, etc.) are invalidated when the page changes. Always re-snapshot after:

- Clicking links or buttons that navigate
- Form submissions
- Dynamic content loading (dropdowns, modals)

```bash
agent-browser click @e5              # Navigates to new page
agent-browser snapshot -i            # MUST re-snapshot
agent-browser click @e1              # Use new refs
```

## Annotated Screenshots (Vision Mode)

Use `--annotate` for screenshots with numbered labels on interactive elements:

```bash
agent-browser screenshot --annotate
# Output: [1] @e1 button "Submit", [2] @e2 link "Home", ...
agent-browser click @e2
```

## Semantic Locators (Alternative to Refs)

```bash
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "user@test.com"
agent-browser find role button click --name "Submit"
```

## JavaScript Evaluation

```bash
# Simple expressions
agent-browser eval 'document.title'

# Complex JS: use --stdin with heredoc
agent-browser eval --stdin <<'EVALEOF'
JSON.stringify(
  Array.from(document.querySelectorAll("img"))
    .filter(i => !i.alt)
    .map(i => ({ src: i.src.split("/").pop(), width: i.width }))
)
EVALEOF
```

## Session Management

```bash
agent-browser --session site1 open http://localhost:3000
agent-browser --session site2 open http://localhost:3001
agent-browser session list
agent-browser close  # Always close when done
```

## Timeouts and Slow Pages

```bash
agent-browser wait --load networkidle  # Best for slow pages
agent-browser wait "#content"          # Wait for specific element
agent-browser wait --url "**/dashboard"  # Wait for URL pattern
agent-browser wait 5000                # Fixed wait (last resort)
```
