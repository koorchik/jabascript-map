---
type: concept
tags: [engineering-craft, software-design, abstractions]
---
# Abstractions

Designing abstractions is the third of the three skills that, per the channel's first video, turn a good coder into a great programmer — with coupling and cohesion as its two core aspects ([[3-things-that-make-a-programmer-better]]); quality code, in turn, is defined as abstractions that keep working as you extend them, code you never have to throw away ([[3-things-that-ruin-a-programmer]]). His practical test for a boundary: business logic must not know the web framework — if the same service classes could power a CLI or a Telegram bot (he shows his 7-year-old Perl 6 golf bot built on exactly that pattern), the abstraction is right ([[vibe-coding-new-project]]). He considers design skill essentially synonymous with skill at abstractions — it's what determines your level at Google, and why he calls Go "absolutely not okay" for business-logic-heavy systems like accounting: the language lacks abstraction constructs, fine for microservices, proxies and CLI tools, while he reaches for TypeScript/C# for complex apps ([[qa-and-plans-for-2024]], [[qa-2-answering-questions]]).

His most original observation — he made a DOU Day slide of it — is that less-experienced developers *fear creating new abstractions*: they reuse or copy existing structures and almost never extract new ones. Not fear of new files (devs create files constantly), but the extra thinking a new abstraction demands, plus not yet seeing the consequences ([[voice-3-scary-abstractions]]). The war stories: `assertDate` bolted onto WebbyLab's TestFactory because the factory was "already everywhere"; base service classes accumulating date/file/session utils into a God Object; his ~100-line widget PoC grown into one 5000-line file ("that's how YOU showed us"); a React team uncomfortable adding a controller concept because nobody there had done it — while at Google his UI controllers over low-level pieces "wonderfully" simplified the code. The inverse failure exists too: AI over-engineers, inventing brand-manager class hierarchies with `registerNewBrand()` where a JSON file of car brands would do — he constantly commands "delete this abstraction" ([[vibe-coding-part-2]]). And the constructive direction: project-specific declarative builders (grid, form, PageBuilder) as deliberate extra layers that massively cheapen UI work ([[voice-2-faster-ui-development]], see [[declarative-ui]]).

## Covered in
- [[voice-3-scary-abstractions]] — the core video: why devs stuff code into existing structures instead of extracting new abstractions, four war stories
- [[3-things-that-make-a-programmer-better]] — designing abstractions as one of the three great-programmer skills; coupling and cohesion
- [[3-things-that-ruin-a-programmer]] — quality = abstractions that survive extension
- [[vibe-coding-new-project]] — the swap test: services that could power a CLI/Telegram bot; layering as the boundary
- [[vibe-coding-part-2]] — the opposite failure: AI's needless abstraction hierarchies, "delete this abstraction"
- [[microservices-main-problem]] — wrong abstractions are cheap to fix in a monolith, brutal across services
- [[voice-2-faster-ui-development]] — builders as productive extra abstraction layers, with a drop-down-a-layer escape hatch
- [[qa-2-answering-questions]] — Go's missing abstraction tools; extending architecture patterns (own controller concept) when they stop fitting
- [[qa-and-plans-for-2024]] — design skill = skill with abstractions; Go verdict for business-logic-heavy systems

## Related
[[software-design]] — abstraction design is the heart of it
[[declarative-ui]] — his favorite constructive abstraction: schema-driven UI builders
[[code-quality]] — rot happens when structure stops matching responsibilities
[[technical-debt]] — un-extracted abstractions compound into debt
[[design-patterns]] — patterns as named, pre-classified abstractions
[[a-philosophy-of-software-design]] — the book he quotes on design attention
