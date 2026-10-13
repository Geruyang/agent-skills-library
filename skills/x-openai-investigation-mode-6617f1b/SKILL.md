---
name: x-openai-investigation-mode-6617f1b
description: 'Orchestrated debugging coordinator. Triggers on frustration signals (stuck, hung, broken, waiting) and systematically triages: runtime logs → workflow status → browser verify → deploy/env. Reports findings at every step.'
metadata:
  priority: '8'
  docs: '[''https://openai.com/index/introducing-codex/'']'
  pathPatterns: '[''**/middleware.{ts,js,mjs}'', ''**/lib/logger.{ts,js}'', ''**/utils/logger.{ts,js}'', ''**/instrumentation.{ts,js}'', ''**/*.log'', ''**/error.{tsx,ts,js,jsx}'', ''**/global-error.{tsx,ts,js,jsx}'', ''**/not-found.{tsx,ts,js,jsx}'']'
  bashPatterns: '[''\\bvercel\\s+logs?\\b'', ''\\bvercel\\s+inspect\\b'', ''\\btail\\s+-f\\b.*\\.log'', ''\\bworkflow\\s+runs?\\b'', ''\\bvercel\\s+ls\\b'', ''\\bcurl\\s+-[vI]'']'
  importPatterns: '[]'
  promptSignals: '{''phrases'': [''nothing happened'', ''still waiting'', "it''s stuck", "it''s hung", ''nothing is happening'', ''not responding'', ''just sitting there'', ''just sits there'', ''seems frozen'', ''is it frozen'', ''frozen'', ''why is it hanging'', ''check the logs'', ''check logs'', ''where are the logs'', ''how do I debug'', ''how to debug'', ''white screen'', ''blank page'', ''spinning forever'', ''timed out'', ''keeps timing out'', ''no response'', ''no output'', ''not loading'', ''debug this'', ''investigate why'', ''what went wrong'', ''why did it fail'', ''why is it failing'', ''something is broken'', ''something broke'', ''seems broken'', ''check what happened'', ''check the status'', ''where is the error'', ''where did it fail'', ''find the error'', ''show me the error'', ''why is it slow'', ''taking forever'', ''still loading'', ''not finishing'', ''seems dead'', ''been waiting'', ''waiting forever'', ''stuck on'', ''hung up'', ''not progressing'', ''stalled out'', ''is it running'', ''did it crash'', ''keeps failing'', ''why no response'', ''where did it go'', ''lost connection'', ''never finishes'', ''pending forever'', ''queue stuck'', ''job stuck'', ''build stuck'', ''request hanging'', ''api not responding''], ''allOf'': [[''stuck'', ''workflow''], [''stuck'', ''deploy''], [''stuck'', ''loading''], [''stuck'', ''build''], [''stuck'', ''queue''], [''stuck'', ''job''], [''hung'', ''request''], [''hung'', ''api''], [''frozen'', ''page''], [''frozen'', ''app''], [''check'', ''why''], [''check'', ''broken''], [''check'', ''error''], [''check'', ''status''], [''check'', ''logs''], [''debug'', ''workflow''], [''debug'', ''deploy''], [''debug'', ''api''], [''debug'', ''issue''], [''investigate'', ''error''], [''logs'', ''error''], [''logs'', ''check''], [''slow'', ''response''], [''slow'', ''loading''], [''timeout'', ''api''], [''timeout'', ''request''], [''waiting'', ''response''], [''waiting'', ''forever''], [''waiting'', ''deploy''], [''not working'', ''why''], [''not'', ''responding''], [''hanging'', ''for''], [''been'', ''hanging''], [''been'', ''stuck''], [''been'', ''waiting''], [''why'', ''slow''], [''why'', ''failing''], [''why'', ''stuck''], [''why'', ''hanging''], [''job'', ''failing''], [''queue'', ''processing'']], ''anyOf'': [''stuck'', ''hung'', ''frozen'', ''broken'', ''failing'', ''timeout'', ''slow'', ''debug'', ''investigate'', ''check'', ''logs'', ''error'', ''hanging'', ''waiting'', ''stalled'', ''pending'', ''processing'', ''loading'', ''unresponsive''], ''noneOf'': [''css stuck'', ''sticky position'', ''position: sticky'', ''z-index'', ''sticky nav'', ''sticky header'', ''sticky footer'', ''overflow: hidden'', ''add a button'', ''create a button'', ''style the button''], ''minScore'': 4}'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Investigation Mode — Orchestrated Debugging

