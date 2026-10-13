# 迁移记录

来源：`upstream/openai/plugins`

原名称：`catalyst-calendar`

原始副本位于导出包 `original-skills/x-openai-catalyst-calendar-ec79012`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。将财务交付 intake 的固定 request_user_input 调用改为实际提问能力/普通对话，保留仅追问实质缺失项与已解析偏好。
- 阅读证据：`SKILL.md` (126 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：权威金融资料与模型/工作簿；共享 intake/HTML/support 参考；按交付需要的本地 XLSX/HTML 生成和重算能力。；原相对资源链接待根任务统一解析：../../shared/deliverable-intake-policy.md, ../../shared/html-artifact-standard.md, ../../shared/plugin-routing-playbook.md, ../../shared/workflow-source-resolution.md, ../public-equity-investing/SKILL.md, ../user-context/SKILL.md
- 保留的真实产品/API/URL：OpenAI、Expo、Render。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
