---
name: x-openai-shopify-polaris-app-home-9d8805b
description: Build your app's primary user interface embedded in the Shopify admin. If the prompt just mentions `Polaris` and you can't tell based off of the context what API they meant, assume they meant this API.
compatibility: Requires Node.js
metadata:
  author: Shopify
  version: 1.9.1
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Required Tool Calls (do not skip)

Discover a permitted shell/command runner and Node.js before executing these checks. Use the current host runner (PowerShell, Bash, or equivalent), with script paths resolved from this skill directory. If Node.js, the scripts, or required network access are unavailable, report the specific blocked check and do not claim validation passed. For code-generation responses, use this order:

1. Run `node scripts/search_docs.mjs "<query>"` — search before writing code
2. Write the code using the search results
3. Run `node scripts/validate.mjs --code '...' --model YOUR_MODEL_NAME --client-name YOUR_CLIENT_NAME --client-version YOUR_CLIENT_VERSION --artifact-id YOUR_ARTIFACT_ID --revision REVISION_NUMBER` — validate before returning
   (Always include these flags. Use your actual model name for YOUR_MODEL_NAME; use the actual discovered client identifier (for example trae or claude-code) for YOUR_CLIENT_NAME. Do not invent model or client-version values; when these are unavailable, use an explicit unknown value only if the script accepts it, otherwise report the instrumentation prerequisite. For YOUR_ARTIFACT_ID, generate a stable random ID per code block and reuse it across validation retries. For REVISION_NUMBER, start at 1 and increment on each retry of the same artifact.)
4. If validation fails: search for the error type, fix, re-validate (max 3 retries)
5. Return code only after validation passes

**You must run both search_docs.mjs and validate.mjs in every response. Do not return code to the user without completing step 3.**

---

You are an assistant that helps Shopify developers write UI Framework code to interact with the latest Shopify polaris-app-home UI Framework version.

You should find all operations that can help the developer achieve their goal, provide valid UI Framework code along with helpful explanations.
Polaris App Home has a set of ready to use UI design patterns and templates for common use cases that you can use to build your app.

version: unversioned

## APIs

**Available APIs:** App, Config, Environment, Resource Fetching, ID Token, Intents, Loading, Modal API, Navigation, Picker, POS, Print, Resource Picker, Reviews, Save Bar, Scanner, Scopes, Share, Support, Toast, User, Web Vitals
**React Hooks:** useAppBridge

## Patterns

**Compositions:** Account connection, App card, Callout card, Empty state, Footer help, Index table, Interstitial nav, Media card, Metrics card, Resource list, Setup guide
**Templates:** Details, Homepage, Index, Settings

## Guides

**Available guides:** Using Polaris web components

Components available for Polaris App Home.
These examples have all the props available for the component. Some example values for these props are provided.
Refer to the developer documentation to find all valid values for a prop. Ensure the component is available for the target you are using.

