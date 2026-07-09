---
type: video
title_uk: "Головна проблема мікросервісів, яку часто недооцінюють"
youtube_id: MCFMQR6Yvd0
tags: [microservices, architecture, monolith, software-design]
date_ingested: 2026-07-09
---
# The Main Problem of Microservices That People Underestimate

> Original: "Головна проблема мікросервісів, яку часто недооцінюють" — https://youtu.be/MCFMQR6Yvd0

A warning for anyone planning to *start* a new project with [[microservices]]. People see them as simpler "because they're small", but the problems outnumber the first impression. He opens with Simon Brown's line — "what makes you think you can build a microservices architecture if you can't build a monolith?" — runs through the well-known (solvable) problems, and then lands on the conceptual one he thinks is underrated: **on day one you never know the domain well enough to slice service boundaries correctly**, and unlike a monolith, microservices make fixing the wrong cut brutally expensive ([[domain-knowledge]], [[software-design]]).

## Key takeaways
- The "known" costs he lists first: instead of one deployed binary you get a wagon of services needing an orchestration platform for building/deploying/rollbacks; **version compatibility** — after rolling back service B you must somehow guarantee A/B/C still fit together (a non-problem in a monolith where all code ships together); each service having its own database kills transactionality — for something like a bookkeeping system needing an atomic posting across services, "distributed transactions… just forget it"; and a call to another module in a monolith always succeeds (it's in memory), while a microservice call can be down or half-down, all of which needs handling patterns and complicates the program.
- He's also skeptical of the "right technology per task" pitch — one service in each of four languages: does that really make development cheaper or maintenance easier? "I'm not sure." Plus you have to *hire* people who actually know how to do all this, in the current market — one more huge problem.
- The core idea comes from Robert C. Martin's talk (link under the video): the architect's job is **not to make decisions but to defer them as long as possible — good architecture maximizes the number of decisions NOT made**. It sounds like heresy, but: architecture quality depends on how well you understand the domain, you understand it better every day, so a decision taken later is a better decision. You deliberately add [[abstractions]] (without fanaticism) that let you decide later.
- Microservices are the opposite bet: they assume that on day one you already know how to cut the system into pieces — but you almost never know the [[domain-knowledge|domain]] well enough yet. A monolith suffers the same wrong-abstraction problem, **but there you have refactoring**: one codebase, one or a few teams, you move responsibilities between modules and classes easily. With microservices in different languages owned by different teams, the same fix is "incredibly hard."
- His favourite mechanism of decay: everyone makes each microservice nice and simple, **but the complexity doesn't disappear — it migrates to the communication level**. When the service boundaries turn out wrong, teams try to fix it in the inter-service communication, one service pulls another pulls a third, extra services get added — "it turns into porridge."
- Bottom line: in ~90% of cases start with a **modular monolith** (a monolith should always be modular) — then splitting it into microservices later, when you actually understand the domain and know *why* you need them, is much easier and usually works better than starting with microservices. He points to Medium's engineering article about their monolith-to-microservices migration (link under the video) as a good example of the approach.

## Covered
[[microservices]], [[software-design]], [[abstractions]], [[domain-knowledge]]
