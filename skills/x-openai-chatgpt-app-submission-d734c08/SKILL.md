---
name: x-openai-chatgpt-app-submission-d734c08
description: Inspect a ChatGPT Apps MCP server codebase and generate chatgpt-app-submission.json with app info suggestions, tool hint justifications, test cases, and negative test cases, then report review-check findings and outputSchema warnings for submission review.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# ChatGPT App Submission

Use this skill when a developer needs a `chatgpt-app-submission.json` file for a ChatGPT Apps submission. The file is uploaded in the Apps submission form to fill out parts of App Info, MCP Server, and Testing.

## Workflow

1. Inspect the MCP server codebase from the current working directory.
2. Read repo metadata, package metadata, README files, app manifests, tool descriptors, resource templates, and widget metadata needed to understand the app.
3. Find every exposed MCP tool, its declared `readOnlyHint`, `openWorldHint`, and `destructiveHint` annotations, and whether it declares `outputSchema`.
4. Read each tool implementation and any called helper functions needed to understand side effects.
5. Compare tool annotations, tool names, tool descriptions, and CSP values against actual behavior. If any value is missing, stale, misleading, or inconsistent, ask the developer for approval before updating source.
6. Generate concise review-facing app info suggestions, tool hint justifications, positive test cases, and negative test cases.
7. Write `chatgpt-app-submission.json` in the current working directory.
8. Print review-check findings and any missing `outputSchema` warnings in the final response, and explain what the developer should do with each finding before submission.

Do not infer behavior from the tool name alone. Use the real tool implementation and declared annotations. If a tool calls into another module or API client, inspect enough of that path to know whether it reads, writes, deletes, sends, publishes, or changes external state.

## App Info Rules

Suggest app info from source-of-truth project metadata and the tool behavior you inspected. Keep it plain-language and submission-review-facing.

- `display_name`: use the product or app name from repo metadata, package metadata, README, manifest, or existing configuration. Keep it short enough for the submission form.
- `subtitle`: summarize what the app does in one short functional phrase, not marketing copy. It must be 30 characters or less.
- `description`: describe concrete user value and the main workflows the tools support.
- `category`: choose one of `BUSINESS`, `COLLABORATION`, `DESIGN`, `DEVELOPER_TOOLS`, `EDUCATION`, `ENTERTAINMENT`, `FINANCE`, `FOOD`, `LIFESTYLE`, `NEWS`, `PRODUCTIVITY`, `SHOPPING`, or `TRAVEL`.

## Hint Rules

Use the Apps SDK review meanings:

- `readOnlyHint`: `true` only when the tool strictly fetches, looks up, lists, retrieves, or computes data without changing state. `false` if it can create, update, delete, send, enqueue, run jobs, write logs, start workflows, or otherwise mutate state.
- `destructiveHint`: `true` if the tool can delete, overwrite, send irreversible messages or transactions, revoke access, or perform destructive admin actions, including via some modes or parameters. Otherwise `false`.
- `openWorldHint`: `true` if the tool can change publicly visible internet state or external third-party systems, such as sending emails or messages, posting/publishing content, creating public tickets/issues, pushing code/content, or submitting external forms. `false` if it only operates in closed/private systems.

ChatGPT Apps submissions require every tool to set all three hints explicitly. Missing or null hints are submission blockers, even if MCP clients may have protocol-level defaults.

If a hint is missing, null, or does not match the actual behavior you found in code, stop before writing the JSON and ask the developer for approval to update the MCP server source. In the approval request, list each affected tool, the missing/current hint value, the behavior you observed, and the recommended explicit hint value. If the developer approves, make the smallest source change that sets the correct hint explicitly, then generate JSON using the updated values. If the developer does not approve or the correct edit location is ambiguous, do not generate misleading JSON; report the mismatch and the blocked update.

## Output Schema Warnings

While inspecting exposed MCP tools, record each tool whose descriptor or source definition omits `outputSchema` or sets it to `null`. Missing `outputSchema` is not a blocker for generating `chatgpt-app-submission.json`, and the submission JSON does not include output schemas.

Do not infer or invent output schemas for this warning. Use the actual MCP tool descriptor or source definition. In the final response, include a concise warning for any missing tools: `Add an outputSchema so models can use this tool's results more reliably. See https://modelcontextprotocol.io/specification/draft/server/tools#tool.` Include the affected tool names. If every tool declares `outputSchema`, do not include an outputSchema warning.

## Tool Descriptor and CSP Rules

Check tool names, tool descriptions, and widget CSP metadata while inspecting the app.

