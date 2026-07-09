---
type: overview
tags: [synthesis]
---
# jabascript — The Knowledge Map

**jabascript** is Viktor's Ukrainian-language YouTube channel (~19k subscribers as
of early 2024), built as an *evergreen knowledge base for engineers* — designed to
be watchable oldest-first without going stale. This wiki compiles all 40 ingested
videos into an interlinked map. Start here, drill into a [[networking-and-internet|cluster]],
or jump straight to a concept.

## The one thesis that runs through everything

**[[deep-learning-of-fundamentals|Learn things deeply]]** is the channel's spine.
Almost every video is an instance of it:

- Understanding *internals* gives you a system's **properties** — marketing
  materials never will ([[database-indexes]], [[uuid-vs-auto-increment]],
  [[awd-and-drivetrains|even car drivetrains]]).
- Knowledge sticks only when hooked onto a **knowledge tree** of fundamentals —
  leaves (details) fall off; branches let you re-learn fast
  ([[learning-deeply-and-remembering]]).
- "Almost all of information security is understanding how things work inside" —
  the stated reason the channel does protocol deep-dives
  ([[security-and-cryptography]]).
- With AI, fundamentals matter *more*, not less: you can't correct what you
  can't evaluate ([[vibe-coding]], [[ai-coding-agents]]).

## The six territories

| Cluster | What lives there |
|---|---|
| [[networking-and-internet]] | The "How the Internet works" series: [[latency-and-speed-of-light]] → [[dns]] (3 parts) → [[dhcp]]; plus [[https-tls]], [[remote-development]] |
| [[databases-and-data-structures]] | The densest learning path: [[algorithmic-complexity]] → [[b-tree|trees]] → [[database-indexes]] → [[full-text-search]]/[[inverted-index]] → [[bloom-filter]] |
| [[security-and-cryptography]] | The [[hashing]]/[[encoding]]/[[encryption]] taxonomy, [[asymmetric-encryption]] and [[digital-signatures]], attack stories ([[social-engineering]], rogue [[dhcp|DHCP]]) |
| [[ai-and-vibe-coding]] | From Gemini comedy stress-tests to full [[vibe-coding]] livestreams with [[claude-code]]; the [[ai-and-jobs|AI-as-junior]] position |
| [[engineering-craft-and-career]] | The opinion core: [[software-design]], [[abstractions]], [[code-review]] (Google's process first-hand), [[microservices]] skepticism, [[career-and-growth]] with real Google comp numbers, and the book canon |
| [[channel-meta]] | Q&A streams, voice-message war stories, [[channel-and-author|who Viktor is]] and why he joined — and left — Google |

## Signature material (the things only this channel gives you)

- **First-hand Google mechanics**: readability certification in [[code-review]],
  comp/stock-cliff arithmetic and promo-committee mechanics in
  [[career-and-growth]] and [[voice-5-why-i-left-google]].
- **A 300 TB hand-rolled full-text search** war story grounding the
  [[inverted-index]] and [[index-compression]] pages.
- **Real benchmarks with numbers**: 60,000× index speedup, UUID-PK bloat
  measurements, Bloom filter vs Redis/MySQL/Map ladders, Kyiv→LA latency stacks.
- **The WebbyLab practice**: architectural reviews beyond per-PR
  [[code-review]], [[declarative-ui]] builders, [[livr]], the
  [[least-privilege|admin-key disaster]].
- **A complete [[five-star-books|book canon]]** with personal verdicts — the
  [[software-design]] set (Evans, Fowler, Martin, Ousterhout) most of all.

## How to use this wiki

Ask questions against it; answers worth keeping get filed back as new pages.
The catalog lives in [[index]]; the ingest history in [[log]]. Conventions and
workflows are in `CLAUDE.md` at the repo root.
