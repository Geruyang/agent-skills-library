# 出处、版本和覆盖边界

本技能为本次下载语料编写的设计综合，不是上游项目官方指南。正文为原创总结；未把任何来源的许可证统一改写成一个许可证。使用、修改或再分发原代码/技能前，以具体组件的许可和 NOTICE 为准。

## 可查询索引

- [source-index.json](source-index.json)：35 个仓库，完整 commit、根许可说明/文件 hash、选定源码证据、设计用途和限制。资源路径均相对包根。GitHub 源码链接可由 `url + /blob/ + commit + / + 仓库内相对路径` 构造。
- [skill-index.json](skill-index.json)：667 个下载导出技能，来自六个仓库；原位置、导出位置、正文 hash、描述、多标签与组件许可入口。分类是检索辅助，不是行为测试结论。
- [mcp-index.json](mcp-index.json)：45 个上游配置定义（43 个去重目标），以及 16 个本地实现/已安装依赖的独立记录；两组存在重叠，不能相加作唯一服务总数。
- [mcp-followup.json](mcp-followup.json)：原先 41 项待定 MCP 的后续前提和安装状态；当前报告仍有 30 个去重目标未启用。条目数与去重统计口径可能不同，以字段解释为准。
- [runtime-dependencies.json](runtime-dependencies.json)：MCP 的锁文件、构建资料及便携 Python/Node 许可证 hash。官方运行时依赖不被冒充为新下载完整源码仓库。

上述快照采集于 2026-10-12。`build_inventory.py` 只读取此下载包的清单和目录，不访问个人 skills/MCP/凭证；新增仓库必须先补人工设计总结。生成报告位于资源包 `reports/agent-designer-coverage.json`。

## 下载的层级

34 个初始仓库 + 后增 Agent Foundation = 35 个 shallow Git 工作树。不是所有历史分支和 release 安装包。下载包的 `export/mcp/servers` 包含 reference servers 与插件实现的导出/适配副本；`upstream-catalog` 包含供应商连接定义和前提，不能据此称 SaaS 后端源码已下载。

运行时另包括固定的 npm/Python 依赖及二进制。版本信息来自 `export/mcp/locks/versions.json` 和各 lock：Playwright MCP 0.0.83、Firebase tools 15.33.0、Serena agent 1.7.0、Bun 1.4.3、Terraform MCP 0.4.0；仅描述这个快照。依赖许可按包内/分发包 license 处理，不用宿主项目许可覆盖传递依赖。

便携运行时迁移应重定位 launcher、venv home 与状态根，而非复制原电脑绝对路径。此次迁移已采用项目内 Node 优先；Serena 通过目标 venv Python 的模块入口启动，避开带旧绝对路径的 console exe。实际运行和迁移证据由资源包报告保存，技能查询脚本不修改运行时。

补充自编 `export/custom-skills/agent-foundation` 也纳入来源覆盖，源快照是 `136cb59eb1a7fa778ff640bd23d2cc0a0a58d1e1`；它不是原始 667 个上游导出技能之一。

## 许可差异必须保留

- 多数 SDK/CLI 是 MIT 或 Apache-2.0，但不能从组织名推断许可。
- anthropics/claude-code 根许可为商业服务条款；claude-agent-sdk-python 的 MIT 不重新许可其调用的产品。
- anthropics/skills 的文档处理技能有 source-available 条款；OpenAI/Anthropic 技能/插件库按组件核对。
- Cherry Studio 的 AGPL、LobeHub Community License、Open WebUI License 各自保留；不统一当宽松开源。
- lencx/ChatGPT 的本次 v2-dev 未找到根许可文件，默认不据此授予复用权。
- MCP 仓库有 Apache/MIT 过渡和文档 CC-BY 条款；按本次 LICENSE 和文件头核对。

## 证据强度

本技能的 source index 表示选择性源码/文档检查，hash 确保定位同一快照。它不表示逐行审阅全部约十万文件、不表示所有 667 工作流运行、更不表示 35 应用部署成功。完整覆盖是来源无遗漏、设计用途可检索、边界明确。

历史可运行证据从 `reports/mcp-summary.json`、`mcp-scope-correction.json`、`mcp-remaining-41.json`、`claude-runtime-functional.json`、`trae-gateway-regression.json`、`trae-native-events.json` 等读取。Claude 的部分功能检查使用确定性模型 stub；MCP 业务执行是真实本地工具；远程账号业务未普遍验证。安装和静态结构检查必须与目标客户端真实加载分开报告。
