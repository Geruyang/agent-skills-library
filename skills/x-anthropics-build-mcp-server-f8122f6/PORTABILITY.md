# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`build-mcp-server`

原始副本位于导出包 `original-skills/x-anthropics-build-mcp-server-f8122f6`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

MCP通用入口按目标客户端获取文档，Claude打包/工具示例明确产品作用域。

运行依赖：MCP SDK及Node/Python、目标客户端官方能力；远程部署/认证按任务需要

保留产品提及：Claude连接器、MCPB、MCP Apps真实产品协议示例

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
