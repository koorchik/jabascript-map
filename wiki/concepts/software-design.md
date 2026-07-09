---
type: concept
tags: [engineering-craft, software-design, architecture]
---
# Software design

Design is the channel's central craft topic — at Google, Viktor says, your level is determined by design ability, not tech knowledge (he'd never written Java or Angular before joining), and he ties that ability directly to working with [[abstractions]] and knowing things' properties from their internals: an index is a sorted structure, therefore writes cost something and only certain query shapes win ([[qa-and-plans-for-2024]]). His personal method is API-first: never start with the implementation — write example *usage* code first, rewrite it until a skeleton emerges, and only implement once the API shows single responsibility, minimal inputs, no leaked implementation details, and extensibility ([[3-things-that-make-a-programmer-better]], [[qa-2-answering-questions]]). He is openly anti-TDD-purist: the red/green loop suits bug fixes, but for design it narrows focus — he quotes *A Philosophy of Software Design* on TDD misdirecting attention, writes tests after the code, and takes the classicist line on mocks: design for injectable implementations instead ([[qa-2-answering-questions]]). Detailed design happens *while* coding, by tracing usage scenarios end to end; not foreseeing everything is normal — which is why he loves Robert C. Martin's idea that the architect's job is to **defer decisions**: good architecture maximizes the number of decisions not made, because domain understanding improves daily ([[microservices-main-problem]]).

The vibe-coding livestreams show the doctrine applied: clean architecture dictated to Claude — thin controllers as untestable glue is the goal (fat controllers and anemic domain models are antipatterns), one application service per endpoint with a single `run()`, validation inside the service, never leak domain entities (the password-hash example), because password hashing is a domain business policy; plus his "API for terrans" vs JSON:API "for zergs" joke and always-HTTP-200-with-status-flag responses like Facebook's API ([[vibe-coding-new-project]]). Design also rests on context the AI lacks: he *knows* there will be ~100–200 race tracks (cache forever, no pagination) but millions of telemetry points (never one entity per point) — with Figma's day-one Rust→WASM optimization and VS Code's Monaco rejecting all web frameworks (while Atom died of slowness) as evidence that some properties must be designed in from the start ([[vibe-coding-part-2]]). Depth is a design prerequisite: you need each subsystem's properties — what happens to the DB if data doubles, how its isolation behaves — to make the whole system meet its requirements ([[learning-deeply-and-remembering]]). Patterns and best practices aren't sacred: a pattern is just a classified name for what worked, best practices exist to prevent terrible code rather than produce the best code — understand the reasons and you may deliberately break them; he cites Greg Young's event-sourcing example being canonized against its author's intent ([[3-things-that-ruin-a-programmer]]). At WebbyLab the discipline is institutional: periodic architectural reviews with mistake checklists (anemic domain model included), a reviewer who must be able to launch the project with one command, a C4 container diagram to open the ~2h call, and an action plan re-reviewed after ~2 months ([[code-review-how-google-does-it]]). His book canon: [[clean-architecture]] for layers, [[domain-driven-design]] for the domain, [[patterns-of-enterprise-application-architecture]] for how the layers are actually implemented ([[3-books-on-software-design]], [[five-star-books]]).

## Covered in
- [[vibe-coding-new-project]] — clean architecture live: thin controllers, one service per endpoint, never leak entities, API design opinions
- [[vibe-coding-part-2]] — designing with context AI lacks (data cardinality), Figma/Monaco/Atom performance-by-design stories, input/result naming
- [[3-things-that-make-a-programmer-better]] — the API-first method: write usage examples before implementing
- [[3-things-that-ruin-a-programmer]] — patterns and best practices aren't sacred; understand the problem they solve
- [[learning-deeply-and-remembering]] — subsystem properties as a design prerequisite
- [[code-review-how-google-does-it]] — WebbyLab's periodic architectural review format
- [[microservices-main-problem]] — good architecture defers decisions
- [[voice-3-scary-abstractions]] — extract new abstractions as responsibilities grow; right at 100 lines, wrong at 5000
- [[voice-2-faster-ui-development]] — one more declarative layer as a design move, with the "maybe it won't fly on your project" caveat
- [[3-books-on-software-design]] — the three-book design canon: layering, domain, implementation patterns
- [[five-star-books]] — PoEAA over GoF as the pattern book; DDD via Evans and Vernon
- [[qa-2-answering-questions]] — anti-TDD-purism, classicist mocks, reinventing GoF patterns at Mail.ua
- [[qa-and-plans-for-2024]] — level = design skill; building abstractions by tracing usage scenarios

## Related
[[abstractions]] — design skill is skill with abstractions
[[domain-knowledge]] — the domain, not patterns, dictates architecture
[[deep-learning-of-fundamentals]] — internals give you the properties design decisions depend on
[[design-patterns]] — vocabulary, not gospel
[[test-driven-development]] — the loop he rejects as a design tool
[[microservices]] — an architecture that punishes early decisions
[[clean-architecture]], [[domain-driven-design]], [[patterns-of-enterprise-application-architecture]], [[a-philosophy-of-software-design]] — the design bookshelf
