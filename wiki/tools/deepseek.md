---
type: tool
tags: [ai, llm, open-source, local-models]
---
# DeepSeek

The Chinese open-weights LLM family, which the channel treats as a data point on the local-vs-frontier gap. Against Viktor's binary-search-in-file benchmark ([[qa-2-answering-questions]]): local R1 distills up to 70B fail even with reasoning enabled, while the full ~700B online version does solve it — but thinks for a long time. The takeaway matches his broader local-model verdict via [[ollama|Ollama]]: distills are not the full model, and as of that Q&A the models you can self-host don't clear the bar frontier models clear casually.

## Covered in
- [[qa-2-answering-questions]] — R1 distills ≤70B fail the benchmark; the full ~700B version passes slowly.

## Related
[[ai-coding-agents]], [[ollama]], [[chatgpt]], [[gemini]]
