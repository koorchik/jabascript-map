---
type: concept
tags: [engineering-craft, testing, ai]
---
# Automated testing

The channel's testing strategy is laid out most concretely in the AI-era context of the vibe-coding streams ([[vibe-coding-part-2]]). Structure: unit tests live next to the files they test, integration/API tests live separately. For parallel DB tests he uses one container holding 10–20 databases mapped to test-worker IDs, so workers never collide. The economics have shifted: tests are now cheap because AI writes them — and the dependency runs both ways, since the AI *needs* tests plus TypeScript as its feedback loop to check its own work.

On frontend tests his answer is a firm "it depends," backed by two extremes he's seen first-hand: in Google's monorepo they're mandatory, because shared Angular code updates under you and only tests catch the breakage; meanwhile Instagram shipped its React web app with zero frontend tests ([[vibe-coding-part-2]]). His broader testing philosophy — tests after code, minimal mocking, design for injectable implementations — lives under [[test-driven-development]], where he argues against the purist loop.

## Covered in
- [[vibe-coding-part-2]] — test layout, parallel DB-container trick, tests as the AI's feedback loop, Google-vs-Instagram frontend-testing extremes

## Related
[[test-driven-development]] — the ritual he rejects while embracing tests themselves
[[vibe-coding]] — tests and types as the safety net for AI-written code
[[ai-coding-agents]] — the agent needs a feedback loop to self-correct
[[code-quality]] — tests as one guardrail among several
