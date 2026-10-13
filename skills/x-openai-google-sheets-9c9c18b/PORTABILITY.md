# 迁移记录

来源：`upstream/openai/plugins`

原名称：`google-sheets`

原始副本位于导出包 `original-skills/x-openai-google-sheets-9c9c18b`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

移除专属插件URI、导入函数示例和artifact_tool硬依赖，交付区分成功原生导入与本地备选。

运行依赖：Google Drive/Sheets认证MCP或API；本地工作簿库、可选浏览器渲染

保留产品提及：Google Sheets/Drive MIME和API字段；connector upload_mode保持为专属示例

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
