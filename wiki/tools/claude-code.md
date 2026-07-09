---
type: tool
tags: [ai, coding-agent, cli, anthropic]
---
# Claude Code

Anthropic's terminal-based AI coding agent — and the main agent in Viktor's [[vibe-coding]] workflow. In [[vibe-coding-new-project]] he runs Opus 4.5 on the ~$100–120/month Max plan and calls it "dramatically better at design, less token-hungry" than before (enough that he stopped bothering with "ultrathink"). His setup is deliberately vanilla: the plain CLI plus a constantly updated `CLAUDE.md`, no plugins and no skills except for genuinely reusable procedures. Workflow staples: `/init` on a new repo, plan mode with every plan read and corrected before execution, multiple parallel instances launched from a Quake-style drop-down terminal inside dev containers, commit first and review diffs after non-stop runs.

He explicitly prefers the CLI over any IDE plugin ([[vibe-coding-part-2]]): it launches anywhere, runs many instances in parallel (isolated via git worktrees, per Anthropic's own docs), and the VS Code plugin just talks to the CLI anyway — the same reason he rejected [[cursor|Cursor]] and Google's Antigravity. He hit rate limits many times on the $100 plan, but they reset within hours — "good enough". Trivia he enjoys: Claude Code, Gemini CLI and Codex are all written in [[react|React]]. Before the agent, he had already tested Claude 3.5 Sonnet for extracting data for his dissertation ([[qa-2-answering-questions]]).

## Covered in
- [[vibe-coding-new-project]] — full live setup: Opus 4.5 on Max, /init, plan mode, parallel instances, CLAUDE.md as the standards store.
- [[vibe-coding-part-2]] — CLI-over-IDE argument, git worktrees for parallelism, /clear per task, rate-limit experience.
- [[qa-2-answering-questions]] — earlier Claude 3.5 Sonnet use for dissertation data extraction.

## Related
[[vibe-coding]], [[ai-coding-agents]], [[gemini]], [[cursor]], [[remote-development]]
