---
name: x-openai-canva-branded-presentation-3bc0a21
description: Create on-brand Canva presentations from an outline or brief. Use when the user asks to create a branded presentation, make an on-brand deck, turn an outline into slides, or generate a presentation from a brief. Input can be text directly in the message, a Canva design ID, a reference to a Canva doc by name, or a Canva design link (e.g., https://www.canva.com/design/...).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Canva Branded Presentation Creator

Create professional, on-brand presentations in Canva from user-provided outlines or briefs.

## Workflow

1. **Get the content source**
   - If the user provides text directly, use that as the outline/brief
   - If the user provides a **Canva design ID** directly (typically starts with `D`, e.g. `DABcd1234ef`), use it as `design_id` with `Canva:start-editing-transaction` to read its contents; **do not** use `Canva:search-designs` for a raw ID
   - If the user provides a Canva design link (e.g., `https://www.canva.com/design/DAG.../...`), extract the design ID from the URL and use `Canva:start-editing-transaction` to read its contents
   - If the user references a Canva doc by name, use `Canva:search-designs` to find it, then `Canva:start-editing-transaction` to read its contents

2. **List available brand kits**
   - Call `Canva:list-brand-kits` to retrieve the user's brand kits
   - If only one brand kit exists, use it automatically without asking
   - If multiple brand kits exist, present the options and ask the user to select one

3. **Generate the presentation**
   - Call `Canva:generate-design` with:
     - `design_type`: "presentation"
     - `brand_kit_id`: the selected brand kit ID
     - `query`: a detailed prompt following the presentation format below
   - Show the generated candidates to the user

4. **Finalize**
   - Ask the user which candidate they prefer
   - Call `Canva:create-design-from-candidate` to create the editable design
   - Provide the user with the link to their new presentation

## Presentation Query Format

Structure the query for `Canva:generate-design` with these sections:

**Presentation Brief**
- Title: working title for the deck
- Topic/Scope: 1-2 lines describing the subject
- Key Messages: 3-5 main takeaways
- Style Guide: tone and imagery style based on the brief

**Narrative Arc**
One paragraph describing the story flow (e.g., Hook → Problem → Solution → Proof → CTA).

**Slide Plan**
For each slide include:
- Slide N — "Exact Title"
- Goal: one sentence on the slide's purpose
- Bullets (3-6): short, parallel phrasing with specifics
- Visuals: explicit recommendation (chart type, diagram, image subject)
- Speaker Notes: 2-4 sentences of narrative detail

## Notes

- If multiple brand kits exist, confirm selection before generating; if only one, use it automatically
- If the outline is sparse, expand it into a complete slide plan with reasonable content
- For briefs (narrative descriptions), extract key points and structure them into slides
- Aim for clear, action-oriented slide titles
- Autofill requires a Canva Enterprise plan
