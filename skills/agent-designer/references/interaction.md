# 交互、事件与 UI

依据 AG-UI 协议源码/规范、ChatKit customer-support 示例、Cherry IPC/stream manager、Roo CLI loop、OpenHands Canvas 架构以及本次 TRAE 网关实验。

## 事件是投影，不是业务真相

后台拥有 run、tool attempt、审批与产物状态；UI 展示其投影。文本 token 流、工具调用进度、业务状态变化和交互请求分别建模。事件至少能关联 thread/run/message/tool call，并有顺序与终止语义。完整输出之后仍可能 cleanup 失败，不能看到最后一个 token 就展示成功。

AG-UI 可承载消息、工具、状态及 run 生命周期事件，选择对应版本 SDK 和 conformance fixtures。不要硬编码 README 中的历史事件总数；snapshot 应替换状态，delta 按协议更新，对重复/乱序/无法应用的 patch 有恢复策略。协议适配不赋予服务器动作权限。

TUI 的渲染、桌面 IPC、Web SSE/WebSocket 可消费同一应用事件模型，但连接寿命不同。关闭窗口不应默认取消后台任务；需要产品明确 `detach` 与 `cancel`。Cherry 的 open/attach/detach/abort 是可参考的区分，Roo 的 ask/say 分类是其特定消息格式，不能强加给其他系统。

## 三类用户交互

| 类型 | UI 呈现 | 后端处理 |
|---|---|---|
| 信息补充 | 表单或短问题，可恢复 | 保存缺失字段与暂停点，不把无回答当同意 |
| 动作批准 | 具体目标、参数、后果、有效期 | 校验当前身份、审批 ID、参数摘要与 run 状态；拒绝与过期可结束或返回模型 |
| 业务操作 | 卡片按钮、选择器、编辑器 | schema 校验、服务端业务约束、幂等键与 receipt |

ChatKit 示例中 widget action 与服务端 handler 驱动业务状态；复制展示代码前补真实身份、存储、权限和幂等。客户端上报的上下文（当前页面、选中记录）是待验证输入。

## 媒体与 MCP Apps 能力矩阵

逐个客户端记录 text / structured JSON / image / audio / resource link / embedded UI / action callback 的实际支持。MCP Apps 不只是返回 HTML：还涉及宿主桥接、资源获取、sandbox/CSP、消息通信与权限。

退化路径按目标选择：原生交互 → 外部受控页面 → 静态预览 → 文件/链接。注明失去哪些交互。图表 PNG 显示成功只能证明静态渲染链，不能证明交互 callback 可执行。

本次导出网关保留原始 MCP Apps resource，同时用原 renderer 生成 PNG 与本地预览。回归报告确认这一链路，明确未验证原生嵌入。预览 URL 的可达性与生命周期依赖网关和缓存；持久产物应有独立文件/对象存储、媒体类型和 digest。

## UI 验收要看到什么

发起、进度、暂停、取消、失败、重连、成功和产物下载都各有状态；审批不因刷新丢失，也不因重复点击重复执行。分别测试工具的协议结果与用户可见内容，截图/录屏或 DOM 证据标记客户端版本。只运行后端测试时交付“前端未验证”。
