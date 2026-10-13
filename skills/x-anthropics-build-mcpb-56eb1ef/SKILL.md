---
name: x-anthropics-build-mcpb-56eb1ef
description: This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Build an MCPB (Bundled Local MCP Server)

MCPB is a local MCP server **packaged with its runtime**. The user installs one file; it runs without needing Node, Python, or any toolchain on their machine. It's the sanctioned way to distribute local MCP servers.

> MCPB is the **secondary** distribution path. Anthropic recommends remote MCP servers for directory listing — see https://claude.com/docs/connectors/building/what-to-build.

**Use MCPB when the server must run on the user's machine** — reading local files, driving a desktop app, talking to localhost services, OS-level APIs. If your server only hits cloud APIs, you almost certainly want a remote HTTP server instead (see `build-mcp-server`). Don't pay the MCPB packaging tax for something that could be a URL.

---

## What an MCPB bundle contains

```
my-server.mcpb              (zip archive)
├── manifest.json           ← identity, entry point, config schema, compatibility
├── server/                 ← your MCP server code
│   ├── index.js
│   └── node_modules/       ← bundled dependencies (or vendored)
└── icon.png
```

The host reads `manifest.json`, launches `server.mcp_config.command` as a **stdio** MCP server, and pipes messages. From your code's perspective it's identical to a local stdio server — the only difference is packaging.

---

## Manifest

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/mcpb/main/schemas/mcpb-manifest-v0.4.schema.json",
  "manifest_version": "0.4",
  "name": "local-files",
  "version": "0.1.0",
  "description": "Read, search, and watch files on the local filesystem.",
  "author": { "name": "Your Name" },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "ROOT_DIR": "${user_config.rootDir}"
      }
    }
  },
  "user_config": {
    "rootDir": {
      "type": "directory",
      "title": "Root directory",
      "description": "Directory to expose. Defaults to ~/Documents.",
      "default": "${HOME}/Documents",
      "required": true
    }
  },
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "platforms": ["darwin", "win32", "linux"]
  }
}
```

**`server.type`** — `node`, `python`, or `binary`. Informational; the actual launch comes from `mcp_config`.

**`server.mcp_config`** — the literal command/args/env to spawn. Use `${__dirname}` for bundle-relative paths and `${user_config.<key>}` to substitute install-time config. **There's no auto-prefix** — the env var names your server reads are exactly what you put in `env`.

**`user_config`** — install-time settings surfaced in the host's UI. `type: "directory"` renders a native folder picker. `sensitive: true` stores in OS keychain. See `references/manifest-schema.md` for all fields.

---

## Server code: same as local stdio

The server itself is a standard stdio MCP server. Nothing MCPB-specific in the tool logic.

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { readFile, readdir } from "node:fs/promises";
import { join } from "node:path";
import { homedir } from "node:os";

// ROOT_DIR comes from what you put in manifest's server.mcp_config.env — no auto-prefix
const ROOT = (process.env.ROOT_DIR ?? join(homedir(), "Documents"));

const server = new McpServer({ name: "local-files", version: "0.1.0" });

server.registerTool(
  "list_files",
  {
    description: "List files in a directory under the configured root.",
    inputSchema: { path: z.string().default(".") },
    annotations: { readOnlyHint: true },
  },
  async ({ path }) => {
    const entries = await readdir(join(ROOT, path), { withFileTypes: true });
    const list = entries.map(e => ({ name: e.name, dir: e.isDirectory() }));
    return { content: [{ type: "text", text: JSON.stringify(list, null, 2) }] };
  },
);

server.registerTool(
  "read_file",
  {
    description: "Read a file's contents. Path is relative to the configured root.",
    inputSchema: { path: z.string() },
    annotations: { readOnlyHint: true },
  },
  async ({ path }) => {
    const text = await readFile(join(ROOT, path), "utf8");
    return { content: [{ type: "text", text }] };
  },
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

**Sandboxing is entirely your job.** There is no manifest-level sandbox — the process runs with full user privileges. Validate paths, refuse to escape `ROOT`, allowlist spawns. See `references/local-security.md`.

Before hardcoding `ROOT` from a config env var, check if the host supports `roots/list` — the spec-native way to get user-approved directories. See `references/local-security.md` for the pattern.

---

## Build pipeline

### Node

```bash
npm install
npx esbuild src/index.ts --bundle --platform=node --outfile=server/index.js
# or: copy node_modules wholesale if native deps resist bundling
npx @anthropic-ai/mcpb pack
```

`mcpb pack` zips the directory and validates `manifest.json` against the schema.

### Python

```bash
pip install -t server/vendor -r requirements.txt
npx @anthropic-ai/mcpb pack
```

Vendor dependencies into a subdirectory and prepend it to `sys.path` in your entry script. Native extensions (numpy, etc.) must be built for each target platform — avoid native deps if you can.

---

## MCPB has no sandbox — security is on you

Unlike mobile app stores, MCPB does NOT enforce permissions. The manifest has no `permissions` block — the server runs with full user privileges. `references/local-security.md` is mandatory reading, not optional. Every path must be validated, every spawn must be allowlisted, because nothing stops you at the platform level.

If you came here expecting filesystem/network scoping from the manifest: it doesn't exist. Build it yourself in tool handlers.

If your server's only job is hitting a cloud API, stop — that's a remote server wearing an MCPB costume. The user gains nothing from running it locally, and you're taking on local-security burden for no reason.

---

## MCPB + UI widgets

MCPB servers can serve UI resources exactly like remote MCP apps — the widget mechanism is transport-agnostic. A local file picker that browses the actual disk, a dialog that controls a native app, etc.

Widget authoring is covered in the **`build-mcp-app`** skill; it works the same here. The only difference is where the server runs.

---

## Testing

```bash
# Interactive manifest creation (first time)
npx @anthropic-ai/mcpb init

# Run the server directly over stdio, poke it with the inspector
npx @modelcontextprotocol/inspector node server/index.js

# Validate manifest against schema, then pack
npx @anthropic-ai/mcpb validate
npx @anthropic-ai/mcpb pack

# Sign for distribution
npx @anthropic-ai/mcpb sign dist/local-files.mcpb

# Install: drag the .mcpb file onto Claude Desktop
```

Test on a machine **without** your dev toolchain before shipping. "Works on my machine" failures in MCPB almost always trace to a dependency that wasn't actually bundled.

---

## Reference files

- `references/manifest-schema.md` — full `manifest.json` field reference
- `references/local-security.md` — path traversal, sandboxing, least privilege
