---
type: video
title_uk: "Вайб-коджу новий крутий проект"
youtube_id: BtHQyH6mniQ
tags: [vibe-coding, ai, claude-code, clean-architecture, backend, livestream]
date_ingested: 2026-07-09
---
# Vibe-coding a New Cool Project (livestream)

> Original: "Вайб-коджу новий крутий проект" — https://youtu.be/BtHQyH6mniQ

Live stream where the author starts a brand-new pet project — a racing telemetry app — from an empty folder, using [[claude-code|Claude Code]] (Opus 4.5 on the ~$100–120/month Max plan) as the main coding agent. He first shows off the previously vibe-coded [[flutter|Flutter]] app for his Blackmagic camera (native builds fly, the web build was "super slow" in debug until Claude optimized state handling), then walks through his real workflow: brainstorm the app with [[gemini|Gemini]], generate screen designs iteratively in [[google-stitch|Google Stitch]] (free, more creative than Figma's AI, needs a VPN from Ukraine), paste the whole description into the repo, and write instructions into `CLAUDE.md` instead of repeating prompts. The bulk of the stream is him dictating his backend philosophy to Claude: clean architecture ([[software-design]] à la Robert Martin's 2012 post — he argues "vertical slice architecture" is nothing new), thin controllers as glue, one application service per endpoint with a single `run()` method, validation inside the service (the real boundary), never leaking domain entities out of controllers, and always returning HTTP 200 with a `status: 0/1` payload "like Facebook's API". He plans the work in Claude's plan mode, reads every plan line by line, corrects it ("routing in one file", "use type inference from validation rules"), and runs several Claude instances in parallel from a Quake-style drop-down terminal inside dev containers.

## Key takeaways
- **His vibe-coding loop:** empty repo → `CLAUDE.md` with project guidelines (updated constantly) → `/init` → plan mode → read and correct the whole plan → let Claude run non-stop on a committed git state and review the diffs afterward. "Skills" in Claude Code only made sense to him for reuse; he stays "vanilla + a constantly updated CLAUDE.md". The old `ultrathink` trick is no longer needed on Opus 4.5, which he finds dramatically better at design and less token-hungry.
- **Architecture is the human's job:** business logic must not know about the web framework; controllers are hard-to-test glue that should be maximally thin (fat controllers and anemic domain models are antipatterns he calls out). Mental test: if the same services could power a CLI or a Telegram bot (he shows his 7-year-old Perl 6 golf bot with the same service-class pattern), the layering is right.
- **Validation lives in the service, not the controller** — the controller only checks that JSON parses. Same rules serve runtime and static typing via [[livr|LIVR]]-style type inference; duplicating validation per transport (HTTP, CLI, GraphQL) is the smell.
- **Don't return domain objects:** services dump only explicitly public fields — otherwise one day you leak a user's password hash. Password hashing itself is a domain-model business policy, not use-case code (a mistake Claude made that he corrects on stream).
- **His "API for terrans":** he found JSON:API so low-level and inhuman he dubbed it "an API for zergs" (StarCraft joke) and wrote his own simpler JSON response spec, which he feeds Claude along with his `chista` / `chista-express` npm modules as reference implementations.
- **With AI agents you become a tech lead from day one** ([[ai-coding-agents]], [[career-and-growth]]): the LLM writes the tests, you design them; your scarce skill shifts to architecture, requirements analysis and reading code. But [[deep-learning-of-fundamentals|deep fundamentals]] matter more, not less — he picked Flutter over React Native *because* he understands Flutter compiles natively while RN shuttles messages over a JS bridge, which matters for real-time telemetry math; without that understanding you can't correct the AI, "and it does so much that's wrong".
- **Life update:** he quit Google because he couldn't fit everything in — volunteering (the war), a PhD dissertation on extracting sensitive data from large text corpora with LLMs, and YouTube; he won't job-hunt until the dissertation is written. A Rust aside: he once reimplemented a JS benchmark in Rust→WASM and got only 2× speedup — not worth switching for.
- **Books he's currently enjoying (audio):** [[essentialism|Essentialism]] and [[effortless|Effortless]] by Greg McKeown, and [[atomic-habits|Atomic Habits]] — he expected nothing new from the latter and is "in delight".

## Covered
[[vibe-coding]], [[ai-coding-agents]], [[software-design]], [[abstractions]], [[deep-learning-of-fundamentals]], [[career-and-growth]], [[claude-code]], [[gemini]], [[google-stitch]], [[flutter]], [[vs-code]], [[livr]], [[essentialism]], [[effortless]], [[atomic-habits]]
