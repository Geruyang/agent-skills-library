---
name: x-openai-ncbi-blast-skill-d137137
description: Submit, poll, and summarize NCBI BLAST Common URL API jobs (Blast.cgi) for nucleotide or protein sequences. Use when a user wants RID status, BLAST results, or compact top-hit summaries; fetch raw Text/JSON2 only on request.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Operating rules

- Use `scripts/ncbi_blast.py` for all concrete BLAST work.
- Honor NCBI limits: `>=10s` between requests and `>=60s` between polls for the same RID.
- Always surface the `RID` in the response so the job can be resumed or refetched later.
- If the conversation is long or multiple tool calls have occurred, refetch from the `RID` instead of trusting older context.
- If a prior turn saved raw output to disk, do not read it back into context unless the user asks for a specific follow-up.

## Execution behavior

- Return compact BLAST summaries first.
- Do not paste full `JSON2` or long Text alignments into chat by default.
- Default to `max_hits=5` and `max_queries=5`.
- If the user asks for raw output, write it to a file and report the path.
- Only provide Python code when the user explicitly asks for code or execution is unavailable.
- For normal user-facing answers, summarize the script JSON in markdown; if the user explicitly asks for machine-readable output, return the JSON verbatim.

## Input

- The script reads one JSON object from stdin.
- `action` must be one of `submit`, `status`, `fetch`, or `run`.
- `submit` and `run` require `program`, `database`, `query_fasta`, and `email` (or `NCBI_EMAIL`).
- `status` and `fetch` require `rid`.
- `program` must be one of `blastn`, `blastp`, `blastx`, `tblastn`, or `tblastx`.
- `result_format` defaults to `json2` for `run` and `fetch`.
- `tool` defaults to `NCBI_TOOL`, then `ncbi-blast-skill`.
- `max_hits` defaults to `5`; `max_queries` defaults to `5`.
- `hitlist_size` defaults to `50`; `descriptions` and `alignments` default to `5`.
- `wait_timeout_sec` defaults to `900`.
- `save_raw` defaults to `false`.
- If `save_raw=true` and `raw_output_path` is omitted, the script writes `ncbi-blast-<rid>.<json|txt>` under the operating system temporary directory (`tempfile.gettempdir()`). Provide `raw_output_path` for a durable project artifact.
- `query_fasta` may contain multi-FASTA input; compact summaries still cap per-query output with `max_hits` and `max_queries`.

## Output

- Common success fields: `ok`, `source`, `action`, `warnings`.
- `submit` returns `rid`, `rtoe_seconds`, and `status="SUBMITTED"`.
- `status` returns `rid`, normalized `status`, and `has_hits`.
- `run` and `fetch` with `result_format=json2` return `rid`, `status`, `has_hits`, `result_format`, `query_count_returned`, `query_count_available`, `query_summaries_truncated`, `query_summaries`, and `raw_output_path`.
- Each `query_summary` contains `query_title`, `hit_count_returned`, `hit_count_available`, `truncated`, and `top_hits`.
- Each `top_hit` contains `rank`, `accession`, `title`, `evalue`, and `bit_score`.
- `fetch` with `result_format=text` returns `text_head` capped at 800 characters unless `save_raw=true`; when `save_raw=true`, it returns only the artifact path.
- Failures return `ok=false`, `error.code`, `error.message`, and `warnings`.

## Execution

- Run `python scripts/ncbi_blast.py`.
- If `requests` is missing, install it once before first use with `python -m pip install requests`.

```bash
echo '{"action":"run","program":"blastp","database":"swissprot","query_fasta":">q1\nMTEYK...","email":"you@example.com"}' | python scripts/ncbi_blast.py
```

## References

- Load `references/blast-common-url-api.txt` only for parameter details or uncommon BLAST options.
- Do not load `references/intent-notes.txt` during normal skill execution; it is not runtime guidance.
