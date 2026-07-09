---
type: concept
tags: [ai, llm, coding-agents, tooling, benchmarks]
---
# AI coding agents

The channel's core claim about coding agents: **AI turns you into a tech lead from day one**. The LLM writes the code and the tests; you analyze requirements, design the tests, own the architecture — and the time it frees should be reinvested into project quality and standards ([[vibe-coding-new-project]]). Agents systematically over-do things, so the non-negotiable skill is being able to *correct* them, which presumes you understand what right looks like — the channel's long-standing [[deep-learning-of-fundamentals]] argument, now with an economic engine behind it. His practical playbook from [[vibe-coding-part-2]]: `/clear` before every task (he uses "clear context and accept edits" so the approved plan becomes a fresh prompt), run parallel Claude instances isolated via git worktrees (as recommended in Anthropic's docs), and feed documentation directly or via context7 when the model's knowledge is stale. Fun facts he drops along the way: [[claude-code|Claude Code]], Gemini CLI and Codex are all written in [[react|React]]; and Ukrainian prompts work fine — he explains why via word2vec/embeddings and the shared multilingual semantic space.

Viktor evaluates every model with one personal benchmark: **write a binary search in a file without loading it into memory**. It's small but unforgiving — Buffer arithmetic, seek offsets, edge cases. As of [[qa-2-answering-questions]]: latest [[chatgpt|ChatGPT]] and Gemini 2 pass; Grok and local [[deepseek|DeepSeek]] R1 distills up to 70B fail even with reasoning; the full ~700B DeepSeek passes but thinks a long time. The benchmark predates the agent era — back at Google I/O 2023 he ran the same style of test (a Node.js file-reading task with binary Buffer ops and mixed sync/async code) on Bard vs ChatGPT-4: GPT-4 nailed it, fixing what 3.5 had gotten wrong, while Bard flailed "like a junior who'd ping ChatGPT for help" — though he credited Bard for honestly admitting what data it could access ([[google-io-2023-watch-party]]). Local models run through [[ollama|Ollama]] (to keep private code off public servers) and via Cline at ≤14B he bluntly rated "trash".

His day-to-day stack is deliberately plural: [[gemini|Gemini]] (including Deep Research) as the most-used work LLM, o3-mini-high for brainstorming, a standing ChatGPT project with a system prompt encoding his React/TypeScript conventions so prototypes come out in his style, and Claude Code as the main agent. He skips autocomplete assistants like [[github-copilot|GitHub Copilot]] — the only one that ever convinced him was Google's internal equivalent, trained on Google's own codebase so it completes in Google style. His position on adoption is categorical: engineers who don't adopt AI lose competitiveness, and a beginner should register a ChatGPT/Bard account *before* installing an editor ([[qa-and-plans-for-2024]]). His everyday uses read like a man-page replacement: naming variables (five options, pick one), parsing binary formats, explaining Unix output, the ffmpeg palette trick that shrank a GIF ~100x, attaching a WebSocket server to an existing Express server via HTTP upgrade.

## Covered in
- [[vibe-coding-new-project]] — the tech-lead-from-day-one framing: the LLM writes tests, you design them and own architecture; agents over-do, so you must correct.
- [[vibe-coding-part-2]] — the practical playbook: /clear per task, parallel Claudes via git worktrees, feeding fresh docs, why Ukrainian prompts work, local-model verdicts.
- [[vibe-coded-mobile-app]] — two evenings of agent work covering an entire camera feature set: "what I liked is that I vibe-coded this".
- [[google-io-2023-watch-party]] — the original Bard-vs-GPT-4 hands-on benchmark, the "no moat" open-source memo, and Google's embed-LLMs-everywhere strategy.
- [[qa-2-answering-questions]] — the binary-search-in-file benchmark scoreboard and his full daily LLM stack, including Ollama for private code.
- [[qa-and-plans-for-2024]] — daily ChatGPT/Bard usage patterns and the adopt-or-lose-competitiveness position.

## Related
[[vibe-coding]] — the workflow these agents power.
[[ai-and-jobs]] — what agents mean for who gets hired.
[[deep-learning-of-fundamentals]] — why correcting an agent requires trunk-level knowledge.
[[remote-development]] — dev containers and terminals where his agents run.
[[test-driven-development]] — designing tests while the agent writes them.
