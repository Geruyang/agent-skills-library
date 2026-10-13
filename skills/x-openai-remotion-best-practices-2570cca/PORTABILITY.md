# 迁移记录

来源：`upstream/openai/plugins`

原名称：`remotion-best-practices`

原始副本位于导出包 `original-skills/x-openai-remotion-best-practices-2570cca`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 4.0.506
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 115 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：Remotion预览和文件监视故障建议适配任意宿主/OS，避免Codex/macOS原因假设。
- 仍需验证：Node.js、Remotion、浏览器和可用文件watcher。
- 保留产品语义：Remotion。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。

## 上游资源缺口修正（2026-10-12）

- 源仓库没有 MapTiler 的 `assets/RiverReveal.tsx`、`assets/CountryLabel.tsx`、`assets/example-Root.tsx`，以及 Cesium 的 `assets/CesiumFlythrough.tsx`、`assets/example-Root.tsx`；此问题同样存在于本技能内的嵌套副本。
- 已在路由入口、技术步骤、资源清单及相关参考说明中明确缺失事实，取消“已捆绑/直接复制运行”的承诺。相关分支必须由用户提供真实组件，或在已授权项目中先按现存架构与渲染规范实现；确认文件、导入及 composition 注册后检查静帧和短序列。未补齐时报告该分支阻塞。
- MapTiler 现有 provider-vector helper、配套数据/脚本及其他地图技术保持原用途；不得用瓦片矢量替代任务要求的有序自定义几何。
- 验证范围：核对四组嵌套文档副本的缺失资源说明；仅修改文档及代码注释，未创建假组件，未安装依赖、访问服务或宣称已完成渲染。
