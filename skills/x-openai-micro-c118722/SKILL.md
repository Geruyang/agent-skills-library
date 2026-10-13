---
name: x-openai-micro-c118722
description: Expert guidance for micro — asynchronous HTTP microservices framework by Vercel. Use when building lightweight HTTP servers, API endpoints, or microservices using the micro library.
metadata:
  priority: '4'
  docs: '[''https://github.com/vercel/micro'']'
  pathPatterns: '[]'
  importPatterns: '[''micro'', ''micro-dev'']'
  bashPatterns: '[''\\bnpm\\s+(install|i|add)\\s+[^\\n]*\\bmicro\\b'', ''\\bpnpm\\s+(install|i|add)\\s+[^\\n]*\\bmicro\\b'', ''\\bbun\\s+(install|i|add)\\s+[^\\n]*\\bmicro\\b'', ''\\byarn\\s+add\\s+[^\\n]*\\bmicro\\b'', ''\\bnpx\\s+micro\\b'', ''\\bnpx\\s+micro-dev\\b'']'
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# micro — Asynchronous HTTP Microservices

You are an expert in micro, Vercel's lightweight framework for building asynchronous HTTP microservices in Node.js. micro makes it easy to write single-purpose HTTP endpoints with minimal boilerplate.

## Installation

```bash
npm install micro
```

## Basic Usage

Create a module that exports a request handler:

```ts
// index.ts
import { serve } from 'micro'

const handler = (req: Request) => {
  return new Response('Hello, World!')
}

serve(handler)
```

Or use the classic API:

```ts
import { IncomingMessage, ServerResponse } from 'http'

export default (req: IncomingMessage, res: ServerResponse) => {
  res.end('Hello, World!')
}
```

Run with:

```bash
npx micro
```

## Core API

### `json(req)` — Parse JSON Body

```ts
import { json } from 'micro'

export default async (req: IncomingMessage, res: ServerResponse) => {
  const body = await json(req)
  return { received: body }
}
```

### `text(req)` — Parse Text Body

```ts
import { text } from 'micro'

export default async (req: IncomingMessage, res: ServerResponse) => {
  const body = await text(req)
  return `You said: ${body}`
}
```

### `buffer(req)` — Parse Raw Body

```ts
import { buffer } from 'micro'

export default async (req: IncomingMessage, res: ServerResponse) => {
  const raw = await buffer(req)
  return `Received ${raw.length} bytes`
}
```

### `send(res, statusCode, data)` — Send Response

```ts
import { send } from 'micro'

export default (req: IncomingMessage, res: ServerResponse) => {
  send(res, 200, { status: 'ok' })
}
```

### `createError(statusCode, message)` — HTTP Errors

```ts
import { createError } from 'micro'

export default (req: IncomingMessage, res: ServerResponse) => {
  if (!req.headers.authorization) {
    throw createError(401, 'Unauthorized')
  }
  return { authorized: true }
}
```

## Development with micro-dev

`micro-dev` provides hot-reloading for development:

```bash
npm install --save-dev micro-dev

# Run in dev mode
npx micro-dev index.js
```

## Composition

Chain multiple handlers with function composition:

```ts
import { IncomingMessage, ServerResponse } from 'http'

const cors = (fn: Function) => async (req: IncomingMessage, res: ServerResponse) => {
  res.setHeader('Access-Control-Allow-Origin', '*')
  return fn(req, res)
}

const handler = async (req: IncomingMessage, res: ServerResponse) => {
  return { hello: 'world' }
}

export default cors(handler)
```

## package.json Setup

```json
{
  "main": "index.js",
  "scripts": {
    "start": "micro",
    "dev": "micro-dev"
  },
  "dependencies": {
    "micro": "^10.0.0"
  },
  "devDependencies": {
    "micro-dev": "^3.0.0"
  }
}
```

## Key Points

1. **Return values are sent as responses** — return strings, objects (auto-serialized to JSON), or Buffers
2. **Async by default** — handlers can be async functions, errors are caught automatically
3. **Thrown errors become HTTP errors** — use `createError()` for proper status codes
4. **No routing built-in** — micro is a single-endpoint server; use a router like `micro-router` for multi-route services
5. **Body parsing is explicit** — use `json()`, `text()`, or `buffer()` to parse request bodies
6. **Composable** — wrap handlers with higher-order functions for middleware-like behavior

## Official Resources

- [micro GitHub](https://github.com/vercel/micro)
