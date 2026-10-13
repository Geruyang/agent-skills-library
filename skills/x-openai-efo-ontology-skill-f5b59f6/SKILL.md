---
name: x-openai-efo-ontology-skill-f5b59f6
description: Submit compact EFO OLS4 requests for search, term lookup, children, and descendants. Use when a user wants concise EFO resolution or ontology-expansion summaries
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Operating rules
- Resolve `scripts/rest_request.py` relative to this skill directory and verify Python 3 with `requests` and authorized network access. Prefer that client; an available MCP/HTTP/CLI client may substitute only with the same endpoint, request fields, limits, and error checks. If neither path exists, report execution as blocked.
- Use `base_url=https://www.ebi.ac.uk/ols4/api`.
- Search, children, and descendant endpoints are better with `max_items=10`; single term lookups usually do not need `max_items`.
- Use the smallest ontology expansion that answers the question.
- Re-run requests in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Prefer these paths: `search`, `ontologies/efo/terms/<double-encoded-iri>`, and the corresponding `children` or `descendants` paths.
- If the user needs the full payload, set `save_raw=true` and report the saved file path.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common OLS4 patterns:
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"search","params":{"q":"asthma","ontology":"efo"},"record_path":"response.docs","max_items":10}`
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0000270"}`
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0000270/descendants","record_path":"_embedded.terms","max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
Run from this skill directory with the discovered Python executable, or use the absolute script path from the project directory. Adapt quoting to the actual shell; this is a Bash example. For `save_raw=true`, supply an absolute `raw_output_path` in the authorized project output directory. Without one, the client uses the current working directory.

```bash
echo '{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"search","params":{"q":"asthma","ontology":"efo"},"record_path":"response.docs","max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
