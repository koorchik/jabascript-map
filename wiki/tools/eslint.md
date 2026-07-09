---
type: tool
tags: [javascript, linting, code-quality, tooling]
---
# ESLint

ESLint is the standard JavaScript linter. The channel's advice, drawn from review practice at both WebbyLab and Google ([[code-review-how-google-does-it]]): use ESLint with every plugin available, each rule tuned to your style guide, so that machines catch what machines can catch and human review time goes to design and correctness. WebbyLab took this to its logical end — they published their own `eslint-plugin-more` on npm and kept adding rules for problems that showed up repeatedly in code reviews, turning recurring review comments into automated checks.

## Covered in
- [[code-review-how-google-does-it]] — max out ESLint plugins tuned to your style guide; WebbyLab's eslint-plugin-more grew from recurring review findings.

## Related
[[prettier]] — the formatting half of "automate style away".
[[code-review]] — linting exists to free human reviewers for real issues.
[[code-quality]] — encoded standards instead of tribal knowledge.
