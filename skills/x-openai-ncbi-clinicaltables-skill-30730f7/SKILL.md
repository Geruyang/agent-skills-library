---
name: x-openai-ncbi-clinicaltables-skill-30730f7
description: Submit compact Clinical Tables NCBI Gene requests for human gene lookup, pagination, and field selection. Use when a user wants concise autocomplete-style human gene search results
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Operating rules
- Use `scripts/ncbi_gene_clinicaltables.py` for all Clinical Tables gene searches.
- The script accepts `max_items`; for search pages, start with `count=10` and `max_items=10`.
- Use `params` for endpoint options like `df`, `ef`, `sf`, `q`, `offset`, and `count`.
- Prefer `ncbi-entrez-skill` when the user wants general Entrez Gene records rather than autocomplete/search rows.
- Page with `offset` instead of asking for large pulls.
- Re-run requests in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.
- If the user asks for the full payload, set `save_raw=true` and report the saved file path instead of pasting large response arrays into chat.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return the JSON verbatim only if the user explicitly asks for machine-readable output.
- Use `terms` for the primary search text.
- Keep `count` modest and page with `offset` instead of pulling large result sets at once.

## Input
- Read one JSON object from stdin.
- Required field: `terms`
- Optional fields: `params`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common NCBI Gene patterns:
  - `{"terms":"TP53","params":{"df":"GeneID,Symbol,description"}}`
  - `{"terms":"BRCA","params":{"count":10,"df":"chromosome,GeneID,Symbol,description,type_of_gene"},"max_items":10}`
  - `{"terms":"kinase","params":{"count":10,"offset":10,"df":"GeneID,Symbol,description"},"max_items":10}`

## Output
- Success returns `ok`, `source`, `terms`, `total`, `codes`, `display_rows`, `extra_fields`, and truncation metadata.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"terms":"TP53","params":{"count":10,"df":"GeneID,Symbol,description"},"max_items":10}' | python scripts/ncbi_gene_clinicaltables.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/ncbi_gene_clinicaltables.py`.
