# 选型与场景

这里给出基于本地固定快照的设计判断，不是市场产品排名。完整提交、源码入口、限制和许可证在 [source-index.json](source-index.json)。相同名称的 `anomalyco/opencode` 与 `opencode-ai/opencode` 是不同项目。

## 先选边界，再选项目

| 需求信号 | 优先考虑 | 付出的责任 / 何时不选 |
|---|---|---|
| 一次结构化分类/抽取，步骤确定 | 普通函数 + 模型 API | 不需要完整 agent 循环；工具与恢复由应用掌管 |
| 产品内需要工具调用、handoff、追踪 | OpenAI Agents Python/JS | Python/JS 按项目语言选择；模型、工具、状态及 tracing 能力逐项核对，不能假设两端完全对称 |
| 嵌入已有编码 agent 的原生行为 | Claude Agent SDK；Pi SDK；Cline SDK | CLI 子进程、权限默认值、会话格式、发行版本耦合不同；SDK 的开放许可证不自动覆盖其调用的闭源产品 |
| 想拥有小而可修改的循环 | Pi；Trae Agent 的研究实现 | 应用自行补租户、持久调度、隔离、运维；Trae Agent 不是 TRAE IDE 完整源码 |
| 有远程工作区、沙箱、编码任务恢复 | OpenHands Software Agent SDK / Agent Server | 需部署和管理工作区；Agent Canvas 是前端，调度服务是另一边界 |
| 需要可嵌入的能力组合，也需要自托管服务 | Agent Foundation Harness / Service | Harness 保留宿主恢复责任；Service 引入数据库、队列、执行环境。UI 不是 Service SDK |
| 自研 CLI/IDE 编码体验 | Codex、Gemini CLI、anomalyco OpenCode、Cline、Roo Code、Goose | 多为完整产品，适合作为架构参考或明确选择的基座；摘取内部模块会承担依赖、状态格式和发布耦合 |
| 对话产品、多模型、知识库与组织界面 | LibreChat、Open WebUI、LobeHub；桌面参考 Cherry Studio | 产品丰富度也意味着数据迁移、权限与 UI 状态复杂度；特殊许可证先按具体组件核对 |
| 只需要聊天与业务 UI 的结合 | ChatKit advanced samples；AG-UI | 前者是应用示例，后者是事件协议；均不能代替业务执行器、持久化或鉴权 |

`Aider` 的 repo map、编辑与 Git 工作流适合学习代码上下文选择；不因此把其 CLI 当作通用多租户服务。`lencx/ChatGPT` 是桌面封装参考，当前 v2-dev 快照无根许可证文件，不作为可直接复制的通用 agent 引擎。

维护状态取自下载快照 README：`opencode-ai/opencode` 已归档并指向 Crush，`continuedev/continue` 只读且停止维护，`OpenHands/OpenHands-CLI` 不再积极维护。可学习其设计；新生产基座默认不采用，除非用户愿意维护 fork。未来重新核验，不能把快照状态当永久事实。

## 把项目组合成六个明确的面

1. **应用面**：业务规则、用户目标、租户、交付物、幂等键；拥有最终授权决定。
2. **运行面**：turn、模型调用、工具循环、停止/取消、预算、可恢复检查点。
3. **能力面**：函数工具、MCP、技能、知识检索、环境 provider；返回结构化事实而非控制宿主策略。
4. **数据面**：事件日志、消息、业务状态、文件产物、索引、凭证引用；不同寿命不能混成一份聊天 JSON。
5. **交互面**：事件投影、流式消息、审批与表单、可见产物；前端按钮不直接获得执行权。
6. **运维面**：部署身份、队列/租约、版本迁移、审计、告警、清理与费用归属。

一般只选一个主循环，其他项目提供适配或设计参考。把两个自主循环串联时必须说明谁决定完成、谁保存历史、谁重试和谁负责预算；否则容易双重重试、重复工具调用和不可解释的终止。

## 场景决策

### 内部知识助手

先用单 agent + 只读检索 + 引用；文档访问控制在检索前/检索时强制。Open WebUI/LibreChat 可作完整产品候选，Agents SDK 或 Harness 可嵌入现有门户。只有跨会话事实确有价值才加长期记忆；每条记忆保留来源、主体、时间与删除路径。验收既看回答正确，也看无权限文档不被召回。

### 自动修复代码的 agent

先确定是嵌入现有编码引擎还是开发循环。选用 OpenHands 时用 Agent Server 管工作区；选 Pi/Trae Agent 时显式实现隔离和恢复；研究 Codex/Gemini/Cline/Roo 的审批、检查点和 diff，不复制整套客户端协议。单任务隔离分支/目录，交付 patch + 测试证据；Git 回退不能撤销已发送网络请求。

### 客服或审批业务

确定步骤用状态机，语言理解和异常处理用 agent。handoff 用于换责任主体，manager-as-tool 用于保留一个总负责人。外部写操作使用业务幂等键、人工授权记录、结果对账。ChatKit 示例可参考业务工具如何驱动界面，但示例数据和启动成功不能证明生产授权正确。

### 7×24 多租户平台

评估 Agent Foundation Service 或 OpenHands Agent Server 的责任边界，再选择已有产品 UI 或自己的 AG-UI 投影。先做断电恢复、重复投递、租户隔离和预算测试，再扩充 agent 数量。OpenHands Canvas 文档指向的 automation 服务不是本次下载语料的一部分；不能声称下载 SDK/Canvas 就已拥有该服务源码。

### 大工具目录或跨客户端能力包

Skill 存流程知识，MCP 提供执行能力，插件清单声明装配关系，前端协议负责可视交互。选择按需发现 + 完整原始 schema，先调用真实工具回路，再验证目标客户端加载和可见产物。不要通过伪造客户端私有工具名来“兼容”。

## 记录取舍

每次选型至少回答一个可反驳的问题：如果选择错了，哪项观测会让我们改方案？例如冷启动超过产品预算、断线后审批无法恢复、租户凭证必须复制到子进程、上下文目录挤占模型预算。用短验证切片消除这个不确定性，而不是先搭全平台。
