# 集成与运行

下面命令针对固定源码快照。发布包的版本以已安装元数据为准；源码中的开发占位版本不是可部署版本。

## Harness

源码开发要求 Python >=3.13、uv。仓库根运行 `uv sync --locked --package a13n-harness`。最小离线例子在技能的 `assets/offline_agent.py`；复制到仓库后运行 `uv run python offline_agent.py`，预期输出 `Hello from the Harness`。该例子没有模型账号或网络推理依赖，但首次同步依赖需要下载。

使用 `HarnessBuilder().build(AgentSpec(), output_type=str, model=FunctionModel(...))`，或在 AgentSpec 内指定模型；选择一个模型来源，避免两处冲突。真实模型按任务选择实际可用的 provider/API，不从示例旧型号推断账号权限。

有状态应用参照 `examples/agent-app`：`uv sync --locked`、`uv run pytest` 在例子目录执行。应覆盖正常多轮、序列化后重启恢复、取消、失败后资源释放，不只检查模型文字。

工具/MCP 参照 `docs/a13n-harness/mcp.md`。离线 MCP 例子使用 FastMCP 和 FunctionModel；不要猜测当前版本 SDK 构造参数。能力组合参照 `capabilities.md`；插件扩展参照 `examples/plugins` 与 `examples/provider-plugin`。

## Service

需要 Docker + Docker Compose；使用模型需要 provider 认证，或框架支持的符合条件 ChatGPT 登录。此登录资格由服务及账号实际结果决定，不能因使用 ChatGPT 客户端而假设已授权。

仓库根可用：

```sh
docker compose -f deploy/docker/compose/a13n-service.yaml up -d --wait --pull always
```

默认 Console `http://127.0.0.1:8080`。首次自行注册管理员，再连接模型、创建 agent 并试运行。堆栈包含 Service/Console、PostgreSQL、Redis，挂载主机 Docker socket。共享部署先阅读 Compose README，固定发布镜像、配置 HTTPS/公共 URL、引导管理员、持久卷与加密设置；不得把开发默认值直接作为共享部署配置。

连接应用读取 `docs/a13n-service/connect-application.md`、`sdks.md` 和 API reference。区分工作区 API 认证与上游模型认证。检查 `/readyz`、Compose 状态与日志；启动成功不等于真实模型或环境业务成功。保留卷的 down 可停止；删除卷会永久删除数据，仅在明确要求重置时执行。

## Harness UI

`uv tool install a13n-harness-ui` 后，在目标项目运行 `a13n-harness-ui` 或 `a13n-harness-ui webui`。按其首次配置流程选择模型和执行权限。Full Control 使用主机账号；`--no-share-computer` 关闭 WebUI 原生主机文件/终端共享。此项是框架功能说明，不要求修改宿主客户端权限。

Windows 上区分可安装的 Python 包、原生 Envd 与 Docker Linux 环境的前提；缺少工具链时报告实际检查结果，按目标组件文档选用 Docker Desktop/WSL，不声称所有原生组件均已在 Windows 验证。
