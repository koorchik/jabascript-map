---
type: tool
tags: [ai, llm, local-models, privacy]
---
# Ollama

A runner for open-source LLMs on local hardware. Viktor's use case is privacy, not cost: he runs local models through Ollama with an editor plugin specifically so private code never reaches public servers ([[qa-2-answering-questions]]) — his 3090-equipped desktop ([[my-workspace-setup]]) makes this practical. He has a full comparison report of local models he may publish; the spoilers so far are unflattering — local [[deepseek|DeepSeek]] R1 distills up to 70B fail his binary-search-in-file benchmark, and small models (≤14B) driven through Cline as agents were "trash" ([[vibe-coding-part-2]]).

## Covered in
- [[qa-2-answering-questions]] — local models via Ollama to keep private code local; unpublished comparison report.

## Related
[[ai-coding-agents]], [[deepseek]], [[claude-code]], [[workspace-and-hardware]]
