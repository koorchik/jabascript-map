---
type: concept
tags: [engineering-craft, learning, fundamentals, philosophy]
---
# Deep learning of fundamentals

This is the channel's single most connective thesis — nearly every video, from DNS to AWD cars, is an application of it. The claim: there are two kinds of engineers, those who "just call the methods" and those who dig, and only understanding a technology's *internals* gives you its *properties* — what happens to the database if the data doubles, why an index speeds up one query shape and not another ([[3-things-that-make-a-programmer-better]], with John Carmack cited as his authority for "learn things deeply"). Marketing materials will never give you those properties; internals will ([[learning-deeply-and-remembering]]). The closing parable of the indexes deep-dive distills it: three programmers — one unaware of indexes, one who knows "indexes = faster," one who understands the internals — and only the third designs well ([[database-indexes-mysql-vs-postgres]]). The flip side is dogmatism, one of the three things that *ruin* a programmer: reading and believing instead of understanding, like "props in getInitialState is a React antipattern" repeated as absolute truth when the docs said it depends on the reasons ([[3-things-that-ruin-a-programmer]]).

The retention argument is his **knowledge-tree analogy** ([[learning-deeply-and-remembering]]): fundamentals are the trunk and branches that new knowledge hooks onto. Learn a leaf (a detail, a framework API) with no branch under it and it "falls to the ground" — forgotten in a month, the fate viewers complain about. With the branch in place, leaves regrow fast and knowledge compounds every year; prefer knowledge that stays relevant 5–10 years, and he even suggests drawing your own technology tree. His personal learning method builds on this: "useful procrastination" — binge many videos on a topic from different angles until saturation, then practice; connect everything new to everything you already know; learn a stack via theory plus a pet project you actually want to launch for a "virtual customer"; and books beat articles, because mid-book-chapter content can't survive as a standalone article ([[qa-and-plans-for-2024]]). Every engineer, he says there, should know OS basics, processes, and networking; to newcomers he adds: ship a pet project end to end — frontend, backend, DB, Docker, cloud, domain, DNS, mail — to own the whole delivery process ([[qa-2-answering-questions]]). Starter exercises from WebbyLab's internal 13–14-topic baseline: the "URL to rendered page" interview question, studying security exploits, writing a JSON parser with zero libraries ([[3-things-that-make-a-programmer-better]]).

In the AI era he argues fundamentals matter *more*, not less: without understanding internals you can only parrot marketing or the AI, which "does so much wrong" — his Flutter-over-React-Native call (native compilation vs a JS bridge, decisive for real-time telemetry math) is the kind of decision no prompt makes for you ([[vibe-coding-new-project]]). Depth is also a design prerequisite — you need each subsystem's properties to make the whole system meet its requirements ([[learning-deeply-and-remembering]], see [[software-design]]). And the thesis travels beyond software: "AWD" is a marketing label, and unless you understand torque splits, coupling cooling, and gearbox types you can't predict how the car behaves — Audi sells three very different things all called "quattro" ([[awd-systems-compared]]).

## Covered in
- [[learning-deeply-and-remembering]] — the core video: knowledge tree, internals → properties, 5–10-year knowledge, draw your own tree
- [[3-things-that-make-a-programmer-better]] — "just call the methods" vs digging, Carmack, WebbyLab's starter exercises
- [[3-things-that-ruin-a-programmer]] — dogmatism as the anti-pattern: believing instead of understanding
- [[database-indexes-mysql-vs-postgres]] — the three-programmers parable; internals predict a technology's properties
- [[vibe-coding-new-project]] — fundamentals matter more with AI; the Flutter-vs-React-Native call; the honest Rust→WASM 2x benchmark
- [[how-dns-works-basics]] — web devs should understand the internet end-to-end; buy a domain and play
- [[dns-recursive-resolution]] — reproduce every dig command yourself
- [[speed-of-light-website-latency]] — you must understand the network to design for it
- [[five-star-books]] — K&R C in two evenings: the layer beneath JS/Python (char arrays, null termination, hand-rolled hash table)
- [[awd-systems-compared]] — the thesis applied to cars: marketing labels vs implementation properties
- [[qa-2-answering-questions]] — ship a pet project end to end; why Docker on macOS eats RAM (it's a Linux VM)
- [[qa-and-plans-for-2024]] — the full learning method: useful procrastination, hooks onto existing knowledge, books over articles, OS + networking baseline

## Related
[[software-design]] — internals give you the properties designs are made of
[[domain-knowledge]] — the other half of "understand before you build"
[[career-and-growth]] — depth is his explanation of how engineers actually level up
[[database-indexes]], [[dns]], [[latency-and-speed-of-light]] — flagship demonstrations of the thesis
[[awd-and-drivetrains]] — the off-topic proof it generalizes
[[vibe-coding]] — why AI raises, not lowers, the value of fundamentals
