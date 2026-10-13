---
name: x-openai-runtime-cache-5e95fce
description: Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, Routing Middleware, and Builds. Use when implementing caching strategies beyond framework-level caching.
metadata:
  priority: '6'
  docs: '[''https://nextjs.org/docs/app/building-your-application/caching'']'
  sitemap: https://nextjs.org/sitemap.xml
  pathPatterns: '[''lib/cache/**'', ''src/lib/cache/**'', ''lib/cache.*'', ''src/lib/cache.*'']'
  bashPatterns: '[''\\bnpm\\s+(install|i|add)\\s+[^\\n]*@vercel/functions\\b'', ''\\bpnpm\\s+(install|i|add)\\s+[^\\n]*@vercel/functions\\b'', ''\\bbun\\s+(install|i|add)\\s+[^\\n]*@vercel/functions\\b'', ''\\byarn\\s+add\\s+[^\\n]*@vercel/functions\\b'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Vercel Runtime Cache API

You are an expert in the Vercel Runtime Cache — an ephemeral caching layer for serverless compute.

## What It Is

The Runtime Cache is a **per-region key-value store** accessible from Vercel Functions, Routing Middleware, and Builds. It supports **tag-based invalidation** for granular cache control.

- **Regional**: Each Vercel region has its own isolated cache
- **Isolated**: Scoped per project AND per deployment environment (`preview` vs `production`)
- **Persistent across deployments**: Cached data survives new deploys; invalidation via TTL or `expireTag`
- **Ephemeral**: Fixed storage limit per project; LRU eviction when full
- **Framework-agnostic**: Works with any framework via `@vercel/functions`

## Key APIs

All APIs from `@vercel/functions`:

### Basic Cache Operations

```ts
import { getCache } from '@vercel/functions';

const cache = getCache();

// Store data with TTL and tags
await cache.set('user:123', userData, {
  ttl: 3600,                      // seconds
  tags: ['users', 'user:123'],    // for bulk invalidation
  name: 'user-profile',           // human-readable label for observability
});

// Retrieve cached data (returns value or undefined)
const data = await cache.get('user:123');

// Delete a specific key
await cache.delete('user:123');

// Expire all entries with a tag (propagates globally within 300ms)
await cache.expireTag('users');
await cache.expireTag(['users', 'user:123']); // multiple tags
```

### Cache Options

```ts
const cache = getCache({
  namespace: 'api',                    // prefix for keys
  namespaceSeparator: ':',             // separator (default)
  keyHashFunction: (key) => sha256(key), // custom key hashing
});
```

### Full Example (Framework-Agnostic)

```ts
import { getCache } from '@vercel/functions';

export default {
  async fetch(request: Request) {
    const cache = getCache();
    const cached = await cache.get('blog-posts');

    if (cached) {
      return Response.json(cached);
    }

    const posts = await fetch('https://api.example.com/posts').then(r => r.json());

    await cache.set('blog-posts', posts, {
      ttl: 3600,
      tags: ['blog'],
    });

    return Response.json(posts);
  },
};
```

### Tag Expiration from Server Action

```ts
'use server';
import { getCache } from '@vercel/functions';

export async function invalidateBlog() {
  await getCache().expireTag('blog');
}
```

## CDN Cache Purging Functions

These purge across **all three cache layers** (CDN + Runtime Cache + Data Cache):

```ts
import { invalidateByTag, dangerouslyDeleteByTag } from '@vercel/functions';

// Stale-while-revalidate: serves stale, revalidates in background
await invalidateByTag('blog-posts');

// Hard delete: next request blocks while fetching from origin (cache stampede risk)
await dangerouslyDeleteByTag('blog-posts', {
  revalidationDeadlineSeconds: 3600,
});
```

**Important distinction**:
- `cache.expireTag()` — operates on Runtime Cache only
- `invalidateByTag()` / `dangerouslyDeleteByTag()` — purges CDN + Runtime + Data caches

## Next.js Integration

### Next.js 16+ (`use cache: remote`)

```ts
// next.config.ts
const nextConfig: NextConfig = { cacheComponents: true };
```

