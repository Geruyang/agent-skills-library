# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`configure`

原始副本位于导出包 `original-skills/x-anthropics-configure-6e9f182`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
user-invocable: true
allowed-tools:
- Read
- Write
- Bash(ls *)
- Bash(mkdir *)
- Bash(echo *)
- Bash(chmod *)
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`reviewed-unchanged`。
- 审核范围：完整读取 `SKILL.md` 与 2 个可读文本文件；复核 0 条原清单宿主匹配。
- 结论：完整程序读取入口及可读支持文件，复核frontmatter、执行路径、工具与产品语境；未发现需改写的Codex执行宿主绑定。
- 剩余依赖：Named MCP integration must be installed and its actual schema discovered；Relevant service authentication/network only when the workflow uses it；Claude Code product or its local data/plugin contract where that is the requested target。
- 保留产品语义：Product/API/model names, documentation URLs and target-specific configuration remain unchanged。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
