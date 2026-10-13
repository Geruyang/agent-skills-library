# 迁移记录

来源：`upstream/anthropics/skills`

原名称：`pptx`

原始副本位于导出包 `original-skills/x-anthropics-pptx-155e3b5`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能跨宿主审核（2026-10-12）

- 状态：`adapted`。
- 范围：完整阅读本技能 `SKILL.md`；本项 manifest `host_matches` 为空，无自动命中的额外文件。按正文语义区分宿主调用与真实产品接口。
- 审核结论：Removed unconditional preinstalled-package/sandbox assertions; added runtime/font/render discovery and precise local-delivery/QA limits.
- 能力核验：这是静态移植审计；未安装依赖、未访问账号或硬件、未执行技能业务流程，不能据此声称目标环境可运行。
- 剩余依赖：
  - Node.js and pptxgenjs
  - Python: markitdown[pptx], Pillow, defusedxml, lxml
  - LibreOffice and Poppler/pdftoppm for rendering
  - Image-viewing capability and installed fonts
  - Optional react-icons/react/react-dom/sharp
- 保留的真实产品/协议名称：PowerPoint；pptxgenjs；LibreOffice；OOXML；Office font names。
- 缺失能力处理：按正文的已核验等价能力或本地交付路径执行；没有等价项时明确报告缺失，不伪造工具调用、远端状态或完成结果。
