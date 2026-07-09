---
type: concept
tags: [engineering-craft, architecture, maintenance]
---
# Technical debt

The framing that stuck with Viktor is a quote he passes on: **"if you just write code, you accumulate technical debt"** ([[code-review-how-google-does-it]]). His example: a system was designed for 10 modules and now has 300. Every new module is written exactly like the previous ones, reviewed like the previous ones, and looks great in the diff — yet the architecture as a whole no longer works. That is the essence of the channel's view: debt is not sloppy code slipping past review; it is *consistent* code accumulating against a design that has silently expired, which makes it invisible to pre-submit [[code-review]].

The same mechanism shows up in his abstraction war stories: a ~100-line proof-of-concept widget grows into one 5000-line file precisely because every change stayed consistent with the surrounding structure — "that's how YOU showed us," the team told him ([[voice-3-scary-abstractions]]). The remedies he describes are structural, not diff-level: Google's post-launch walkthroughs of merged code and WebbyLab's periodic architectural reviews with checklists, a C4 diagram, and an action plan re-checked after ~2 months ([[code-review-how-google-does-it]]). Microservices make this debt uniquely expensive: a wrong boundary in a monolith is a cheap refactor, across services in different languages and teams it is incredibly hard to fix ([[microservices-main-problem]]).

## Covered in
- [[code-review-how-google-does-it]] — the "just writing code accumulates debt" thesis, the 10→300 modules example, and the review formats that catch architecture-level rot
- [[voice-3-scary-abstractions]] — how debt grows through consistency with a stale structure (the 5000-line file)
- [[microservices-main-problem]] — wrong service boundaries as the hardest-to-repay form of debt

## Related
[[code-review]] — per-PR review cannot see this class of debt; architectural review can
[[code-quality]] — quality as code that keeps letting you extend it
[[abstractions]] — failing to extract new abstractions as responsibilities grow is how debt compounds
[[microservices]] — distributed systems freeze bad decisions in place
