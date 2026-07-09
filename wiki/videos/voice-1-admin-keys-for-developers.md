---
type: video
title_uk: "Голосове №1 - чому не можна давати розробникам адмінські ключі"
youtube_id: zmXSLPvGea4
tags: [security, security-practices, least-privilege, career, war-story, podcast]
date_ingested: 2026-07-09
---
# Voice Message #1: Why You Shouldn't Give Developers Admin Keys

> Original: "Голосове №1 - чому не можна давати розробникам адмінські ключі" — https://youtu.be/zmXSLPvGea4

The first episode of a new sponsors-only audio-podcast format: shorter, more casual life-stories from development, recorded when the author is travelling and can't shoot a full video (which he reserves for deep, non-aging fundamentals). This one is a war story about least privilege. Back when he and Anton Morozov founded Webbylab with a small team, they asked a developer to write a Redmine analytics/reporting script and debated whether to issue an admin API key or a normal one — they picked admin, figuring "nothing bad will happen."

## Key takeaways
- The developer wasn't malicious: he searched GitHub for a Redmine API library, copied the example straight from its documentation, and ran it with the admin key — and the example's sample calls deleted user #2, renamed user #5, etc.
- Real damage surfaced over days: co-founder Anton could no longer log in (his user had been deleted); a week later a Ukrainian client named Oleksandr wrote in asking why they'd renamed him to "Raul" with his Ukrainian surname — the sample code had overwritten real records.
- The lesson the author draws: handing developers admin keys is a bad idea — scope credentials to the task (least privilege), because even accidental, copy-pasted example code can wreak havoc with elevated rights.
- Framing note: this is the first of a planned series of such stories; he says these take little time to record so he'll do them regularly.

## Covered
[[security-practices]], [[least-privilege]], [[social-engineering]], [[career-and-growth]]
