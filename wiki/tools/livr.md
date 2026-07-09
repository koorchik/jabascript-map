---
type: tool
tags: [validation, javascript, webbylab, open-source]
---
# LIVR

LIVR (Language Independent Validation Rules) is Viktor's own validation library — born at WebbyLab, which standardizes its stacks: they tried every validation library, wrote a specification first, and only then implementations, so the same rule format now exists in JS, PHP, Perl, Go, Swift and Erlang ([[google-io-2023-watch-party]]). The design pitch, laid out in a LIVR-vs-Zod deep dive from his design doc ([[vibe-coding-part-2]]): rules are pure data — serializable, so LIVR rules could be compiled to Zod but not vice versa — with DDD-style rule aliasing (a `valid_price` rule with custom error codes) and a deliberate no-code-generation stance as a security position. On performance, warm-path numbers are comparable (Zod ~4M ops/s vs LIVR ~3.4M), but Zod is ~94x slower when rules are constructed dynamically.

In the vibe-coding streams LIVR is also a lens on working with AI: he wants validation rules to drive TypeScript type inference — runtime and static validation from one schema in the same module — but Claude kept duplicating types instead, a correction he had to explicitly teach ([[vibe-coding-new-project]]).

## Covered in
- [[vibe-coding-part-2]] — the LIVR-vs-Zod deep dive: rules as pure data, rule aliasing, no codegen, and the dynamic-rules benchmark (~94x gap).
- [[vibe-coding-new-project]] — validation-driven TypeScript inference as a design goal Claude had to be taught.
- [[google-io-2023-watch-party]] — origin story: spec-first library design at WebbyLab, one rule format across six languages, contrasted with Google's monorepo where no library choice exists.

## Related
[[software-design]] — spec-first, data-as-rules design philosophy.
[[abstractions]] — rule aliasing as a domain-level abstraction over raw validators.
[[vibe-coding]] — the streams where LIVR meets AI-generated code.
[[security-practices]] — refusing code generation as a security stance.
