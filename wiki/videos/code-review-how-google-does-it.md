---
type: video
title_uk: "Як покращити Code Review? Як це робить Google?"
youtube_id: Xv92EsebyvU
tags: [code-review, google, engineering-process, architecture]
date_ingested: 2026-07-09
---
# How to Improve Code Review? How Google Does It

> Original: "Як покращити Code Review? Як це робить Google?" — https://youtu.be/Xv92EsebyvU

There is no single "right" way to do [[code-review]] — so he shares first-hand experience from two places: his company webilab and Google (where he works). He covers the classic pull-request review and how to unload it with automation, Google's peer-review + *readability* system, how to be a kind PR author, and then the part he thinks people underestimate: why per-PR review is **not enough**, and the periodic *architectural review* process webilab runs to catch the [[technical-debt]] that accumulates even when every individual PR looks great.

## Key takeaways
- Classic flow (branch → PR → senior reviews → merge) works, but only with **guidelines**: often two approaches are both correct and you should just standardize on one so the whole company's code reads uniformly. Once the reviewer starts writing "2 spaces here, 4 there", you've failed — **automate style away** with [[prettier]] and [[eslint]] with every plugin you can find, each tuned to your style guide. webilab even published its own plugin (`eslint-plugin-more` on npm) and kept adding rules for problems they saw repeatedly in reviews, so no senior ever has to comment on them again.
- **Who reviews?** Senior/team-lead review and peer review both work — it depends on whether you even have seniors free. At Google it's peer review: he can put *any* googler as reviewer, junior reviewing senior included.
- **Google's twist — the "readability" status**: besides an engineer who knows the feature saying LGTM, someone holding *readability* for that language must certify the code matches the style guides. Readability in TypeScript takes about half a year to earn; in C++ maybe years. In his team a junior developer has readability and can approve his code — while his own approval alone is never enough, since he doesn't hold the status. Both roles can be one person; teams switching language stacks get assigned an outside readability reviewer from anywhere in Google.
- Google backs this with a colossal amount of static analysis (per file type, built up over years) and a mono-repo so uniform that "you practically don't use Stack Overflow — you use code search", find good examples, and learn any library from real usage.
- **Be kind to your reviewer** — a mentality he says works great at Google: the reviewer has their own job, so make review effortless if you want it fast, thorough and repeatable. One merge request = one concern; describe it; and for any UI change attach a screenshot or a screencast, often annotated "was like this → became like this". Reviewers see the behavior instantly.
- The phrase that stuck with him from a book: **"if you just write code, you accumulate technical debt."** His example: a codebase designed for 10 modules now has 50 or 300; every new module is written and reviewed exactly like the previous ones, each piece looks great — yet the system no longer works as intended and none of it is visible in a pre-submit diff ([[technical-debt]]).
- webilab's answer: **periodic architectural review** (monthly or every few months). Checklists of the typical frontend, backend and [[security-practices|security]] mistakes (down to things like config handling or the *anemic domain model* antipattern); the reviewer works independently first — starting by launching the project, which must start with one command; the team self-audits against the same checklist; then a ~2-hour call where the team lead first draws a **C4 container diagram** (a notation you can learn in 5 minutes) of the processes/subsystems; output is a document and action plan; re-review after ~2 months ([[software-design]]).
- Post-launch review at Google: when something ships, the team gathers and whoever implemented a big feature walks everyone through the code and answers questions — after it's merged. His summary: don't *under*rate these other review types, and don't *over*rate the review you do on merge requests, because alone it's simply not enough.

## Covered
[[code-review]], [[technical-debt]], [[software-design]], [[security-practices]], [[eslint]], [[prettier]]
