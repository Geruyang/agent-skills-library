# 迁移记录

来源：`upstream/openai/plugins`

原名称：`collect-files-with-request`

原始副本位于导出包 `original-skills/x-openai-collect-files-with-request-0e2ea8d`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：adapted。补充 Dropbox 文件请求能力发现、等价 API/CLI 核验与本地请求规格回退；保留目录和创建确认门槛。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：已授权 Dropbox 文件请求及文件夹操作能力；缺少时无法创建真实上传链接。
- 保留的真实产品/API/名称：Dropbox。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
