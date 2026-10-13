---
name: x-openai-cron-jobs-8cb064d
description: Vercel Cron Jobs configuration and best practices. Use when adding, editing, or debugging scheduled tasks in vercel.json.
metadata:
  priority: '6'
  docs: '[''https://vercel.com/docs/cron-jobs'']'
  sitemap: https://vercel.com/sitemap/docs.xml
  pathPatterns: '[''vercel.json'', ''apps/*/vercel.json'']'
  bashPatterns: '[]'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Vercel Cron Jobs

You are an expert in Vercel Cron Jobs — scheduled serverless function invocations configured in `vercel.json`.

## Configuration

Cron jobs are defined in the `crons` array of `vercel.json`:

```json
{
  "crons": [
    {
      "path": "/api/cron/daily-digest",
      "schedule": "0 8 * * *"
    }
  ]
}
```

## Key Rules

1. **Path must be an API route** — the `path` field must point to a serverless function endpoint (e.g., `/api/cron/...`)
2. **Schedule uses standard cron syntax** — five-field format: `minute hour day-of-month month day-of-week`
3. **Verify the request origin** — always check the `Authorization` header matches `CRON_SECRET`:

```ts
// app/api/cron/route.ts
export async function GET(request: Request) {
  const authHeader = request.headers.get("authorization");
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response("Unauthorized", { status: 401 });
  }
  // ... your scheduled logic
  return Response.json({ ok: true });
}
```

4. **Hobby plan limits** — max 2 cron jobs, minimum interval of once per day
5. **Pro plan** — up to 40 cron jobs, minimum interval of once per minute
6. **Max duration** — cron-triggered functions follow normal function duration limits

## Common Patterns

- **Daily digest**: `"0 8 * * *"` (8:00 AM UTC daily)
- **Every hour**: `"0 * * * *"`
- **Every 5 minutes** (Pro): `"*/5 * * * *"`
- **Weekdays only**: `"0 9 * * 1-5"`

## Debugging

- Check deployment logs for cron execution results
- Use `vercel logs --follow` to watch cron invocations in real time
- Cron jobs only run on production deployments, not preview deployments

## References

- [Cron Jobs documentation](https://vercel.com/docs/cron-jobs)
