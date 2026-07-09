---
type: tool
tags: [javascript, frontend, ui, framework]
---
# React

React is the dominant JavaScript UI library, and the channel carries rare first-hand history with it: WebbyLab ran React 0.4 in production just two months after its release ([[qa-2-answering-questions]], [[qa-and-plans-for-2024]]). Viktor lived through the whole state-management saga from the inside — Flux announced by Facebook with no implementation, the community's Fluxxor, his team wrapping PubSubJS to fake Flux, then Redux with its boilerplate, then metaprogramming wrappers to tame it. His conclusion after that tour: there is no single "correct" frontend architecture — today his pet projects use no Redux at all, just React plus his own API-access library.

The SSR chapter is a war story with a trophy: his production-grade server-side-rendering article (grown from a KharkivJS talk) won react.js Newsletter's worldwide best-article contest, earning him a ReactConf ticket and an afterparty with the React team, including vjeux ([[qa-and-plans-for-2024]]). React also anchors his default product stack — Node backend, JS frontend, React Native mobile — so one team shares one language.

## Covered in
- [[qa-2-answering-questions]] — first-hand state-management history: React 0.4 in production, Flux → Fluxxor → PubSubJS wrapper → Redux → metaprogramming; no Redux in his pet projects today.
- [[qa-and-plans-for-2024]] — the SSR article that won react.js Newsletter's worldwide contest and the ReactConf afterparty with the React team.

## Related
[[nextjs]] — the React SSR framework he now uses instead of hand-rolling SSR.
[[nodejs]] — the backend half of the one-language stack.
[[material-ui]] — the React component library under his grid builders.
[[react-admin]] — declarative admin building in the React ecosystem.
[[declarative-ui]] — the paradigm React mainstreamed.
