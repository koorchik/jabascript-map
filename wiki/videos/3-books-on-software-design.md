---
type: video
title_uk: "3 важливі книги про проектування програмного забезпечення"
youtube_id: p7awmGY9yus
tags: [books, software-design, architecture, recommendations]
date_ingested: 2026-07-09
---
# 3 Essential Books on Software Design

> Original: "3 важливі книги про проектування програмного забезпечення" — https://youtu.be/p7awmGY9yus

Viewers keep asking for programming book recommendations, but "programming" is too broad — so the author narrows it to three foundational books on [[software-design]], each of which, he says, makes you look at building a program from a slightly different angle. He deliberately avoids "hardcore" picks: these are the fundamentals to start with. The three books form a set that he presents as mutually reinforcing: [[clean-architecture|Clean Architecture]] tells you *which layers* a backend should have, [[patterns-of-enterprise-application-architecture|Fowler's patterns]] show *how those layers are actually implemented* in real systems, and [[domain-driven-design|DDD]] explains *why* understanding the problem domain decides whether a project succeeds at all.

## Key takeaways
- **Clean Architecture (Robert Martin)** — half the book is about how to structure a backend into layers and the logic behind that layering; the other half is SOLID. Basic but very useful. The author promises follow-up channel videos digging deeper: not just "here are the layers" but how to implement each layer.
- **Domain-Driven Design (Eric Evans)** — explains why some projects fail while others succeed, and why adding features is easy in some codebases and painful in others; the answer is designing around the domain. For the author this book was a genuine revelation ("прям відкриттям") that changed how he looks at development.
- He relays an Evans interview detail: Evans's one regret about the book is that the crucial *bounded context* topic sits at the end instead of the beginning. Even reading only half the book already changes how you think.
- **Patterns of Enterprise Application Architecture (Martin Fowler)** — don't be scared off by "Enterprise" in the title; the author doesn't know why it's named that, but the book is great. Unlike the tactical GoF patterns, these are *strategic* patterns.
- You will likely never implement Fowler's patterns directly, but you will *meet every one of them* in your application — inside your ORM, your framework, your backend structure. The book teaches you how the tools you already use actually work.
- The three books interlock: Fowler complements Clean Architecture (which describes layers but not how to realize them) and adds concrete patterns (value objects, etc.) to the ideas of DDD.

## Covered
[[software-design]], [[clean-architecture]], [[domain-driven-design]], [[patterns-of-enterprise-application-architecture]]