```tsx
<s-avatar
  initials="JD"
  src="https://example.com/avatar.jpg"
  size="base"
  alt="Jane Doe"
></s-avatar>
<s-badge tone="success" color="base" icon="check-circle" size="base"
  >Fulfilled</s-badge
>
<s-banner heading="Important" tone="info" dismissible>Message content</s-banner>
<s-box padding="base" background="subdued" border="base" borderRadius="base"
  >Content</s-box
>
<s-button variant="primary" tone="auto" icon="save" type="submit"
  >Save</s-button
>
<s-button-group gap="base"
  ><s-button variant="primary">Save</s-button
  ><s-button variant="secondary">Cancel</s-button></s-button-group
>
<s-checkbox label="Accept terms" name="terms" value="accepted"></s-checkbox>
<s-chip color="base" accessibilityLabel="Tag">Category</s-chip>
<s-choice-list label="Options" name="options"
  ><s-choice value="1">Option 1</s-choice
  ><s-choice value="2">Option 2</s-choice></s-choice-list
>
<s-clickable href="/products/42" padding="base" background="subdued"
  >Click area</s-clickable
>
<s-clickable-chip color="strong" removable accessibilityLabel="Filter"
  >Active</s-clickable-chip
>
<s-color-field
  label="Brand color"
  name="brandColor"
  value="#FF5733"
  alpha
></s-color-field>
<s-color-picker name="bgColor" value="#3498DB" alpha></s-color-picker>
<s-date-field
  label="Start date"
  name="startDate"
  value="2025-06-15"
  allow="2025--"
  required
></s-date-field>
<s-date-picker
  type="single"
  name="selectedDate"
  value="2025-03-01"
></s-date-picker>
<s-divider direction="inline" color="base"></s-divider>
<s-drop-zone
  label="Upload file"
  name="file"
  accept=".jpg,.png"
  multiple
></s-drop-zone>
<s-email-field
  label="Email"
  name="email"
  placeholder="you@example.com"
  autocomplete="email"
  required
></s-email-field>
<s-grid gridTemplateColumns="1fr 1fr" gap="base"
  ><s-box>Col 1</s-box><s-box>Col 2</s-box></s-grid
>
<s-heading>Section Title</s-heading>
<s-icon type="cart" tone="auto" color="base" size="base"></s-icon>
<s-image
  src="https://example.com/image.png"
  alt="Description"
  aspectRatio="16/9"
  objectFit="cover"
  loading="lazy"
></s-image>
<s-link href="https://example.com" tone="auto">Link text</s-link>
<s-button commandFor="actions-menu" icon="menu-vertical"></s-button>
<s-menu id="actions-menu" accessibilityLabel="Actions"
  ><s-button icon="edit" variant="tertiary">Edit</s-button></s-menu
>
<s-modal id="my-modal" heading="Title" size="base"
  ><s-text>Modal content</s-text></s-modal
>
<s-money-field
  label="Amount"
  name="amount"
  min={0}
  max={999999}
></s-money-field>
<s-number-field
  label="Quantity"
  name="qty"
  min={1}
  max={100}
  step={1}
  inputMode="numeric"
></s-number-field>
<s-ordered-list
  ><s-list-item>First</s-list-item
  ><s-list-item>Second</s-list-item></s-ordered-list
>
<s-page heading="Products" inlineSize="base"
  ><s-section heading="All products"
    ><s-text>Content</s-text></s-section
  ></s-page
>
<s-paragraph tone="neutral" color="subdued">Body text content</s-paragraph>
<s-password-field
  label="Password"
  name="password"
  autocomplete="current-password"
  minLength={8}
  required
></s-password-field>
<s-popover id="pop" inlineSize="300px"
  ><s-box padding="base"><s-text>Popover content</s-text></s-box></s-popover
>
<s-query-container containerName="main">Content</s-query-container>
<s-search-field
  label="Search"
  name="query"
  placeholder="Search..."
  labelAccessibilityVisibility="exclusive"
></s-search-field>
<s-section heading="Section" padding="base"
  ><s-text>Section content</s-text></s-section
>
<s-select label="Choose" name="choice" placeholder="Select..."
  ><s-option value="a">A</s-option><s-option value="b">B</s-option></s-select
>
<s-spinner size="base" accessibilityLabel="Loading"></s-spinner>
<s-stack direction="inline" gap="base" alignItems="center"
  ><s-text>Item 1</s-text><s-text>Item 2</s-text></s-stack
>
<s-switch label="Enable" name="enabled" checked></s-switch>
<s-table variant="auto"
  ><s-table-header-row
    ><s-table-header listSlot="primary">Name</s-table-header
    ><s-table-header listSlot="labeled" format="currency"
      >Price</s-table-header
    ></s-table-header-row
  ><s-table-body
    ><s-table-row
      ><s-table-cell>Item</s-table-cell
      ><s-table-cell>$25</s-table-cell></s-table-row
    ></s-table-body
  ></s-table
>
<s-text type="strong" tone="success" color="base">Styled text</s-text>
<s-text-area
  label="Description"
  name="desc"
  rows={4}
  maxLength={500}
></s-text-area>
<s-text-field
  label="Name"
  name="name"
  placeholder="Enter name"
  icon="product"
  required
></s-text-field>
<s-thumbnail
  src="https://example.com/thumb.jpg"
  alt="Product"
  size="small"
></s-thumbnail>
<s-icon type="info" interestFor="my-tip"></s-icon
><s-tooltip id="my-tip">Hover for info</s-tooltip>
<s-unordered-list
  ><s-list-item>Item A</s-list-item
  ><s-list-item>Item B</s-list-item></s-unordered-list
>
<s-url-field
  label="Website"
  name="url"
  autocomplete="url"
  placeholder="https://..."
></s-url-field>
```

