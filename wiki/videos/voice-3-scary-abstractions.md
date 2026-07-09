---
type: video
title_uk: "Голосове №3 - страшні абстракції"
youtube_id: qVWi-o6Gkj0
tags: [abstractions, software-design, voice-message, war-stories]
date_ingested: 2026-07-09
---
# Voice Message #3 — Scary Abstractions

> Original: "Голосове №3 - страшні абстракції" — https://youtu.be/qVWi-o6Gkj0

Third episode of the voice-message series, about a strange phenomenon he keeps observing (he even made a slide about it for his DOU Day talk but ran out of time): **developers are afraid to create new [[abstractions]]**. Less-experienced developers work by template — they either stuff new content into existing files/classes or copy files with an existing structure; genuinely *new* abstractions appear very rarely. He argues it isn't really about creating a new file (devs create files constantly in React/backend work) — it's that inventing a new abstraction requires thinking about how to do it right, extra effort that many aren't ready to invest, plus juniors don't yet see the consequences of *not* doing it ([[software-design]]).

## Key takeaways
- **Story 1 — `assertDate` in TestFactory (webilab):** their backend test suites have a `TestFactory` abstraction (creates test users/data/warehouses to set up the environment) and chai for assertions. Someone needed a custom assert for calendar dates — and it ended up as `TestFactory.assertDate`, purely because `TestFactory` was the object already available in every test, even though its responsibility is completely different. The right move was trivially small: a new module holding one function.
- That pattern generalizes to the classic **God Object antipattern**: he's watched base service classes accumulate date utils, file utils, session utils — everything dumped into the parent "so all child classes can reach it" instead of creating `DateUtils`, `FileUtils`, etc., until the base class is an unconnected pile of responsibilities.
- **Story 2 — the 100-line proof of concept that became a 5000-line file:** for a webilab PowerPoint-like web presentation system he wrote a small PoC (~100 lines): a serializable slide data structure, a widget primitive with position/rotation/config, and a couple of standard widgets (circle, rectangle, text). Six months later: one file, 5000 lines, every widget plus synchronization subsystems all mixed together, unsupportable. When he asked why, the answer was **"well, that's how *you* showed us."** His point: when it was 100 lines, that structure was right; as responsibilities grow you must extract new abstractions — but developers follow the existing pattern and just keep adding. Notably, the team *felt* the pain (things "wouldn't take off") and had themselves initiated the review.
- **Story 3 — builders (recap of [[voice-2-faster-ui-development|voice message #2]]):** given a low-level grid with a declarative config, everyone copies that raw config into every screen instead of writing a higher-level, project-specific builder/facade that hides the low-level configuration — same fear of adding a structure that doesn't exist yet.
- **Story 4 — the missing controller:** discussing a friends' React project with dumb and smart components, the missing piece was a coordination abstraction for high-level actions. His suggestion — just add a controller — felt uncomfortable to the team *because nobody on that project had ever done it*. Meanwhile at Google, when a UI subsystem lacked abstractions, he added controllers over the low-level pieces that hid configuration details, could be reused, and "wonderfully" simplified the code and its maintenance.
- The meta-lesson: experienced developers create new abstractions when responsibilities emerge; the reluctance to do so — reusing whatever structure already exists — is what slowly rots a codebase even while every individual change looks consistent with the surrounding code.

## Covered
[[abstractions]], [[software-design]], [[code-quality]]
