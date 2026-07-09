---
type: tool
tags: [javascript, formatting, code-quality, tooling]
---
# Prettier

Prettier is the opinionated code formatter for JavaScript and friends. Its role in the channel's code-review doctrine is simple and absolute ([[code-review-how-google-does-it]]): Prettier plus linting should eliminate *all* style comments from human review — "automation to the maximum". If a reviewer is still commenting on formatting, the tooling has failed; human attention belongs on design, correctness and readability, not on where the braces go.

## Covered in
- [[code-review-how-google-does-it]] — Prettier + linting must remove every style comment from human review.

## Related
[[eslint]] — the semantic-rules companion in the same automation stack.
[[code-review]] — the process Prettier exists to declutter.
[[code-quality]] — style consistency as a machine problem, not a debate.
