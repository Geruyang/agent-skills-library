# D3 Architecture Patterns

## What Problem This Solves

This reference keeps D3 projects maintainable inside modern applications.

## When to Use It

Use this when integrating D3 with React, Svelte, or any other framework-owned UI.

## Key Takeaways

- Separate data shaping, scales, geometry derivation, rendering, and interaction state.
- Let the framework own container structure when possible.
- Keep D3 imperative islands narrow and purposeful.

## Common Mistakes

- Mixing data loading, layout math, DOM mutation, and app state in one effect.
- Letting D3 fight the framework for ownership of the same nodes.

## Adjacent Skills

- `../SKILL.md`
- `../../x-openai-typescript-data-visualization-engineering-02d5aac/SKILL.md`

## Source Links

- [D3 API](https://d3js.org/api)
