---
type: concept
tags: [engineering-craft, frontend, declarative-ui, abstractions]
---
# Declarative UI (schema-driven builders)

Borrowed straight from game development: like Doom's level editor producing declarative level files, Viktor's idea is to describe UI as schemas that get compiled into components ([[voice-2-faster-ui-development]]). Tools like [[react-admin]] already do this cross-project, but they're standardized to a lowest common denominator; his stronger claim is that a *project-specific* builder is worth building even inside ONE project — it's far cheaper than a cross-project framework, and you'd be writing all those screens anyway. Because it's project-specific, when a feature request arrives he extends the schema the same day, and every screen in the app picks up the behavior consistently.

His own layered stack: a grid builder whose schema turns ~2 of his parameters into ~5 low-level [[material-ui|Material]] grid params, encoding consistent behavior, settings persistence, API compatibility, per-row actions, delete confirmations and navigation; a form builder; and a PageBuilder producing whole CRUD pages — always with the option to drop down a layer for genuinely custom pages ([[voice-2-faster-ui-development]]). He's puzzled the approach isn't popular: people use forms libraries raw on every screen even though every project has customizations (API-specific error formats bound to fields, say) that one more declarative layer would encode exactly once. Offered with his explicit caveat: it's idea-sharing — "maybe it won't fly on your project."

## Covered in
- [[voice-2-faster-ui-development]] — the whole concept: level-editor analogy, grid/form/PageBuilder layers, same-day schema extension, why project-specific beats framework

## Related
[[abstractions]] — the builder is a deliberately added abstraction layer with an escape hatch
[[software-design]] — encode project conventions once instead of per-screen
[[react-admin]] — the cross-project version of the same idea
[[material-ui]] — the low-level layer his builders compile to
[[react]] — the ecosystem where he sees teams afraid to add such layers
