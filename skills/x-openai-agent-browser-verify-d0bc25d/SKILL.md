---
name: x-openai-agent-browser-verify-d0bc25d
description: Automated browser verification for dev servers. Triggers when a dev server starts to run a visual gut-check with agent-browser — verifies the page loads, checks for console errors, validates key UI elements, and reports pass/fail before continuing.
metadata:
  priority: '2'
  docs: '[''https://openai.com/index/introducing-codex/'']'
  pathPatterns: '[]'
  bashPatterns: '[''\\bnext\\s+dev\\b'', ''\\bnpm\\s+run\\s+dev\\b'', ''\\bpnpm\\s+dev\\b'', ''\\bbun\\s+run\\s+dev\\b'', ''\\byarn\\s+dev\\b'', ''\\bvite\\s*(dev)?\\b'', ''\\bnuxt\\s+dev\\b'', ''\\bvercel\\s+dev\\b'']'
  promptSignals: '{''phrases'': [''check the page'', ''check the browser'', ''check the site'', ''is the page working'', ''is it loading'', ''blank page'', ''white screen'', ''nothing showing'', ''page is broken'', ''screenshot the page'', ''take a screenshot'', ''check for errors'', ''console errors'', ''browser errors'', ''page is stuck'', ''page is hanging'', ''page not loading'', ''page frozen'', ''spinner not stopping'', ''page not responding'', "page won''t load", ''page will not load'', ''nothing renders'', ''nothing rendered'', ''ui is broken'', ''screen is blank'', ''screen is white'', "app won''t load"], ''allOf'': [[''check'', ''page''], [''check'', ''browser''], [''check'', ''site''], [''blank'', ''page''], [''white'', ''screen''], [''console'', ''errors''], [''page'', ''broken''], [''page'', ''loading''], [''not'', ''rendering''], [''page'', ''stuck''], [''page'', ''hanging''], [''page'', ''frozen''], [''page'', ''timeout'']], ''anyOf'': [''page'', ''browser'', ''screen'', ''rendering'', ''visual'', ''spinner'', ''loading''], ''minScore'': 6}'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Dev Server Verification with agent-browser

**You MUST verify the dev server in a real browser after starting it.** Prefer the installed `agent-browser` CLI and inspect its current help before using the examples below. If it is unavailable, use an actually connected browser MCP or installed automation library such as Playwright that provides navigation, screenshots, DOM/accessible snapshots, and console capture. Map those operations to its documented schema; do not call an invented host tool. If no equivalent browser capability is available, report browser verification as blocked. Do not assume the page works just because the dev server process started. Many issues (blank pages, hydration errors, missing env vars, broken imports) are only visible in the browser. Run this verification before continuing with any other work:

Read the actual reachable URL from the server output or project configuration; `http://localhost:3000` below is only an example. Remote browser sessions may need an authorized forwarded URL. Save screenshots in the current project's selected artifact directory and close only the browser session created for this check. Use backend-specific log commands below only when that backend and CLI are actually present.

## Quick Verification Flow

```bash
# 1. Open the dev server
agent-browser open http://localhost:3000
agent-browser wait --load networkidle

# 2. Screenshot for visual check
agent-browser screenshot --annotate

# 3. Inspect an application-provided error buffer, if it exists.
# Also capture browser console/pageerror events through the chosen browser tool.
# An absent __consoleErrors buffer is NOT evidence of a clean console.
agent-browser eval 'JSON.stringify(window.__consoleErrors || [])'

# 4. Snapshot interactive elements
agent-browser snapshot -i
```

## Verification Checklist

Run each check and report results:

1. **Page loads** — `agent-browser open` succeeds without timeout
2. **No blank page** — snapshot shows meaningful content (not empty body)
3. **No error overlay** — no Next.js/Vite error overlay detected
4. **Console errors** — capture console and page-error events through the browser tool; report unavailable capture as unverified. Error-overlay DOM checks are additional evidence, not a substitute for console capture.
5. **Key elements render** — snapshot `-i` shows expected interactive elements
6. **Navigation works** — if multiple routes exist, verify at least the home route

## Error Detection

```bash
# Check for framework error overlays
agent-browser eval 'document.querySelector("[data-nextjs-dialog], .vite-error-overlay, #webpack-dev-server-client-overlay") ? "ERROR_OVERLAY" : "OK"'

# Check page isn't blank
agent-browser eval 'document.body.innerText.trim().length > 0 ? "HAS_CONTENT" : "BLANK"'
```

## On Failure

If verification fails:

1. Screenshot the error state: `agent-browser screenshot error-state.png`
2. Capture the error overlay text or console output
3. Close the browser: `agent-browser close`
4. Fix the issue in code
5. Re-run verification (max 2 retry cycles to avoid infinite loops)

## Diagnosing a Hanging or Stuck Page

When the page appears stuck (spinner, blank content after load, frozen UI), the browser is only half the story. Correlate what you see in the browser with server-side evidence:

### 1. Capture Browser Evidence

```bash
# Screenshot the stuck state
agent-browser screenshot stuck-state.png

# Check for pending network requests (XHR/fetch that never resolved)
agent-browser eval 'JSON.stringify(performance.getEntriesByType("resource").filter(r => r.duration === 0).map(r => r.name))'

# Check console for errors or warnings
agent-browser eval 'JSON.stringify(window.__consoleErrors || [])'

# Look for fetch calls to workflow/API routes that are pending
agent-browser eval 'document.querySelector("[data-nextjs-dialog]") ? "ERROR_OVERLAY" : "OK"'
```

### 2. Check Server Logs

After capturing browser state, immediately check the backend:

```bash
# Stream Vercel runtime logs for the deployment
vercel logs --follow

# If using Workflow DevKit, check run status
npx workflow inspect runs
npx workflow inspect run <run_id>

# Check workflow health
npx workflow health
```

### 3. Correlate Browser + Server

| Browser Shows | Server Shows | Likely Issue |
|--------------|-------------|-------------|
| Spinner / loading forever | No recent function invocations | API route not being called — check fetch URL in client code |
| Spinner / loading forever | Function started but no step logs | Workflow step is stuck — add `console.log` at step entry/exit |
| Blank page, no errors | Build succeeded, no runtime errors | Hydration issue or missing data — check SSR vs client rendering |
| Network request pending | 504 Gateway Timeout in logs | Function timeout — increase `maxDuration` or optimize step |
| Console: "Failed to fetch" | OIDC/credential error in logs | Missing `vercel env pull` — run `vercel link && vercel env pull` |
| Error overlay visible | Stack trace in runtime logs | Read the server error — it usually has more detail than the client |

### 4. Fix and Re-verify

After fixing the issue:

```bash
# Re-open and verify the fix
agent-browser open http://localhost:3000
agent-browser wait --load networkidle
agent-browser screenshot after-fix.png
agent-browser eval 'document.body.innerText.trim().length > 0 ? "HAS_CONTENT" : "BLANK"'
agent-browser close
```

## On Success

```bash
agent-browser close
```

Report the checks actually completed: page load, meaningful content, overlays, console capture, and key UI elements. Use "Dev server verified — page loads, no errors detected, key UI elements render correctly" only when all those checks passed; explicitly name skipped or blocked checks.

## Suggest Verification After Implementation

When you finish building or implementing a feature (wrote code, created routes, set up a project), briefly let the user know they can ask you to verify everything works with a browser check. One sentence is enough. Don't force it if only a small fix or question was involved.
