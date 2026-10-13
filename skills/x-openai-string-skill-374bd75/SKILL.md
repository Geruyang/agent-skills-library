---
name: x-openai-string-skill-374bd75
description: Submit compact STRING API requests for network, interaction partner, and enrichment endpoints. Use when a user wants concise STRING summaries
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Operating rules
- Resolve `scripts/rest_request.py` relative to this skill directory and verify Python 3 with `requests` and authorized network access. Prefer that client; an available MCP/HTTP/CLI client may substitute only with the same endpoint, request fields, limits, and error checks. If neither path exists, report execution as blocked.
- Use `base_url=https://string-db.org/api/json`.
- Use `method=POST` with `form_body` for STRING endpoints.
- Include `caller_identity` in `form_body`; use an accurate application identifier and keep it stable within a session. The examples use a generic identifier, not a claim about the host.
- The script accepts `max_items`; for `network` and `interaction_partners`, start with API `limit=10` and `max_items=10`.
- For `enrichment`, summarize the top `5` to `10` rows unless the user asks for more.
- Re-run requests in long conversations instead of relying on prior tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return the script JSON verbatim only if the user explicitly asks for machine-readable output.
- Prefer these paths: `network`, `interaction_partners`, and `enrichment`.
- For long identifier lists, keep the request small and paged; if full results are needed, use `save_raw=true`.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common STRING patterns:
  - `{"base_url":"https://string-db.org/api/json","path":"network","method":"POST","form_body":{"identifiers":"TP53","species":9606,"caller_identity":"agent-skill-client","limit":10},"max_items":10}`
  - `{"base_url":"https://string-db.org/api/json","path":"interaction_partners","method":"POST","form_body":{"identifier":"TP53","species":9606,"caller_identity":"agent-skill-client","limit":10},"max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
Run from this skill directory with the discovered Python executable, or use the absolute script path from the project directory. Adapt quoting to the actual shell; this is a Bash example. For `save_raw=true`, supply an absolute `raw_output_path` in the authorized project output directory. Without one, the client uses the current working directory.

```bash
echo '{"base_url":"https://string-db.org/api/json","path":"network","method":"POST","form_body":{"identifiers":"TP53","species":9606,"caller_identity":"agent-skill-client","limit":10},"max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
