# 迁移记录

来源：`upstream/openai/plugins`

原名称：`magicpath`

原始副本位于导出包 `original-skills/x-openai-magicpath-5770581`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: Bash(npx -y magicpath-ai *)
user-invocable: true
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`adapted`。
- 审核范围：完整读取 `SKILL.md` 与 5 个可读文本文件；复核 2 条原清单宿主匹配。
- 结论：画布浏览器改为可用嵌入浏览器或用户浏览器链接，MagicPath CLI与账户仍是实际依赖。
- 剩余依赖：Node.js/npx and magicpath-ai CLI；MagicPath account and project permissions；Browser or manual review for canvas verification。
- 保留产品语义：。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
