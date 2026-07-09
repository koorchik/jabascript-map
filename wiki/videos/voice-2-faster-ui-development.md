---
type: video
title_uk: "Голосове №2 - як швидше розробляти інтерфейс"
youtube_id: fzJngfQ9lWo
tags: [frontend, ui, abstractions, declarative, voice-message]
date_ingested: 2026-07-09
---
# Voice Message #2 — How to Develop UI Faster

> Original: "Голосове №2 - як швидше розробляти інтерфейс" — https://youtu.be/fzJngfQ9lWo

Second voice-message episode (he renamed the podcast from "5 minutes about programming" because he literally records these as voice messages on his iPhone). One idea for speeding up frontend work: borrow the **game level editor** concept. Games separate the engine from content — Doom was built with a level editor from day one (edit level → relaunch → look → repeat), and the editor implies a *declarative saved description* of the level. His thesis: [[declarative-ui|declarative UI builders]] — schemas compiled into low-level components — are worth building not only as cross-project tools but **even inside a single project**, where he claims they dramatically cheapen development and keep the UI consistent ([[abstractions]]).

## Key takeaways
- Ready-made declarative admin tools ([[react-admin]] and the like) let you assemble list/CRUD/grid/gallery screens fast — but they're standardized and don't fit every project or company. webilab invested in its own cross-project admin-building tool; that pays off across many projects but requires serious investment.
- His newer realization: the same builder approach makes sense **within one project**. It looks like a stupidly expensive move, but a project-specific framework is much cheaper than a cross-project one — and you'd have to write those screens anyway.
- Concrete example from a recent project: React [[material-ui|Material]] grid is powerful but quite low-level, so he wrote his own **grid builder** that takes a schema; from ~2 of his parameters it initializes ~5 low-level ones. Result: a grid he configures easily on any page, behaves consistently, persists its settings where he wants, is compatible with his API, supports per-row custom actions via an extra schema, shows delete confirmations, and integrates with navigation — all things you'd otherwise hand-write per page.
- On top of that: a **form builder** (forms in dialogs or on pages, callable from the grid or anywhere), and above everything a **PageBuilder** that produces an entire CRUD page from one schema. For more custom pages he drops down a level and uses just the grid builder or form builder — the layers stay useful individually.
- The key advantage of project-specific (vs cross-project) builders: when a new feature arrives, he just extends the schema that same day with the missing elements. The whole UI stays consistent everywhere, which "strongly, strongly cheapens" development and maintenance.
- He's puzzled the approach isn't more popular: people take a forms library and use it raw on every screen, even though every project has custom bits — e.g. your API returns errors in a specific format that must be handled and bound to fields — and one more declarative layer over the library would encode that once ([[software-design]]).
- Usual caveat for the series: these are ideas and reflections, not the one true way — "maybe it won't fly on your project, and maybe on some of mine it won't either."

## Covered
[[declarative-ui]], [[abstractions]], [[software-design]], [[react-admin]], [[material-ui]]
