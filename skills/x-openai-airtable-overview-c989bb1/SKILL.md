---
name: x-openai-airtable-overview-c989bb1
description: Explains what Airtable is and how data is structured — bases, tables, fields, records, views, automations, and interfaces. Use when you need context about the Airtable data model.
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

# Airtable Overview

Airtable is a no-code platform where teams build custom applications and AI-powered workflows from structured data. Users organize their data into bases, define tables with typed fields, set up automations to act on changes, and create interfaces that give different audiences tailored views of the same data.

## Data model

### Bases

A base is an Airtable database. It is the top-level container for all related data. A base contains one or more tables.

### Tables

A table is a collection of structured data within a base, similar to a sheet in a spreadsheet or a table in a relational database. Each table has a defined set of fields and contains records.

### Fields

A field defines a named, typed property on every record in a table.

### Records

A record is a single entry in a table. Each record has a unique ID and stores a cell value for each field defined on that table.

### Views

A view is a saved configuration for how to display records in a table. Views can filter, sort, group, and hide fields without changing the underlying data. Multiple views can exist on the same table, each showing the data differently.

## Automations

An automation is a workflow that runs in response to a defined trigger (e.g. a record entering a view) and executes one or more actions (e.g. sending an email or updating a record).

## Interfaces

Interfaces are custom app-like pages built on top of base data. They provide tailored, user-friendly ways to view and interact with records without exposing the full base structure or all of its data. A base can have multiple interfaces, each designed for a specific workflow or audience.

Some users can only access a base through its interfaces and cannot read or modify the underlying tables directly.
