---
name: x-openai-canva-resize-for-social-media-7485ec7
description: Resize a Canva design into multiple social media formats (Facebook post, Facebook story, Instagram post, Instagram story, LinkedIn post). Use this skill when users want to resize Canva designs specifically for multiple social media platforms in one operation, rather than resizing to a single format manually.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Canva Resize for Social Media

Automatically resize a single Canva design into multiple social media formats.

## Overview

This skill enables rapid multi-platform content distribution by taking a single Canva design and creating optimized versions for:
- Facebook post
- Facebook story
- Instagram post
- Instagram story
- LinkedIn post

All resized versions are provided with Canva edit links so users can further edit or download them directly from Canva.

## Workflow

### Step 1: Identify the Source Design

Determine which Canva design the user wants to resize. This can be provided in three ways:

1. **Direct design ID**: User provides a design ID (starts with "D")
   - Example: "resize design DABcd1234ef for all social media"
   - Use the design ID directly with `get-design` tool to retrieve design information

2. **Direct design URL**: User provides a Canva design link
   - Example: "resize https://www.canva.com/design/DABcd1234ef/... for all social media"
   - Extract the design ID from the URL (the part after `/design/` and before the next `/` or query parameter)
   - Use the extracted design ID with `get-design` tool

3. **Search by design name**: Use `search-designs` tool with the design name as the query
   - Example: "resize my Demo Brand Template: Brix&Hart Flyer design for all social media"
   - Use the exact name/phrase the user provides as the search query
   - If multiple matches are found, present options and ask the user to select one

4. **Current context**: If the user just created or edited a design in the conversation, use that design ID

**Implementation note**: When searching by name, pass the design name directly to `search-designs` as the query parameter. The tool will find the best match based on the design title.

### Step 2: Retrieve Source Design Information

Use the `get-design` tool with the design ID to:
- Confirm the design exists and is accessible
- Get the design title (for naming resized versions)
- Verify design type compatibility

### Step 3: Ask Which Platforms and Formats

Present the available formats and ask which ones the user wants:

```
Which platforms and formats would you like to resize for?

- Facebook post (1200×630)
- Facebook story (1080×1920)
- Instagram post (1080×1080)
- Instagram story (1080×1920)
- LinkedIn post (1200×627)
```

If the user says "all" or "all social media", use all five. Otherwise, only resize for the ones they select.

### Step 4: Resize to Selected Formats

Execute the resize operations **in parallel** by calling the `resize-design` tool once for each selected format. Use these exact specifications:

**Available formats and dimensions:**

1. **Facebook Post**: 1200 × 630 pixels (custom)
   ```
   design_type: { type: "custom", width: 1200, height: 630 }
   ```

2. **Facebook Story**: 1080 × 1920 pixels (custom)
   ```
   design_type: { type: "custom", width: 1080, height: 1920 }
   ```

3. **Instagram Post**: 1080 × 1080 pixels (custom)
   ```
   design_type: { type: "custom", width: 1080, height: 1080 }
   ```

4. **Instagram Story**: 1080 × 1920 pixels (custom)
   ```
   design_type: { type: "custom", width: 1080, height: 1920 }
   ```

5. **LinkedIn Post**: 1200 × 627 pixels (custom)
   ```
   design_type: { type: "custom", width: 1200, height: 627 }
   ```

**Note**: Facebook Story and Instagram Story have identical dimensions. Create both versions but inform the user they're the same size.

**Error handling**: If a resize operation fails, continue with remaining formats and report which formats succeeded and which failed at the end.

### Step 5: Present Results with Edit Links

**Present comprehensive results to the user:**

Provide the user with a summary including:

1. **Summary**: Confirm which formats were created successfully
2. **Design edit links**: Canva editor URLs for each resized design so users can make further edits or download directly from Canva
3. **Note about duplicates**: Mention that Facebook Story and Instagram Story have identical dimensions

**Presentation format example:**
```
✅ Successfully resized your design for all social media platforms!

Edit Links:

**Facebook Post** (1200×630)
- [Edit in Canva](edit_url)

**Facebook Story** (1080×1920)
- [Edit in Canva](edit_url)

**Instagram Post** (1080×1080)
- [Edit in Canva](edit_url)

**Instagram Story** (1080×1920)
- [Edit in Canva](edit_url)

**LinkedIn Post** (1200×627)
- [Edit in Canva](edit_url)

Note: Facebook Story and Instagram Story use the same dimensions (1080×1920).
```

**Implementation details**:
- Design edit links come from the `resize-design` tool response (use the `urls.edit_url` field from each resized design)
- Present links as clickable URLs, not just plain text
- Organize by platform for easy scanning

## Key Implementation Notes

- **Compatibility**: Discover authenticated Canva design lookup and resize capabilities in the current host. Map `get-design`, `search-designs`, and `resize-design` to the connected MCP tools or a documented Canva API with the same design-copy and edit-link behavior. Validate the actual schema before calling it. If resizing is unavailable or the account lacks access, report that blocker; do not claim that new designs were created
- **Parallel execution**: Resize operations should be performed in parallel for efficiency
- **Consistent naming**: Use the source design title with platform suffix for resized designs
- **Error resilience**: If any operation fails, complete the remaining operations and clearly report what succeeded/failed
- **User confirmation**: Do not require user approval between steps - execute the full workflow automatically unless errors occur
- **Format accuracy**: Always use the exact pixel dimensions specified above for each platform
