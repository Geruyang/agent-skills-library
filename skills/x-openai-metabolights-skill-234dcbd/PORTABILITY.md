# 迁移记录

来源：`upstream/openai/plugins`

原名称：`metabolights-skill`

原始副本位于导出包 `original-skills/x-openai-metabolights-skill-234dcbd`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：reviewed-unchanged。保留 MetaboLights HTTP 请求脚本、字段与 EBI 官方地址；未发现宿主绑定。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：Python 3、随包 scripts/rest_request.py；https://www.ebi.ac.uk/metabolights/ws 网络访问。
- 保留的真实产品/API/名称：MetaboLights、EBI、https://www.ebi.ac.uk/metabolights/ws。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
