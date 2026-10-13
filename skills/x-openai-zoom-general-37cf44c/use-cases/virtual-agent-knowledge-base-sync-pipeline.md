# Virtual Agent Knowledge Base Sync Pipeline

Use this flow when knowledge content lives outside Zoom and must stay synchronized for Virtual Agent responses.

## When to Use

- Your source-of-truth KB is in another CMS.
- Web sync alone is not enough for your content structure.
- You need repeatable ingestion and update automation.

## Skill Chain

1. [virtual-agent](../../x-openai-build-zoom-virtual-agent-6f67c33/SKILL.md)
2. [zoom-rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
3. [zoom-oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)

## Typical Flow

1. Decide sync mode: sitemap/link-discovery/manual URLs vs custom API connector.
2. Configure S2S OAuth app and required scopes.
3. Pull content from external source and transform to KB article schema.
4. Upsert articles, tags, and categories into Virtual Agent knowledge base.
5. Reconcile stale entries and monitor sync errors.
6. Re-run sync on release cadence.

## References

- [Virtual Agent Environment Variables](../../x-openai-build-zoom-virtual-agent-6f67c33/references/environment-variables.md)
- [Virtual Agent Troubleshooting](../../x-openai-build-zoom-virtual-agent-6f67c33/troubleshooting/common-drift-and-breaks.md)
- [REST API Skill](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