- Tool input schemas should not solicit sensitive data unless that data is strictly necessary for the app's stated user-facing workflow. Flag fields that ask for PHI, PCI, SSNs, credentials, MFA codes, government IDs, biometrics, or similarly sensitive identifiers.
- Tool names should match the action the tool performs and should not imply capabilities the implementation does not provide.
- Tool descriptions should accurately describe inputs, side effects, and user-visible results.
- CSP values should be as narrow as the implementation supports. Flag wildcard domains, unused domains, broad resource/connect domains, and missing domains required by actual widget behavior.

If tool names, descriptions, or CSP values appear missing or inconsistent with actual behavior, prompt the developer for approval before editing source. If the developer declines or the correct edit is ambiguous, keep the generated JSON truthful and report the finding in the final response.

## Test Case Rules

Generate exactly five positive test cases and exactly three negative test cases.

- Positive test cases must use exact MCP action names in `tools_triggered`.
- Positive prompts should cover the main tool-backed workflows and edge conditions that review should exercise.
- Negative test cases should describe prompts where the app should not trigger, including nearby-but-out-of-scope requests.
- Keep expected outputs review-facing and concise. Do not include secrets, credentials, source snippets, local paths, request IDs, stack traces, or private implementation details.

## Output Contract

Write exactly one JSON file named `chatgpt-app-submission.json`:

```json
{
  "$schema": "https://developers.openai.com/apps-sdk/schemas/chatgpt-app-submission.v1.json",
  "schema_version": 1,
  "app_info": {
    "display_name": "Example App",
    "subtitle": "Find and update records",
    "description": "Example App helps users find records, inspect details, and update workspace data through ChatGPT.",
    "category": "PRODUCTIVITY"
  },
  "tools": {
    "tool_name": {
      "annotations": {
        "readOnlyHint": true,
        "openWorldHint": false,
        "destructiveHint": false
      },
      "justifications": {
        "read_only_justification": "Only retrieves matching records and does not modify data.",
        "open_world_justification": "Does not write to public internet state or third-party systems.",
        "destructive_justification": "Does not delete, overwrite, revoke access, or perform irreversible actions."
      }
    }
  },
  "test_cases": [
    {
      "description": "Find records that match a specific user request.",
      "user_prompt": "Find my open records for this week.",
      "file_attachment_urls": null,
      "tools_triggered": "tool_name",
      "expected_output": "Returns matching records with enough detail for the user to choose the next action.",
      "expected_output_url": null
    }
  ],
  "negative_test_cases": [
    {
      "description": "Do not trigger for unrelated calendar requests.",
      "user_prompt": "What meetings do I have tomorrow?",
      "file_attachment_urls": null,
      "tools_triggered": null,
      "expected_output": "The app should not be invoked because the request is outside its supported workflows.",
      "expected_output_url": null
    }
  ]
}
```

`$schema` identifies the import file shape for editors and importers; the agent does not need to fetch it. `tools` is required. `app_info`, `test_cases`, and `negative_test_cases` are optional in the schema, but generate them whenever the repo contains enough information. Do not include review-check findings in this JSON file.

## Writing Justifications

- Keep each justification to one sentence.
- Be specific about the actual behavior, not the annotation itself.
- For write tools, state what system is changed and whether the change is bounded/private or public/external.
- For destructive tools, name the irreversible action and mention any real safeguard only if it exists in the code.
- Do not include source snippets, secrets, tokens, request IDs, local paths, stack traces, or private implementation details in the JSON.

Good examples:

- `Only retrieves project metadata and returns it without creating or updating records.`
- `Creates a private task in the user's workspace and cannot publish content to public URLs.`
- `Deletes the selected workspace document, which cannot be recovered after confirmation.`

Bad examples:

- `readOnlyHint is true because the tool is read-only.`
- `Probably safe.`
- `The function calls client.delete_item(...) in src/server.py.`

## Reporting Review Checks

Report these checks in the final response after writing `chatgpt-app-submission.json`. Do not write them into the JSON file.

- Sensitive data solicitation: flag tool input schema fields that request PHI, PCI, SSNs, credentials, MFA codes, government IDs, biometrics, or similarly sensitive identifiers. Include the tool name and input field in the finding.
- Tool data use: flag tools that collect, expose, mutate, or transmit sensitive data in a way the descriptor or tests do not clearly explain.
- Tool naming: flag names or descriptions that are too vague, misleading, overbroad, or inconsistent with implementation behavior.
- Weak CSPs: flag broad, wildcard, unused, or missing CSP domains in widget metadata.

For each finding, explain the practical next step: update source, update submission copy, narrow CSP, remove or justify a sensitive input, or manually review before submitting. If there are no findings, say that these checks did not find obvious issues from source inspection.

## Final Response

After writing the file, summarize the app info fields generated, number of tools covered, positive test case count, and negative test case count. Then include a `Review findings` section with any sensitive data solicitation, tool data use, tool naming, weak CSP findings, or missing `outputSchema` warnings and what to do with each one. If generation is blocked, lead with the exact missing hints or source ambiguity.
