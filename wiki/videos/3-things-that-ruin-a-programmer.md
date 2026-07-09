---
type: video
title_uk: "3 речі, що псують програміста"
youtube_id: _j8ACibMJ0s
tags: [career, code-quality, dogmatism, teamwork]
date_ingested: 2026-07-09
---
# 3 Things That Ruin a Programmer

> Original: "3 речі, що псують програміста" — https://youtu.be/_j8ACibMJ0s

Companion to [[3-things-that-make-a-programmer-better]]: three things that turn a good programmer into a worse one. They may sound banal, but his angle is unusual — he explains why each one damages *you personally*, not just the project: (1) writing crappy code destroys the "code smell" intuition you need to become a senior; (2) **dogmatism** — believing in programming instead of understanding it; (3) a dismissive attitude toward colleagues, which caps your growth and your impact ([[career-and-growth]], [[code-quality]]).

## Key takeaways
- **Everyone accepts the "fast / quality / cheap — pick two" triangle axiomatically, but he questions it**: maybe you *can* have all three — quality code is often both cheaper and faster to develop (scale-dependent; separate video promised).
- **Why bad code hurts the programmer, not just the business**: senior developers have an intuition — they open unfamiliar code and, before really reading it, ask the right questions and predict where the problems are, just from seeing the abstractions. That "code smell" nose is built over years of writing good code. If you keep writing garbage, you stop smelling it and never develop the intuition that makes a higher-level developer ([[code-quality]], [[career-and-growth]]).
- His definition of quality here is explicitly *not* perfectionism or load-proof, fully-tested code: quality code is code that **doesn't stop you from extending it** — you write a little now, add more later, add tests, and the [[abstractions]] keep working instead of having to be thrown away.
- **Dogmatism examples he collected**: a Ukrainian frontend chat claimed "using props in `getInitialState` is an antipattern" as an absolute — the React docs said it's an antipattern *under certain conditions*, and the reasons, not the syntax, are what matter ([[deep-learning-of-fundamentals]]).
- The [[test-driven-development|TDD]] mock dogma: people decided TDD means unit tests and unit tests mean mocking everything in isolation. He points to the "Is TDD Dead?" conversations (Kent Beck, Martin Fowler, DHH — link under the video), where Kent Beck — who basically invented TDD and wrote the book — says he almost never mocks and mocks as little as possible. "People just decided it must be that way."
- Same story with Greg Young and event sourcing: Young himself says he showed *an example* at a conference and everyone canonized it as *the* way — events don't have to be handled exactly like that (he also notes Redux is a related idea). And design patterns (GoF, Fowler): a pattern is not sacred knowledge — it's a classified name for something that worked for many people; the point is the problem it solves, not the reference implementation. Best practices exist to stop you writing *terribly bad* code, not to produce the best code — if you understand the reasons behind a practice, you may deliberately break it ([[software-design]]).
- His formula for the whole disease: **people read something and believe it instead of understanding it — faith in programming instead of understanding of programming**. Weigh everything (including his own videos) against your own experience.
- **Contempt for colleagues** kicks in exactly when you start feeling like a hot-shot: always be ready to hear out less-experienced colleagues — they often propose a better solution than yours. A brilliant lone-wolf who helps the people around him produces far more than he ever could alone, and that leadership unlocks bigger projects. At Google (where he works) this is a core value — people are extremely qualified yet always open to your opinion, and in such a team "you can build things you could never build alone."

## Covered
[[code-quality]], [[career-and-growth]], [[deep-learning-of-fundamentals]], [[software-design]], [[abstractions]], [[test-driven-development]]
