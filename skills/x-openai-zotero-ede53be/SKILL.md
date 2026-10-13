---
name: x-openai-zotero-ede53be
description: Use Zotero Desktop through its local API to enable/probe the local API, search a local Zotero library, list items/collections/tags, export BibTeX, insert citation keys into LaTeX or Markdown drafts, read indexed full text when requested, and import BibTeX/RIS records into Zotero through the connector server. Use when the user mentions Zotero, citations, references.bib, BibTeX export, local Zotero API, localhost:23119, or adding citations from a Zotero library.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Zotero

Use this skill to operate a user's local Zotero Desktop library through available local process/API access.

Core helper:

```bash
python3 <skill-dir>/scripts/zotero.py <command>
```

Resolve `<skill-dir>` to the directory containing this installed `SKILL.md`, verify the helper exists, and discover a Python 3 executor with access to the user's Zotero localhost service. If unavailable, provide a local command handoff and state that the library was not accessed.

The helper is stdlib-only and follows the repo convention of running plugin Python helpers with `python3` / `#!/usr/bin/env python3`; it does not depend on a particular agent client.

## Fast starts

Check readiness in one command:

```bash
python3 <skill-dir>/scripts/zotero.py status --json
```

Enable the local API and restart Zotero if needed:

```bash
python3 <skill-dir>/scripts/zotero.py enable --restart
```

Search and export citation data:

```bash
python3 <skill-dir>/scripts/zotero.py search "transformer" --json
python3 <skill-dir>/scripts/zotero.py export-bibtex --out references.bib
```

Insert a citation from Zotero into a draft and keep `references.bib` in sync:

```bash
python3 <skill-dir>/scripts/zotero.py cite --query "Attention Is All You Need" --tex paper.tex --bib references.bib --marker '<cite>'
```

## Workflow

1. Start with `status --json`. Do not rediscover prefs, ports, or profile paths manually unless the helper fails.
2. If `local_api_enabled_pref` is false, run `enable --restart` when the user asked you to operate Zotero. This updates Zotero's local preference and restarts Zotero so port `23119` comes up.
3. Use read-only local API commands for normal work:
   - `inventory` for item/collection/tag summaries.
   - `search <query>` for papers/items.
   - `export-bibtex` or `sync-bib` for `.bib` files.
   - `cite` for inserting a citation into a draft.
4. Only retrieve attachment file URLs or full text when the user asks for PDFs, attachment paths, or full-text content.
5. Treat Zotero library writes as explicit write actions. Before `import-bibtex`, `import-ris`, or connector save commands, confirm the exact record/source and destination unless the user's prompt already explicitly asked to add/import it.

## Common commands

```bash
# Readiness and route map
python3 <skill-dir>/scripts/zotero.py status --json
python3 <skill-dir>/scripts/zotero.py probe --json

# Library inventory
python3 <skill-dir>/scripts/zotero.py inventory
python3 <skill-dir>/scripts/zotero.py collections
python3 <skill-dir>/scripts/zotero.py tags

# Search and export
python3 <skill-dir>/scripts/zotero.py search "BERT"
python3 <skill-dir>/scripts/zotero.py export-bibtex --out references.bib
python3 <skill-dir>/scripts/zotero.py export-bibtex --item-key PXW99EKT
python3 <skill-dir>/scripts/zotero.py citations --style apa --json

# Draft editing
python3 <skill-dir>/scripts/zotero.py cite --item-key PXW99EKT --tex paper.tex --bib references.bib --marker '<cite>'
python3 <skill-dir>/scripts/zotero.py cite --query "BERT" --markdown notes.md --bib references.bib --marker '<cite>'

# Attachments and full text; use only on request
python3 <skill-dir>/scripts/zotero.py children PXW99EKT --json
python3 <skill-dir>/scripts/zotero.py fulltext 2JAZS9U8 --out attention-fulltext.txt
python3 <skill-dir>/scripts/zotero.py file-url 2JAZS9U8

# Writes to Zotero; confirm first unless explicitly requested
python3 <skill-dir>/scripts/zotero.py selected-target --json
python3 <skill-dir>/scripts/zotero.py import-bibtex --file new-reference.bib --yes
python3 <skill-dir>/scripts/zotero.py import-ris --file new-reference.ris --yes
```

## Output standards

- For inventory/search, return title, creators, year, Zotero item key, and BibTeX key when available.
- Explain the two-key distinction when relevant: Zotero item keys like `PXW99EKT` are not the same as exported BibTeX keys like `vaswani_attention_2023`.
- For `.bib` export, return the absolute output path and entry count.
- For draft citation insertion, report the edited file, inserted citation key, and updated `.bib` path.
- For blockers, name the exact gate: Zotero app missing, local API disabled, port closed, connector unavailable, no matching item, or write not confirmed.

## Route details

Read `references/local-api-routes.md` only when you need endpoint details beyond the helper commands.
