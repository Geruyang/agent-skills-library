---
name: x-openai-airtable-filters-5bed075
description: Use this skill when the user wants to find, filter, or narrow down Airtable records by field values, even when they don't explicitly say "filter."
license: MIT
metadata:
  version: 1.0.0
  author: airtable
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Airtable MCP Filters

This document describes the Airtable connector's structured `filters` schema. Discover authenticated Airtable tools and inspect their actual schemas before querying. Use this format only for tools exposing it; MCP alone does not imply these parameters. If only REST API access is available, explicitly translate supported predicates to Airtable's documented `filterByFormula` format and verify semantics against the table metadata. Do not send this connector JSON unchanged to REST. Missing query access or required field metadata blocks the affected filter.

When querying records from an interface page, these filters are combined with the page's built-in filters using AND.

## Schema shape

When no top-level `operator` is specified, conditions are combined with AND. The first element in a condition's `operands` array is always a **field ID** — look up the table's schema to find field IDs before filtering.

## Field type categories

-   **Text-like**: singleLineText, multilineText, email, url, phoneNumber, richText, barcode
-   **Numeric**: number, percent, currency, rating, duration, autoNumber, count
-   **Date**: date, dateTime, createdTime, lastModifiedTime
-   **Single select**: singleSelect
-   **Multiple selects**: multipleSelects
-   **Single collaborator**: singleCollaborator
-   **Multiple collaborators**: multipleCollaborators
-   **Linked records**: multipleRecordLinks
-   **Attachment**: multipleAttachments
-   **Checkbox**: checkbox

Computed fields (formula, rollup, lookup) support whichever operators match their result type.

## Comparison operators

| Operator                | Second operand                     | Field categories                                                                                                                   |
| ----------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `=`                     | string, number, boolean, choice ID | text-like, numeric, date, checkbox, single select, multiple selects, single collaborator, multiple collaborators, linked records   |
| `!=`                    | string, number, choice ID          | text-like, numeric, date, single select, single collaborator                                                                       |
| `<`, `>`, `<=`, `>=`    | number or date value object        | numeric, date                                                                                                                      |
| `contains`              | string                             | text-like, linked records                                                                                                          |
| `doesNotContain`        | string                             | text-like, linked records                                                                                                          |
| `doesNotContain`        | array of IDs                       | multiple selects, multiple collaborators                                                                                           |
| `isEmpty`, `isNotEmpty` | _(none)_                           | text-like, numeric, date, single select, multiple selects, single collaborator, multiple collaborators, linked records, attachment |
| `hasAnyOf`, `hasAllOf`  | array of IDs                       | multiple selects, multiple collaborators, linked records                                                                           |
| `isAnyOf`               | array of IDs                       | single select, single collaborator                                                                                                 |
| `isNoneOf`              | array of IDs                       | single select, single collaborator, linked records                                                                                 |
| `isWithin`              | date range object                  | date                                                                                                                               |
| `filename`, `fileType`  | string or `"image"`/`"text"`       | attachment                                                                                                                         |

When matching a field against multiple values, prefer dedicated operators (`isAnyOf`, `isNoneOf`, `hasAnyOf`, `hasAllOf`) over combining multiple `=` conditions with `or`/`and`, when those operators are available for the field type.

## Field-type rules

### Select fields

For select fields, operand values must be **choice IDs** (e.g., `"selABCDEFGHIJKLM"`), not display names. Look up the table's schema to find choice IDs before filtering.

### Collaborator fields

When filtering by a collaborator group ID, use `operatorOptions` to match individual members of the group instead of the literal group ID. See the tool's `operatorOptions` parameter for details.

Example operand: `{"operator": "hasAnyOf", "operands": ["fldCRi9oz2vRLcIWr", "ugpDUVUnftA7H9bG8"], "operatorOptions": {"matchGroupsByMembership": true}}`

### Attachment fields

Use `fileType` to filter attachments by type (e.g., `"image"`, `"text"`) rather than `isNotEmpty` when the user specifies a file type.

### Date fields

Date comparisons (`=`, `!=`, `<`, `>`, `<=`, `>=`) use a date value object instead of a raw date string, and `isWithin` uses a date range object. The tool schema defines the available modes for each. Always include `timeZone`.

## Composing conditions

A filter's top-level operands array can contain two or more conditions, which are combined with the top-level operator (AND by default). For simple multi-condition filters, this flat structure is sufficient.

When the logic requires mixing AND and OR, nest a filter object as one of the operands. Each nested filter has its own operator and operands.

**OR inside AND** — useful when one condition is fixed and another allows multiple alternatives:

> "Scripted videos that are either in Writing or Pre-Production"
> → Bucket = Scripted AND (Status = Writing OR Status = Pre-Production)

**AND inside OR** — useful when you want records matching either a simple condition or a combination:

> "Approved videos, or videos assigned to Bailey that are in Cut 2"
> → Status = Approved OR (Editor = Bailey AND Status = Cut 2 Ready)

When combining many conditions on different fields, prefer a flat AND rather than unnecessary nesting. Only nest when the logic genuinely requires mixed AND/OR at different levels.

Prefer composing all conditions into a single `filters` object rather than splitting them across multiple calls. A single call with a composed filter is more efficient and returns the correct result set directly.

## Examples

Filter where a text field equals "orange" OR a number field is greater than 5:

```json
{
    "operator": "or",
    "operands": [
        {"operator": "=", "operands": ["fld8WsrpLHHevsnW8", "orange"]},
        {"operator": ">", "operands": ["fldulcCPDVz87Bmnw", 5]}
    ]
}
```

Filter for records where a date field is within the past week:

```json
{
    "operands": [
        {
            "operator": "isWithin",
            "operands": ["fldABC12345678x", {"mode": "pastWeek", "timeZone": "America/New_York"}]
        }
    ]
}
```
