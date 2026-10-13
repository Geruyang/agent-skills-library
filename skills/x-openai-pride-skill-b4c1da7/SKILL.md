---
name: x-openai-pride-skill-b4c1da7
description: Submit compact PRIDE Archive API requests for proteomics project discovery and project-level metadata. Use when a user wants concise PRIDE summaries
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Operating rules
- Resolve `scripts/rest_request.py` relative to this skill directory and verify Python 3 with `requests` and authorized network access. Prefer that client; an available MCP/HTTP/CLI client may substitute only with the same endpoint, request fields, limits, and error checks. If neither path exists, report execution as blocked.
- Use `base_url=https://www.ebi.ac.uk/pride/ws/archive/v2`.
- Start with `projects` for discovery and keep page sizes modest.
- Prefer project-level metadata lookups over broad archive dumps.
- Re-run requests in long conversations instead of relying on older tool output.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return raw JSON only if the user explicitly asks for machine-readable output.
- Prefer these paths: `projects` and `projects/<PXD accession>`.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common PRIDE patterns:
  - `{"base_url":"https://www.ebi.ac.uk/pride/ws/archive/v2","path":"projects","params":{"keyword":"proteomics","pageSize":10},"max_items":10}`
  - `{"base_url":"https://www.ebi.ac.uk/pride/ws/archive/v2","path":"projects/PXD001357"}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
Run from this skill directory with the discovered Python executable, or use the absolute script path from the project directory. Adapt quoting to the actual shell; this is a Bash example. For `save_raw=true`, supply an absolute `raw_output_path` in the authorized project output directory. Without one, the client uses the current working directory.

```bash
echo '{"base_url":"https://www.ebi.ac.uk/pride/ws/archive/v2","path":"projects","params":{"keyword":"proteomics","pageSize":10},"max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