When a user reports something stuck, hung, broken, or not responding, you are the **diagnostic coordinator**. Do not guess. Follow the triage order, report what you find at every step, and stop when you have a high-confidence root cause.

## Reporting Contract

Every investigation step MUST follow this pattern:

1. **Tell the user what you are checking** — "I'm checking the runtime logs for errors…"
2. **Share the evidence you found** — paste the relevant log line, status, error, or screenshot
3. **Explain the next step** — "The logs show a timeout on the DB call. I'll check the connection pool next."

Never silently move between steps. The user is already frustrated — silence makes it worse.

## Triage Order

Work through these in order. Stop as soon as you find the root cause.

### 1. Runtime Logs (check first — most issues leave traces here)

- **Dev server**: Check terminal output for errors, warnings, unhandled rejections
- **Vercel logs**: `vercel logs --follow` (production) or `vercel logs <deployment-url>`
- **Browser console**: Open DevTools → Console tab for client-side errors
- **If no logs exist**: This is the problem. Add logging before continuing (see "Add Logging" below)

Tell the user: "Checking runtime logs…" → share what you found → explain next step.

### 2. Workflow / Background Job Status

If the app uses workflows, queues, or cron jobs:

- Run `vercel workflow runs list` to check recent run statuses
- Look for runs stuck in `running` state — likely a missing `await` or unresolved promise
- Check individual run details: `vercel workflow runs get <run-id>`
- Look for failed steps, retry exhaustion, or timeout errors

Tell the user: "Checking workflow run status…" → share the run state → explain next step.

### 3. Browser Verification

Use agent-browser to visually verify what the user sees:

- Take a screenshot of the current page state
- Check the browser console for JavaScript errors
- Check the Network tab for failed requests (4xx/5xx, CORS errors, hanging requests)
- Look for hydration mismatches or React error boundaries

Tell the user: "Taking a browser screenshot to see the current state…" → share the screenshot → explain what you see.

### 4. Deploy / Environment Status

- `vercel inspect <deployment-url>` — check build output, function regions, environment
- `vercel ls` — verify the latest deployment succeeded
- Check for environment variable mismatches between local and production
- Verify the correct branch/commit is deployed

Tell the user: "Checking deployment status…" → share the deployment state → explain findings.

## Stop Condition

**Stop investigating when:**
- You find a high-confidence root cause (specific error, missing env var, failed step, etc.)
- Two consecutive triage steps produce no signal — report what you checked and that you found no evidence, then ask the user for more context

**Do not** keep cycling through steps hoping something appears. If logs are empty and workflows look fine, say so and ask the user what they expected to happen.

## Common Hang Causes

When logs point to code issues, check for these frequent culprits:

- **Missing `await`**: Async functions called without await cause silent failures
- **Infinite loops**: `while(true)` without break conditions, recursive calls without base cases
- **Unresolved promises**: `new Promise()` that never calls `resolve()` or `reject()`
- **Missing env vars**: `process.env.X` returning `undefined` causing silent auth/DB failures
- **Connection pool exhaustion**: Database connections not being released
- **Middleware chains**: A middleware that never calls `next()` or returns a response
- **Timeout misconfigs**: Function timeout too short for the operation (check `vercel.json` maxDuration)

## Add Logging (If Missing)

If the investigation reveals insufficient observability, **add structured logging immediately** — you cannot debug what you cannot see.

```typescript
// API routes — wrap handlers with try/catch + logging
export async function POST(request: Request) {
  console.log('[api/route] incoming request', { method: 'POST', url: request.url });
  try {
    const result = await doWork();
    console.log('[api/route] success', { resultId: result.id });
    return Response.json(result);
  } catch (error) {
    console.error('[api/route] failed', { error: String(error), stack: (error as Error).stack });
    return Response.json({ error: 'Internal error' }, { status: 500 });
  }
}
```

```typescript
// Workflow steps — log entry/exit of every step
const result = await step.run('process-data', async () => {
  console.log('[workflow:process-data] step started');
  const data = await fetchData();
  console.log('[workflow:process-data] step completed', { count: data.length });
  return data;
});
```

**Key principle**: Every async boundary, every external call, every step entry/exit should have a log line. When something hangs, the last log line tells you exactly where it stopped.

> **Cross-reference**: For comprehensive logging setup (OpenTelemetry, log drains, Sentry, Vercel Analytics), see the **observability** skill. For workflow-specific debugging, see the **workflow** skill.