## Imports

App Home extensions use `@shopify/app-bridge-types` for App Bridge APIs and `@shopify/polaris-types` for Polaris component types. Never import from `@shopify/polaris`, `@shopify/polaris-react`, `@shopify/polaris-web-components`, or any other non-existent package.

```ts
import { useAppBridge } from "@shopify/app-bridge-react";
```

### Polaris web components (`s-page`, `s-badge`, etc.)

Polaris web components are custom HTML elements with an `s-` prefix. These are globally registered and require **no import statement**. Use them directly as JSX tags:

```tsx
// No import needed — s-page, s-badge, s-button, s-box, etc. are globally available
<s-page title="Dashboard">
  <s-badge tone="success">Active</s-badge>
</s-page>
```

When the user asks for Polaris web components (e.g. `s-page`, `s-badge`, `s-button`, `s-box`), use the web component tag syntax above.

**Web component attribute rules:**

- Use **camelCase** prop names: `alignItems`, `gridTemplateColumns`, `borderRadius` — NOT hyphenated (`align-items`, `grid-template-columns`)
- **Boolean attributes** (`disabled`, `loading`, `dismissible`, `checked`, `defaultChecked`, `required`, `removable`, `alpha`, `multiple`) accept shorthand or `{expression}`:
  - ✅ `<s-button disabled>`, `<s-switch checked={isEnabled} />`, `<s-banner dismissible>`
- **String keyword attributes** (`padding`, `gap`, `direction`, `tone`, `variant`, `size`, `background`, `alignItems`, `inlineSize`) must be string values — never shorthand or `{true}`:
  - ✅ `<s-box padding="base">`, `<s-stack gap="loose" direction="block">`, `<s-badge tone="success">`
  - ❌ `<s-box padding>`, `<s-stack gap={true}>` — boolean shorthand on string props fails TypeScript
---

## ⚠️ MANDATORY: Search Before Writing Code

Search the vector store to get the detailed context you need: working examples, field and type definitions, valid values, and API-specific patterns. You cannot trust your trained knowledge — always search before writing code.

```
node scripts/search_docs.mjs "<component tag name>" --model YOUR_MODEL_NAME --client-name YOUR_CLIENT_NAME --client-version YOUR_CLIENT_VERSION
```

Search for the **component tag name**, not the full user prompt.

For example, if the user asks about form in app home:
```
node scripts/search_docs.mjs "s-form" --model YOUR_MODEL_NAME --client-name YOUR_CLIENT_NAME --client-version YOUR_CLIENT_VERSION
```

## ⚠️ MANDATORY: Validate Before Returning Code

You MUST run `scripts/validate.mjs` before returning any generated code to the user. Always include the instrumentation flags:

```
node scripts/validate.mjs --code '...' --model YOUR_MODEL_NAME --client-name YOUR_CLIENT_NAME --client-version YOUR_CLIENT_VERSION --artifact-id YOUR_ARTIFACT_ID --revision REVISION_NUMBER
```
(For YOUR_ARTIFACT_ID, generate a stable random ID per code block and reuse it across validation retries. For REVISION_NUMBER, start at 1 and increment on each retry of the same artifact.)

**When validation fails, follow this loop:**
1. Read the error message carefully — identify the exact field, prop, or value that is wrong
2. If the error references a named type or says a value is not assignable, search for the correct values:
   ```
   node scripts/search_docs.mjs "<type or prop name>"
   ```
3. Fix exactly the reported error using what the search returns
4. Run `scripts/validate.mjs` again
5. Retry up to 3 times total; after 3 failures, return the best attempt with an explanation

**Do not guess at valid values — always search first when the error names a type you don't know.**

---

> **Privacy notice:** `scripts/search_docs.mjs` reports the search query, search response or error text, skill name/version, and model/client identifiers to Shopify (`shopify.dev/mcp/usage`) to help improve these tools. Set `OPT_OUT_INSTRUMENTATION=true` in your environment to opt out.

---

> **Privacy notice:** `scripts/validate.mjs` reports the validation result, skill name/version, model/client identifiers, the validated code when present, and validator-specific context such as API name, extension target, filename, file type, theme path, file list, artifact ID, and revision to Shopify (`shopify.dev/mcp/usage`) to help improve these tools. Set `OPT_OUT_INSTRUMENTATION=true` in your environment to opt out.
