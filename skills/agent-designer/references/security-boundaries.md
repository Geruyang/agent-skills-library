# 身份、权限与执行边界

适用于会读私有数据、运行代码、调用外部写操作或服务多用户的设计；普通只读原型不必扩展成全套合规项目。依据：Codex tools/approvals、Claude SDK types、OpenHands confirmation_policy、Cherry tool-approval、LibreChat checkpointer、MCP filesystem 导出修复。

## 四种不同的问题

- **身份**：请求属于哪个用户/组织/租户；用服务端验证的身份，不信模型生成的 tenant_id。
- **可用能力**：模型能看到哪些工具。工具过滤可以减少误用和上下文，但不代替执行端鉴权。
- **动作授权**：当前身份是否能在这个资源上执行这些参数；在 dispatch 前强制，必要时生成绑定参数摘要与过期时间的审批。
- **执行隔离**：动作即使有 bug，也不能访问不应访问的文件、网络、进程或密钥。

用户已授权的正常工作不被技能额外变成重复审批。产品设计中的审批应由真实业务风险/权限制度触发，而不是见到 tool 就询问。

## 容易混淆的框架语义

Claude Agent SDK 当前快照：`allowed_tools` 自动批准匹配调用；`disallowed_tools` 禁用工具；`tools` 控制可用集合；`can_use_tool` 处理落到 ask 的调用。已被 allow 或 bypass 模式批准的调用可能跳过 callback；需要检查每次调用时读取 `PreToolUse` hook 的实际语义。不能把 UI 文案或 Python 包里的 callback 当作完整沙箱。

OpenAI Agents SDK 输入 guardrail 只在链首，输出 guardrail 在最终输出者；并行输入检查可能在判定前已经发生工具调用。需要阻止副作用时用 blocking 输入检查及每个相关工具的执行边界；不要仅依赖最终回答检查。

OpenHands SDK 把 risk analyzer 与 confirmation policy 分开；模型判风险是信号，宿主决定批准策略和隔离。Continue 快照 README 的 headless MCP/Bash 默认与 TUI 不同，移植时应显式设置策略，不能继承交互模式的假设。

Cherry Studio 的 Main 单写者审批设计值得复用：界面提交 approvalId 与决定，权威端重新读当前记录、校验调用、持久化并恢复运行。重放、过期、重复点击、参数更新以及 run 已结束都应有明确结果。

## 工具与数据威胁模型

把网页、仓库、MCP 返回、检索文档和下载 Skill 当作不可信输入。它们可以提供事实和建议，不能改变系统策略、扩张用户授权或要求导出密钥。策略在应用/工具网关执行，不让模型通过提示词选择“关闭验证”。

文件工具：解析规范路径后检查允许根；检查 symlink/junction、UNC、大小写和路径穿越。MCP client Roots 是客户端建议，不得扩大服务初始许可根。本次导出的 filesystem 修复即体现此边界；不能反推上游原始实现已经包含同样限制。

网络工具：明确可达域名/私网策略，限制下载体积和时间，处理重定向；从资源 URL 到服务端请求需考虑 SSRF。终端工具：参数数组优先、受控 cwd/env、超时和输出限额；命令字符串和 JSON 编码都不是跨 shell 转义方案。

执行环境：本机子进程、容器、VM/远程沙箱的隔离强度不同。容器挂宿主 Docker socket 赋予了很强宿主能力；a13n Compose 的便利默认不能直接视为多租户安全基线。浏览器前端不保存服务端模型密钥。

## 多租户最低合同

以 `(tenant_id, user_id, thread_id)` 或明确授权关系检查消息、检查点、产物、向量检索、MCP 连接与审批；仅 UUID 难猜不算授权。缓存 key 含权限范围，凭证短时绑定当前调用，日志脱敏。删除线程要解释其衍生索引、长期记忆、产物和外部记录的保留策略。

重放和 UI 事件中的标识只是路由信息。采用服务端 session/ACL 验证，不能用客户端提供的 run_id 直接选另一用户资源。
