---
type: video
title_uk: "Книги, які я прочитав й поставив п'ять зірок"
youtube_id: ij0y4qVLSF0
tags: [books, recommendations, career, software-design, sponsors-video]
date_ingested: 2026-07-09
---
# Books I Read and Rated Five Stars

> Original: "Книги, які я прочитав й поставив п'ять зірок" — https://youtu.be/ij0y4qVLSF0

A sponsors video born from a GeekOps meetup question ("what books do you read?") that wasn't recorded: the author walks top-to-bottom through his Goodreads list and comments on every book he gave five stars. Almost all are technical, none are fiction, and his rule of thumb is: five stars means "read it *if the topic interests you*; if not, skip." Along the way he shares his personal history with the books — reading [[code-complete|Code Complete]] 14 years ago and learning there is no ideal third solution, discovering at Mail.ua that his team had independently re-invented 8 of the 24 GoF patterns before he ever read the book, and using [[cracking-the-coding-interview|Cracking the Coding Interview]] to prepare for his Google interviews. The list ranges across [[software-design]], time management, Linux, B2B sales, manufacturing theory, motor racing, and game-industry war stories.

## Key takeaways
- **Code Complete** answered the question that haunted him as a beginner: "is there a third solution that improves *this* aspect without hurting *that* one?" The book convinced him such a solution usually doesn't exist — engineering is trade-offs — and he "was convinced of it many times since." It's from 1993, so the code examples are dated, but conceptually it still holds.
- **His theory of design patterns** ([[design-patterns|GoF]]): patterns are not sacred secret knowledge — they're the *most widespread* solutions everyone already uses. Proof from his own career: working at Mail.ua before reading the book, his team's architecture already contained eight of the book's patterns, because they were simply the most logical choices. The real value of learning them is a shared vocabulary with other developers ("I want a facade here", "let's use a strategy for the log transport").
- **[[patterns-of-enterprise-application-architecture|Fowler's PoEAA]]** is the pattern book he recommends to everyone over GoF: high-level *strategic* patterns. You'll never implement ~70% of them yourself, but you'll *lean on* them daily because they're already inside your ORM and web framework.
- **[[domain-driven-design|DDD]]**: read both Evans and Vernon. Evans can feel too abstract (concepts, not code); Vernon shows exactly how to structure the code — but people who only read Vernon mistake code structure for DDD, when the conceptual idea is the point. One of the best design books he knows; first of all for backenders, useful for frontenders too — it's about fighting complexity ([[software-design]]).
- **[[mythical-man-month|The Mythical Man-Month]]**: read it to see that between 1975 (paper stacks instead of Jira, IBM mainframe OS development) and 2024 essentially nothing changed — the same constraints remain, including essential vs accidental complexity, concepts you meet every day.
- **[[c-programming-language|K&R C]]** is thin — a couple of evenings — but afterwards you understand what actually happens beneath JavaScript or Python: a string is an array of characters, copying it means a loop, null-terminated strings, plus a great hand-rolled hash table implementation ([[deep-learning-of-fundamentals]]).
- **[[cracking-the-coding-interview|Cracking the Coding Interview]]**: the tasks themselves you can grind on LeetCode/AlgoExpert; the underrated gold is the two intros — what interviewers actually expect from you, and a very good primer on [[algorithmic-complexity]] analysis.
- Non-programming five-stars he vouches for: [[the-goal|The Goal]] (theory of constraints as a novel — he knows people in Ukraine who built a working manufacturing business from Goldratt's books), [[good-strategy-bad-strategy|Good Strategy Bad Strategy]] (mostly valuable for saying what is *not* a strategy), [[the-checklist-manifesto|The Checklist Manifesto]] (changed his view of checklists), [[spin-selling|SPIN Selling]] (the B2B sales classic), and Lem's [[summa-technologiae|Summa Technologiae]] (1960s pure-logic futurology in which he recognized the plots of The Matrix and The Thirteenth Floor).

## Full book list with verdicts
- **Getting Things Done** (David Allen) — read back in university; he still uses its idea of separate lists per context: when he lands in a context, he walks that context's list. Recommended, but it's time management, not programming.
- **The 7 Habits of Highly Effective People** (Stephen Covey) — "класика класика" of time management and personal development; very recommended.
- **Code Complete** (Steve McConnell) — thick, many start and never finish it; see takeaway above. Strongly recommended: naming, structuring code, optimization, profiling — "по полочкам."
- **Patterns of Enterprise Application Architecture** (Martin Fowler) — his universal patterns recommendation; explains how the systems you use are built.
- **Higher-Order Perl** (functional programming in Perl) — great book, but if you don't write Perl it probably won't interest you.
- **Domain-Driven Design** (Eric Evans) + **Implementing Domain-Driven Design** (Vaughn Vernon) — recommends both; order is debated; Evans worked great for him personally.
- **A 2001 Linux security book** (title not stated) — read it several times, the book itself was great, but **don't read it**: it's simply outdated; if new editions existed he'd recommend it.
- **Summa Technologiae** (Stanisław Lem) — pure emotionless reasoning about the world ~1000 years out; will click for some, not for others.
- **The Goal** (Eliyahu Goldratt) — theory of constraints written as a novel; small, reads easily, "класика класика"; a must if you run a business or optimize processes.
- **How Linux Works** (Brian Ward) — practical-theoretical tour of Linux subsystems, network stack, administration; readable in a week; great book (check for a newer edition).
- **Speed Secrets / Ultimate Speed Secrets** (Ross Bentley) — he read the whole series; the books largely repeat each other, so read the latest, *Ultimate Speed Secrets*. It was his starting point as a driver and made him faster on track/karting.
- **SPIN Selling** (Neil Rackham) — the rare classic on B2B (vs B2C) sales; worth knowing even if you don't build your process exactly by it.
- **It's Not Luck** (Eliyahu Goldratt) — read The Goal first, then decide whether to continue with Goldratt.
- **Design Patterns** (GoF — Gamma et al.) — see the Mail.ua story above; read it for the shared lexicon, not for revelations.
- **The Mythical Man-Month** (Frederick Brooks) — see takeaway above; also an excursion into pre-internet development.
- **The C Programming Language** (Kernighan & Ritchie) — see takeaway above.
- **Clean Code** (Robert Martin) — skipped in the video: "everyone has heard of it."
- **Who: The A Method for Hiring** — decent, many good ideas about building a recruiting process, but for him it wasn't the revelation others claim; much of it you could reach on your own.
- **The Checklist Manifesto** (Atul Gawande) — a list of stories about when and why checklists worked; gives you one more process-improvement tool.
- **Good Strategy Bad Strategy** (Richard Rumelt) — what a strategy is (its three building blocks) and, most importantly, what is NOT a strategy; strongly recommended if you take part in strategic planning.
- **Cracking the Coding Interview** (Gayle Laakmann McDowell) — used for his own Google prep; see takeaway above.
- **A Docker internals book** (title not stated; regularly updated, 2023 edition — matches Docker Deep Dive) — quick, easy read on how Docker works inside: subsystems, overlay networks, practical usage.
- **A karting-specific racing book** (title not stated) — ~70% overlaps with Ultimate Speed Secrets, 30% different perspective; the two together are more useful than either alone.
- **Sandworm** (Andy Greenberg) — cybersecurity; mentioned but skipped without a verdict.
- **The Staff Engineer's Path** (Tanya Reilly) — explains what a staff engineer even does, how to become one and what to do next; the start gripped him, but it got less interesting toward the end and he finished it slowly. Still useful.
- **Blood, Sweat, and Pixels** (Jason Schreier) — game-industry stories from Stardew Valley to AAA; "прям топ": if the book covers even one game you know, buy it.
- **Software Engineering at Google** — currently (almost) finished; the entire Google development process from A to Z in 600 pages; free PDF available.
- **Making Sense of Squiggly Lines** — racing telemetry analysis; no ebook exists, he ordered a paper copy from the US; very good if you race.
- **Designing Data-Intensive Applications** (Martin Kleppmann) — famous, but honestly admits it has been hanging unfinished for a long time.

## Covered
[[software-design]], [[design-patterns]], [[algorithmic-complexity]], [[deep-learning-of-fundamentals]], [[career-and-growth]], [[clean-architecture]], [[domain-driven-design]], [[patterns-of-enterprise-application-architecture]], [[code-complete]], [[mythical-man-month]], [[c-programming-language]], [[cracking-the-coding-interview]], [[the-goal]], [[good-strategy-bad-strategy]], [[the-checklist-manifesto]], [[spin-selling]], [[summa-technologiae]]