```ts
import { cacheLife, cacheTag } from 'next/cache';

async function getData() {
  'use cache: remote'     // stores in Vercel Runtime Cache
  cacheTag('example-tag')
  cacheLife({ expire: 3600 })
  return fetch('https://api.example.com/data').then(r => r.json());
}
```

- `'use cache'` (no `: remote`) — in-memory only, ephemeral per instance
- `'use cache: remote'` — stores in Vercel Runtime Cache

### Next.js 16 Invalidation APIs

| Function | Context | Behavior |
|----------|---------|----------|
| `updateTag(tag)` | Server Actions only | Immediate expiration, read-your-own-writes |
| `revalidateTag(tag, 'max')` | Server Actions + Route Handlers | Stale-while-revalidate (recommended) |
| `revalidateTag(tag, { expire: 0 })` | Route Handlers (webhooks) | Immediate expiration from external triggers |

**Important**: Single-argument `revalidateTag(tag)` is deprecated in Next.js 16. Always pass a `cacheLife` profile as the second argument.

### Runtime Cache vs ISR Isolation

- Runtime Cache tags do **NOT** apply to ISR pages
- `cache.expireTag` does **NOT** invalidate ISR cache
- Next.js `revalidatePath` / `revalidateTag` does **NOT** invalidate Runtime Cache
- To manage both, use same tag and purge via `invalidateByTag` (hits all cache layers)

## CLI Cache Commands

```bash
# Purge all cached data
vercel cache purge                    # CDN + Data cache
vercel cache purge --type cdn         # CDN only
vercel cache purge --type data        # Data cache only
vercel cache purge --yes              # skip confirmation

# Invalidate by tag (stale-while-revalidate)
vercel cache invalidate --tag blog-posts,user-profiles

# Hard delete by tag (blocks until revalidated)
vercel cache dangerously-delete --tag blog-posts
vercel cache dangerously-delete --tag blog-posts --revalidation-deadline-seconds 3600

# Image invalidation
vercel cache invalidate --srcimg /images/hero.jpg
```

Note: `--tag` and `--srcimg` cannot be used together.

## CDN Cache Tags

Add tags to CDN cached responses for later invalidation:

```ts
import { addCacheTag } from '@vercel/functions';

// Via helper
addCacheTag('product-123');

// Via response header
return Response.json(product, {
  headers: {
    'Vercel-CDN-Cache-Control': 'public, max-age=86400',
    'Vercel-Cache-Tag': 'product-123,products',
  },
});
```

## Limits

| Property | Limit |
|----------|-------|
| Item size | 2 MB |
| Tags per Runtime Cache item | 64 |
| Tags per CDN item | 128 |
| Max tag length | 256 bytes |
| Tags per bulk REST API call | 16 |

Tags are **case-sensitive** and **cannot contain commas**.

## Observability

Monitor hit rates, invalidation patterns, and storage usage in the Vercel Dashboard under **Observability → Runtime Cache**. The CDN dashboard (March 5, 2026) provides a unified view of global traffic distribution, cache performance metrics, a redesigned purging interface, and **project-level routing** — update response headers or rewrite to external APIs without triggering a new deployment. Project-level routes are available on all plans and take effect instantly.

## When to Use

- Caching API responses or computed data across functions in a region
- Tag-based invalidation when content changes (CMS webhook → expire tag)
- Reducing database load for frequently accessed data
- Cross-function data sharing within a region

## When NOT to Use

- Framework-level page caching → use Next.js Cache Components (`'use cache'`)
- Persistent storage → use a database (Neon, Upstash)
- CDN-level full response caching → use `Cache-Control` / `Vercel-CDN-Cache-Control` headers
- Cross-region shared state → use a database
- User-specific data that differs per request

## References

- 📖 docs: https://vercel.com/docs/runtime-cache
- 📖 changelog: https://vercel.com/changelog/introducing-the-runtime-cache-api
- 📖 CLI cache: https://vercel.com/docs/cli/cache
- 📖 CDN cache purging: https://vercel.com/docs/cdn-cache/purge
