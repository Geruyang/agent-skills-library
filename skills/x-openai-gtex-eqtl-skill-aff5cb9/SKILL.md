---
name: x-openai-gtex-eqtl-skill-aff5cb9
description: Fetch GTEx single-tissue eQTL associations from one variant input by accepting rsID, GRCh37, or GRCh38 input and resolving to the required GRCh38 query for the GTEx v2 API. Use when a user wants eQTL associations returned as JSON.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Operating rules

- Use Python `requests` for all network calls.
- Accept exactly one of `rsid`, `grch37`, `grch38`, or `variant`, and resolve to a GRCh38 `chrom-pos-ref-alt` query.
- Convert to GTEx `variantId` format: `chr{chrom}_{pos}_{ref}_{alt}_b38`.
- Always return one JSON object (no markdown) as final output.

# Input

Accept JSON on stdin as either:

- A string: `"10-112998590-C-T"` (treated as GRCh38)
- An object:

```json
{
  "grch38": "10-112998590-C-T",
  "max_results": 200
}
```

Other accepted object forms include:

```json
{
  "grch37": "10-114758349-C-T"
}
```

```json
{
  "rsid": "rs7903146",
  "max_results": 50
}
```

Allowed variant separators include `-`, `:`, `_`, `/`, or whitespace, for example:

- `10-112998590-C-T`
- `10:112998590-C-T`
- `10:112998590:C:T`
- `chr10 112998590 C T`

`max_results` is optional and truncates returned eQTL rows when provided.

# Output

Success shape:

```json
{
  "ok": true,
  "source": "gtex-v2",
  "input": {"type": "grch38", "value": "10-112998590-C-T"},
  "query_variant": {
    "chr": "10",
    "pos": 112998590,
    "ref": "C",
    "alt": "T",
    "canonical": "10:112998590-C-T",
    "variant_id": "chr10_112998590_C_T_b38"
  },
  "eqtl_count": 2,
  "eqtl_count_total": 2,
  "truncated": false,
  "eqtls": [],
  "paging_info": {},
  "warnings": []
}
```

Failure shape:

```json
{
  "ok": false,
  "error": {"code": "...", "message": "..."},
  "warnings": []
}
```

# Execution

Use:

- `scripts/gtex_eqtl.py`

The script reads JSON from stdin and prints JSON to stdout.

Example:

```bash
echo '{"grch38":"10-112998590-C-T","max_results":5}' | python scripts/gtex_eqtl.py
```
