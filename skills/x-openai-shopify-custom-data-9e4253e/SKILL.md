---
name: x-openai-shopify-custom-data-9e4253e
description: MUST be used first when prompts mention Metafields or Metaobjects. Use Metafields and Metaobjects to model and store custom data for your app. Metafields extend built-in Shopify data types like products or customers, Metaobjects are custom data types that can be used to store bespoke data structures. Metafield and Metaobject definitions provide a schema and configuration for values to follow.
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

<critical-instructions>
# Best Practise for working with Metafields and Metaobjects

# ESSENTIAL RULES

- **ALWAYS** show creating metafield/metaobject definitions, then writing values, then retrieving values.
- **NEVER** show or offer alternate approaches to the same problem if not explicitly requested. It will only increase the user's confusion.
- Keep examples minimal -- avoid unnecessary prose and comments
- Remember the audience for this guidance is app developers -- they do not have access to the Shopify Admin site
- Follow this guidance meticulously and thoroughly

REMEMBER!!! Other documentation can flesh out this guidance, but the instructions here should be followed VERY CLOSELY and TAKE PRECEDENCE!

# ALWAYS: First, create definitions

## with TOML (99.99% of apps)

```toml
# shopify.app.toml

# Metafield definition -- owner type is PRODUCT, namespace is $app, key is care_guide
[product.metafields.app.care_guide]
type = "single_line_text_field"
name = "Care Guide"
access.admin = "merchant_read_write"

# Metaobject definition -- type is $app:author
[metaobjects.app.author]
name = "Author"
display_name_field = "name"
access.storefront = "public_read"

[metaobjects.app.author.fields.name]
name = "Author Name"
type = "single_line_text_field"
required = true

# Link metaobject to product
[product.metafields.app.author]
type = "metaobject_reference<$app:author>"
name = "Book Author"
```

Why: Version controlled, auto-installed, type-safe. GraphQL (Admin/Storefront) is used for reading or writing values after the TOML definitions already exist. Fields/objects can be edited by merchants when `access.admin = "merchant_read_write"` is set.

**NEVER** include `metafieldDefinitionCreate`, `metaobjectDefinitionCreate` GraphQL if TOML is the correct fit.

### Exceptions (0.01% of apps)

**NEVER, EVER** show these unless strictly required:

- Apps that **REQUIRE** creating definitions at **runtime** (i.e. types are configured dynamically by merchants) should use `metafieldDefinitionCreate`, `metaobjectDefinitionCreate`
- Apps that want **other apps** to read/write their data should use the above GraphQL, and "merchant-owned" namespace

# CRITICAL: App-Owned Metaobject and Metafield identification

- Metaobjects defined with `[metaobjects.app.example...]` in `shopify.app.toml`, MUST be accessed using `type: $app:example`
- Metafields defined with `[product.metafields.app.example]` MUST be accessed using `namespace: $app` and `key: example`
  - The same applies to other owner types, like customers, orders, etc.
- Avoid customizing namespaces for metafields.
- Avoid the common mistake of using `namespace: app`. This is profoundly incorrect.

# NEXT: demonstrate writing metafield and metaobject values via Admin API

## Writing metafields

**ALWAYS** use `metafieldsSet` to write metafields. `namespace` should normally be excluded as the default is $app.

```graphql
mutation {
  metafieldsSet(metafields:[{
    ownerId: "gid://shopify/Product/1234",
    key: "example",
    value: "Hello, World!"
  }]) { ... }
}
```

## Writing metaobjects

**ALWAYS** use `metaobjectUpsert` to write metaobjects.

```graphql
mutation {
  metaobjectUpsert(handle: {
    type: "$app:author",
    handle: "my-metaobject",
  }, metaobject: {
    fields: [{
      key: "example",
      value: "Hello, world!"
    }]
  }) { ... }
}
```

# FINALLY: demonstrate reading metafield and metaobject values

## Loading metafields

Metafields are accessed via their owning type (e.g. a Product). `namespace` should normally be excluded as the default is $app.

- Always prefer `jsonValue` where possible as it better serialises complex types
- Always alias metafield loads for easy reference

```graphql
# Admin API
query {
  product(id: "gid://shopify/Product/1234") {
    example: metafield(key: "example") {
      jsonValue
    }
  }
}
# Storefront API
query {
  product(handle: "wireless-headphones-1") {
    example: metafield(key: "example") {
      value
    }
  }
}
```

## Loading metaobjects

```graphql
# Admin API
query {
  metaobjects(type: "$app:author", first: 10) {
    nodes {
      handle
      example: field(key: "example") {
        jsonValue
      }
    }
  }
}
# Storefront API
query {
  metaobjects(type: "$app:author", first: 10) {
    nodes {
      handle
      example: field(key: "example") {
        value
      }
    }
  }
}
```

### Access Metafields directly in checkout extensions

**DO**: Access app-owned metafields directly (NO network call):

```tsx
function Extension() {
  // ESSENTIAL: Register this metafield in `shopify.extension.toml`
  const [energyRating] = useAppMetafields({
    namespace: "$app",
    key: "energy-rating",
    type: "product",
  }).filter((entry) => entry.target.id === productVariantId);
}
```

**DON'T**: Make network calls for app-owned metafields.

### Access Metafields in Shopify Functions

Use the GraphQL input query to select metafields to load:

```graphql
query Input {
  cart {
    lines {
      merchandise {
        __typename
        ... on ProductVariant {
          example: metafield(namespace: "$app", key: "example") {
            jsonValue
          }
        }
      }
    }
  }
}
```

Docs: [Metafields & Metaobjects](https://shopify.dev/docs/apps/build/custom-data)
</critical-instructions>

### Always use Shopify CLI

- **CLI:** ALWAYS use Shopify CLI to scaffold apps and extensions. Never hand-roll files: `shopify app init`, `shopify app generate extension`, `shopify app dev`, `shopify app deploy`.
- For CLI installation, setup, upgrade, or troubleshooting, use `shopify-use-shopify-cli`.
