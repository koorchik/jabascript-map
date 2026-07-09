---
type: concept
tags: [engineering-craft, testing, tdd]
---
# Test-driven development

The channel is explicitly anti-TDD-purist. Viktor likes tests but dislikes Kent Beck's red/green loop as a design tool: it suits bug fixes, but for design it narrows your focus onto the next assertion instead of the shape of the API ([[3-things-that-make-a-programmer-better]], [[qa-2-answering-questions]]). His alternative is API-first sketching — write example usage code, rewrite until a skeleton emerges, implement, and write the tests *after* the code. He backs the position with sources: the "Is TDD Dead?" conversation series (Beck/Fowler/DHH) and *A Philosophy of Software Design*'s argument that TDD misdirects attention ([[qa-2-answering-questions]]).

His favorite illustration of TDD dogma is the mocking cargo cult: people decided that TDD = unit tests = mock everything, yet in those same "Is TDD Dead?" talks Kent Beck himself says he mocks as little as possible — "people just decided it must be that way" ([[3-things-that-ruin-a-programmer]]). Viktor's own line is classicist: instead of mocking, design for injectable implementations. The whole topic is his case study of dogmatism — believing in programming instead of understanding it.

## Covered in
- [[3-things-that-ruin-a-programmer]] — the mock-everything dogma vs what Beck actually says
- [[3-things-that-make-a-programmer-better]] — likes tests, dislikes the red/green loop; API-first instead
- [[qa-2-answering-questions]] — the full position: "Is TDD Dead?" series, *A Philosophy of Software Design* quote, tests after code, classicist mocks

## Related
[[automated-testing]] — he's pro-tests, anti-ritual
[[software-design]] — the API-first method TDD is rejected in favor of
[[deep-learning-of-fundamentals]] — understand practices' reasons instead of believing them
[[a-philosophy-of-software-design]] — his cited authority against TDD-as-design
