# 迁移记录

来源：`upstream/openai/plugins`

原名称：`google-slides`

原始副本位于导出包 `original-skills/x-openai-google-slides-f9361a1`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。Google Slides 读取、导出和渲染改为经验证连接器或官方API；原宿主 host 适配器明确为条件依赖，不再强制 functions.exec。
- 审核入口与匹配资源：`SKILL.md`。
- 仍需环境能力：Authenticated Google Slides and Drive access；Node.js for local parsers；PDF renderer / image viewer。
- 保留的真实产品或兼容字段：Google Slides；Google Drive。
