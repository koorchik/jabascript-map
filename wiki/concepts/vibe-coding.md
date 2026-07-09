---
type: concept
tags: [ai, vibe-coding, workflow, llm, software-design]
---
# Vibe-coding

Vibe-coding, as Viktor practices it live on the channel, is not "close your eyes and accept whatever the model outputs" — it is a disciplined, standards-driven workflow where the human stays the architect and the AI does the typing. His full pipeline, demonstrated from an empty folder in the racing-telemetry livestream ([[vibe-coding-new-project]]): brainstorm the app idea with [[gemini|Gemini]] and write per-screen descriptions, generate the UI screens in [[google-stitch|Google Stitch]] (iterating screen by screen, picking winners from variations), paste the descriptions into the repo, and then drive [[claude-code|Claude Code]] in plan mode — reading and correcting *every* plan before letting it run. The central trick is encoding project standards in `CLAUDE.md` instead of repeating them in prompts: every time the AI does something wrong, the correction goes into `CLAUDE.md`, not just into the chat. He runs several Claude instances in parallel and reviews diffs after non-stop runs; with Opus 4.5 he found "ultrathink" no longer necessary, and skills only worth writing for genuinely reusable procedures.

The thesis he keeps returning to in [[vibe-coding-part-2]]: **the better structured the project, the better AI works**. Iterate corrections into `CLAUDE.md` for a few weeks and every new feature "just lands". The flip side is that setting up the infrastructure — the decision-heavy part — is exactly what AI (like juniors) can't do, which is why he plans an opinionated boilerplate (a refresh of his chista/chista-express) that ships *with* a `CLAUDE.md` and skills, so "the AI already knows how to work with it" from the first prompt. Vibe-coding in his framing is therefore continuous with the channel's older themes: [[software-design]], [[abstractions]], [[code-quality]] and standards matter *more* in the AI era, not less, because they are the leverage that turns a fast-but-sloppy junior into a productive team.

He also shows vibe-coding is past the toy stage: Blackmagic ships a REST API but no app for his screen-less Micro Studio Camera, so he vibe-coded a full-featured [[flutter|Flutter]] controller app in two evenings ([[vibe-coded-mobile-app]]). His takeaway is economic — vibe-coding makes "write your own vendor app" a sane weekend project rather than a months-long commitment.

## Covered in
- [[vibe-coding-new-project]] — the full workflow live from an empty folder: Gemini brainstorm → Stitch screens → CLAUDE.md-encoded standards → plan mode → parallel Claude instances → diff review.
- [[vibe-coding-part-2]] — the "structure feeds the AI" thesis, iterating corrections into CLAUDE.md, why infrastructure setup stays human, and the plan for an AI-ready opinionated boilerplate.
- [[vibe-coded-mobile-app]] — concrete non-toy proof: a complete Blackmagic camera controller app vibe-coded in two evenings against the camera's REST API.

## Related
[[ai-coding-agents]] — the tooling and agent mechanics underneath the workflow.
[[ai-and-jobs]] — the AI-as-junior scaling analogy that justifies investing in standards.
[[software-design]] — clean architecture taught live during the vibe-coding streams.
[[code-quality]] — standards in CLAUDE.md are the AI-era version of style guides.
[[automated-testing]] — you design the tests, the LLM writes them.
[[code-review]] — reviewing AI diffs replaces reviewing junior PRs.
