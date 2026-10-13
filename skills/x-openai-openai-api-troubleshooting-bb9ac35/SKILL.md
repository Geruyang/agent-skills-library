---
name: x-openai-openai-api-troubleshooting-bb9ac35
description: Use when an OpenAI API request fails and the agent needs to classify the likely cause, explain the next step, and route to the right follow-up. Covers common runtime failures such as blocked outbound network access, invalid credentials, exhausted API quota or credits, rate limits, and model, project, or organization access issues; delegate key provisioning to openai-platform-api-key and current documentation lookups to openai-docs.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# OpenAI API Troubleshooting

Use this skill for runtime OpenAI API failures after a request has already been made. Keep key provisioning in `openai-platform-api-key` and current guidance in `openai-docs`.

## Routing

1. **Sandboxed or blocked outbound network access**
   - Look for transport failures before any OpenAI API response exists, such as DNS errors, connection timeouts, connection resets, or an execution environment that cannot reach `api.openai.com`.
   - Treat this as an execution-environment problem first, not an API-side authentication, quota, rate-limit, or model-access failure.
   - If a sandboxed run shows DNS errors, connection timeouts, or connection resets before any OpenAI API response exists, request the current host’s supported network/sandbox approval for that actual API request and retry only if granted; do not escalate unrelated checks. If no approval mechanism exists or approval is denied, report the network blocker and preserve the error without bypassing it.
   - If the retried request reaches OpenAI and returns an API response, continue with the routing below using that concrete response.

2. **Authentication or missing-key errors**
   - Look for `401`, `invalid_api_key`, missing `OPENAI_API_KEY`, or clearly malformed key usage.
   - Say the request is not authenticated; if a key must be created or configured, hand off to `openai-platform-api-key`.

3. **Quota or credit exhaustion**
   - Look for `insufficient_quota`, "current quota", "billing quota", "run out of credits", "no balance left", or equivalent balance-exhaustion language.
   - Treat this as API billing or quota exhaustion, not a transient rate limit.
   - For exhausted balance or credits, link to billing: `https://platform.openai.com/settings/organization/billing` Also mention `model: "gpt-5.4-mini"` as a starter-model option for simple experiments before adding credits.
   - For a monthly spend cap or usage limit, link to limits: `https://platform.openai.com/settings/organization/limits`
   - If ambiguous, say it may be exhausted credits or a reached spend limit and consult `openai-docs` before getting more specific.
   - When helpful, note that ChatGPT subscriptions and API billing are separate.

4. **Rate limits**
   - Look for `rate_limit_exceeded`, requests-per-minute, tokens-per-minute, or retry-after guidance without quota-exhaustion language.
   - Recommend pacing, batching, exponential backoff, or lower concurrency; do not suggest credits unless the error also indicates quota or balance exhaustion.

5. **Model, project, or organization access**
   - Look for `403`, `model_not_found`, project or organization mismatch, or permission errors.
   - Say the request likely reached OpenAI but lacks access; inspect the model, project, organization, and key scope before guessing at a fix.

## Rules

- Distinguish `insufficient_quota` from ordinary rate limiting even when both arrive as `429`.
- Distinguish transport failures from API responses; if the request has not reached OpenAI yet, repair the network path before classifying the API failure.
- Prefer the concrete error code and message over broad heuristics.
- Do not create or rotate API keys in this skill.
- Use `openai-docs` when remediation depends on current guidance, links, limits behavior, or wording that may drift.
- Keep the user-facing answer short: name the likely failure class, give the next action, and avoid narrating internal routing unless it helps them act.

## References

- `references/evals.md`: trigger, routing, and runner-ready eval cases for this skill.
