# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`access`

原始副本位于导出包 `original-skills/x-anthropics-access-1660754`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
user-invocable: true
allowed-tools:
- Read
- Write
- Bash(ls *)
- Bash(mkdir *)
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`reviewed-unchanged`。

完整入口及绑定候选已静态审阅；内容为通用领域指导或明确产品教程，未发现需改写的Codex执行绑定。

运行依赖：Claude iMessage channel及其实际access.json；仅可信终端用户请求可改权限

保留产品提及：Claude专属产品教程/可选配置保留，未将其改名为TRAE

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
