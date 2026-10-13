---
name: x-openai-swr-8f69c32
description: SWR data-fetching expert guidance. Use when building React apps with client-side data fetching, caching, revalidation, mutations, optimistic UI, pagination, or infinite loading using the SWR library.
metadata:
  priority: '4'
  docs: '[''https://swr.vercel.app/docs'']'
  sitemap: https://swr.vercel.app/sitemap.xml
  pathPatterns: '[''lib/fetcher.*'', ''src/lib/fetcher.*'', ''utils/fetcher.*'', ''src/utils/fetcher.*'', ''hooks/use*SWR*'', ''src/hooks/use*SWR*'', ''hooks/useFetch*'', ''src/hooks/useFetch*'']'
  importPatterns: '[''swr'', ''swr/*'']'
  bashPatterns: '[''\\bnpm\\s+(install|i|add)\\s+[^\\n]*\\bswr\\b'', ''\\bpnpm\\s+(install|i|add)\\s+[^\\n]*\\bswr\\b'', ''\\bbun\\s+(install|i|add)\\s+[^\\n]*\\bswr\\b'', ''\\byarn\\s+add\\s+[^\\n]*\\bswr\\b'']'
  promptSignals: '{''phrases'': [''swr'', ''useswr'', ''stale-while-revalidate''], ''allOf'': [[''data fetching'', ''client''], [''cache'', ''revalidat'']], ''anyOf'': [''mutation'', ''optimistic'', ''infinite loading'', ''pagination''], ''noneOf'': [], ''minScore'': 6}'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# SWR — React Hooks for Data Fetching

You are an expert in SWR v2 (latest: 2.4.1), the React Hooks library for data fetching by Vercel. SWR implements the stale-while-revalidate HTTP cache invalidation strategy — serve from cache first, then revalidate in the background.

## Installation

```bash
npm install swr
```

## Core API

### `useSWR`

```tsx
import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then(res => res.json())

function Profile() {
  const { data, error, isLoading, mutate } = useSWR('/api/user', fetcher)

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error loading data</div>
  return <div>Hello, {data.name}</div>
}
```

**Key parameters:**
- `key` — unique string, array, or function identifying the resource (often a URL)
- `fetcher` — async function that receives the key and returns data
- `options` — optional config object

**Return values:** `data`, `error`, `isLoading`, `isValidating`, `mutate`

### `useSWRMutation` — Remote Mutations

```tsx
import useSWRMutation from 'swr/mutation'

async function updateUser(url: string, { arg }: { arg: { name: string } }) {
  return fetch(url, { method: 'POST', body: JSON.stringify(arg) }).then(res => res.json())
}

function Profile() {
  const { trigger, isMutating } = useSWRMutation('/api/user', updateUser)

  return (
    <button disabled={isMutating} onClick={() => trigger({ name: 'New Name' })}>
      Update
    </button>
  )
}
```

### `useSWRInfinite` — Pagination & Infinite Loading

```tsx
import useSWRInfinite from 'swr/infinite'

const getKey = (pageIndex: number, previousPageData: any[]) => {
  if (previousPageData && !previousPageData.length) return null
  return `/api/items?page=${pageIndex}`
}

function Items() {
  const { data, size, setSize, isLoading } = useSWRInfinite(getKey, fetcher)
  const items = data ? data.flat() : []

  return (
    <>
      {items.map(item => <div key={item.id}>{item.name}</div>)}
      <button onClick={() => setSize(size + 1)}>Load More</button>
    </>
  )
}
```

## Global Configuration

Wrap your app (or a subtree) with `SWRConfig` to set defaults:

```tsx
import { SWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig value={{
      fetcher: (url: string) => fetch(url).then(res => res.json()),
      revalidateOnFocus: false,
      dedupingInterval: 5000,
    }}>
      <Dashboard />
    </SWRConfig>
  )
}
```

## Revalidation Strategies

| Strategy | Option | Default |
|---|---|---|
| On window focus | `revalidateOnFocus` | `true` |
| On network recovery | `revalidateOnReconnect` | `true` |
| On mount if stale | `revalidateIfStale` | `true` |
| Polling | `refreshInterval` | `0` (disabled) |
| Manual | Call `mutate()` | — |

## Optimistic Updates

```tsx
const { trigger } = useSWRMutation('/api/user', updateUser, {
  optimisticData: (current) => ({ ...current, name: 'New Name' }),
  rollbackOnError: true,
  populateCache: true,
  revalidate: false,
})
```

## Conditional Fetching

Pass `null` or a falsy key to skip fetching:

```tsx
const { data } = useSWR(userId ? `/api/user/${userId}` : null, fetcher)
```

## Error Retry

SWR retries on error by default with exponential backoff. Customize with:

```tsx
useSWR(key, fetcher, {
  onErrorRetry: (error, key, config, revalidate, { retryCount }) => {
    if (error.status === 404) return // Don't retry on 404
    if (retryCount >= 3) return      // Max 3 retries
    setTimeout(() => revalidate({ retryCount }), 5000)
  },
})
```

## `useSWRSubscription` — Real-Time Data Sources

Subscribe to real-time data (WebSockets, SSE, etc.) with automatic deduplication:

```tsx
import useSWRSubscription from 'swr/subscription'

function LivePrice({ symbol }: { symbol: string }) {
  const { data } = useSWRSubscription(
    `wss://stream.example.com/${symbol}`,
    (key, { next }) => {
      const ws = new WebSocket(key)
      ws.onmessage = (event) => next(null, JSON.parse(event.data))
      ws.onerror = (event) => next(event)
      return () => ws.close()
    }
  )

  return <span>{data?.price}</span>
}
```

The `subscribe` function receives a `next(error, data)` callback and must return a cleanup function. Multiple components using the same key share a single subscription.

## Key Rules

- **Keys must be unique** — two `useSWR` calls with the same key share cache and deduplicate requests
- **Fetcher is optional** when set via `SWRConfig`
- **`mutate(key)`** globally revalidates any hook matching that key
- **Array keys** like `useSWR(['/api/user', id], fetcher)` — the fetcher receives the full array
- **Never call hooks conditionally** — use conditional keys (`null`) instead
