---
type: concept
tags: [engineering-craft, code-review, process, google]
---
# Code review

The channel's take is first-hand: Viktor draws on review practice at both WebbyLab and Google and insists there is no single right way — but there are moves that make any review better ([[code-review-how-google-does-it]]). Standardize your guidelines (when two approaches are both fine, just pick one so reviews stop relitigating taste) and automate style away entirely, so senior time is never spent on formatting comments. Google's system he describes from the inside: peer review where a junior can review a senior, plus a separate per-language "readability" certification (~6 months to earn for TypeScript, years for C++) — code cannot merge without approval from a readability holder, so on his team a junior with readability approved his code while his own approval alone was insufficient. The author's side matters just as much: one concern per MR, real descriptions, before/after screenshots and screencasts — make the review effortless for the reviewer.

His sharpest point is that per-PR review alone is never enough: every diff can look great while the architecture quietly stops working — which is why Google also runs post-launch reviews where the feature author walks the team through the merged code, and WebbyLab runs periodic architectural reviews (see [[technical-debt]] and [[software-design]]). In the AI era the practice extends to machine output: AI-written code must be read line by line like a human PR — he watches Claude's edits stream in the terminal and hits Escape the moment it goes wrong, or reviews the full diff for big one-shot changes — and notes that AI already reviews more PRs than it writes, with a human still reviewing what's left ([[vibe-coding-part-2]]).

## Covered in
- [[code-review-how-google-does-it]] — the core video: automate style, standardize guidelines, Google's peer review + readability certification, author-side etiquette, post-launch reviews
- [[vibe-coding-part-2]] — reviewing AI output like a human PR: streaming-diff supervision, Escape-key interventions, AI as reviewer

## Related
[[technical-debt]] — the failure mode per-PR review can't see: every diff looks fine, the architecture rots
[[code-quality]] — what review is ultimately protecting
[[software-design]] — WebbyLab's periodic architectural review complements per-PR review
[[vibe-coding]] — supervising AI-generated code is review work
[[software-engineering-at-google]] — the book behind much of Google's process
