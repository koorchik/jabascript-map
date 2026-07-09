---
type: concept
tags: [engineering-craft, code-quality]
---
# Code quality

Viktor challenges the classic "fast / quality / cheap — pick two" triangle: maybe you can have all three, because quality code is *cheaper and faster* to develop, not a luxury you trade speed for ([[3-things-that-ruin-a-programmer]]). His definition is pointedly non-perfectionist: quality is code that doesn't stop you from extending it — abstractions that keep working as the system grows, code you never have to throw away. And his most personal argument is that bad code hurts *you*, not just the project: writing crappy code destroys the "code smell" intuition that lets seniors spot problems before they've even read the code. The habit caps your own growth.

The subtle enemy is consistency with a stale structure: codebase rot happens even while every individual change looks perfectly consistent with the surrounding code — that's exactly how God Objects and 5000-line files grow ([[voice-3-scary-abstractions]]). Quality, in the channel's telling, is therefore less about polishing lines and more about noticing when the structure itself has expired — which connects it to [[technical-debt]] and to review formats that look beyond the diff ([[code-review]]).

## Covered in
- [[3-things-that-ruin-a-programmer]] — the fast/quality/cheap challenge, quality as extensibility, bad code destroying your smell intuition
- [[voice-3-scary-abstractions]] — rot through consistency: every change looks fine, the file hits 5000 lines

## Related
[[abstractions]] — quality = abstractions that survive extension
[[technical-debt]] — what accumulates when quality is only judged per-diff
[[code-review]] — automating style, catching what diffs can't show
[[career-and-growth]] — crappy code damages the programmer, not just the codebase
[[clean-code]], [[code-complete]] — the craft bookshelf
