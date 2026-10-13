---
name: x-openai-aspnet-core-84d1c85
description: Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# ASP.NET Core

## Overview

Choose the right ASP.NET Core application model, compose the host and request pipeline correctly, and implement features in the framework style Microsoft documents today.

Load the smallest set of references that fits the task. Do not load every reference by default.

## Workflow

1. Confirm the target framework, SDK, and current app model.
2. Open [references/stack-selection.md](references/stack-selection.md) first for new apps or major refactors.
3. Open [references/program-and-pipeline.md](references/program-and-pipeline.md) next for `Program.cs`, DI, configuration, middleware, routing, logging, and static assets.
4. Open exactly one primary app-model reference:
   - [references/ui-blazor.md](references/ui-blazor.md)
   - [references/ui-razor-pages.md](references/ui-razor-pages.md)
   - [references/ui-mvc.md](references/ui-mvc.md)
   - [references/apis-minimal-and-controllers.md](references/apis-minimal-and-controllers.md)
5. Add cross-cutting references only as needed:
   - [references/data-state-and-services.md](references/data-state-and-services.md)
   - [references/security-and-identity.md](references/security-and-identity.md)
   - [references/realtime-grpc-and-background-work.md](references/realtime-grpc-and-background-work.md)
   - [references/testing-performance-and-operations.md](references/testing-performance-and-operations.md)
6. Open [references/versioning-and-upgrades.md](references/versioning-and-upgrades.md) before introducing new platform APIs into an older solution or when migrating between major versions.
7. Use [references/source-map.md](references/source-map.md) when you need the Microsoft Learn section that corresponds to a task not already covered by the focused references.

## Default Operating Assumptions

- Prefer the latest stable ASP.NET Core and .NET unless the repository or user request pins an older target.
- As of March 2026, prefer .NET 10 / ASP.NET Core 10 for new production work. Treat ASP.NET Core 11 as preview unless the user explicitly asks for preview features.
- Prefer `WebApplicationBuilder` and `WebApplication`. Avoid older `Startup` and `WebHost` patterns unless the codebase already uses them or the task is migration.
- Prefer built-in DI, options/configuration, logging, ProblemDetails, OpenAPI, health checks, rate limiting, output caching, and Identity before adding third-party infrastructure.
- Keep feature slices cohesive so the page, component, endpoint, controller, validation, service, data access, and tests are easy to trace.
- Respect the existing app model. Do not rewrite Razor Pages to MVC or controllers to Minimal APIs without a clear reason.

## Reference Guide

- [references/_sections.md](references/_sections.md): Quick index and reading order.
- [references/stack-selection.md](references/stack-selection.md): Choose the right ASP.NET Core application model and template.
- [references/program-and-pipeline.md](references/program-and-pipeline.md): Structure `Program.cs`, services, middleware, routing, configuration, logging, and static assets.
- [references/ui-blazor.md](references/ui-blazor.md): Build Blazor Web Apps, choose render modes, and use components, forms, and JS interop correctly.
- [references/ui-razor-pages.md](references/ui-razor-pages.md): Build page-focused server-rendered apps with handlers, model binding, and conventions.
- [references/ui-mvc.md](references/ui-mvc.md): Build controller/view applications with clear separation of concerns.
- [references/apis-minimal-and-controllers.md](references/apis-minimal-and-controllers.md): Build HTTP APIs with Minimal APIs or controllers, including validation and response patterns.
- [references/data-state-and-services.md](references/data-state-and-services.md): Use EF Core, `DbContext`, options, `IHttpClientFactory`, session, temp data, and app state responsibly.
- [references/security-and-identity.md](references/security-and-identity.md): Apply authentication, authorization, Identity, secrets, data protection, CORS, CSRF, and HTTPS guidance.
- [references/realtime-grpc-and-background-work.md](references/realtime-grpc-and-background-work.md): Use SignalR, gRPC, and hosted services.
- [references/testing-performance-and-operations.md](references/testing-performance-and-operations.md): Add integration tests, browser tests, caching, compression, health checks, rate limits, and deployment concerns.
- [references/versioning-and-upgrades.md](references/versioning-and-upgrades.md): Handle target frameworks, breaking changes, obsolete APIs, and migrations.
- [references/source-map.md](references/source-map.md): Map the official ASP.NET Core documentation tree to the references in this skill.

## Execution Notes

- When generating new code, start from the correct `dotnet new` template and keep the generated structure recognizable.
- When editing an existing solution, follow the solution's conventions first and use these references to avoid framework misuse or outdated patterns.
- When a task mentions "latest", verify the feature on Microsoft Learn or the ASP.NET Core docs repo before relying on memory.
