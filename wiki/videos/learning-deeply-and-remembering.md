---
type: video
title_uk: "Навіщо глибоко розбиратися в речах й як менше забувати те, що вивчили?"
youtube_id: vunaSc37B5o
tags: [fundamentals, learning, career, knowledge]
date_ingested: 2026-07-09
---
# Why Learn Things Deeply, and How to Forget Less of What You Learned

> Original: "Навіщо глибоко розбиратися в речах й як менше забувати те, що вивчили?" — https://youtu.be/vunaSc37B5o

A conceptual follow-up to [[3-things-that-make-a-programmer-better]], triggered by two viewer comments: "I learned network protocols at university and never once needed them" and "whatever I learn, I forget in a month — do I have to keep re-learning?". He defers the concrete war stories to a separate video and instead gives his mental model of why depth matters ([[deep-learning-of-fundamentals]]) and his **knowledge-tree** analogy for why fundamentals make new knowledge stick.

## Key takeaways
- He used to think deep understanding was mainly for debugging (where it does save enormous time), but the bigger payoff is **design**: you can't base architecture on marketing materials. Understanding how a system works inside — even just conceptually — gives you its *properties*, and you need the properties of every subsystem to make the overall system meet its requirements ([[software-design]]).
- His standing test questions for any database (MySQL, MongoDB, Postgres, whatever): what happens to performance if you pour in twice the data? How do its transactions and isolation actually behave? If you can't answer, you don't know the system's properties and can't design with it.
- **The knowledge tree**: the trunk is the most fundamental knowledge; branches are fields; twigs are more detailed concepts; leaves are the super-fine details. New knowledge must *catch onto* an existing branch — it also hooks onto practical experience. If the branch isn't there, the new leaf "falls to the ground and is lost" — that's exactly the "I forgot it in a month" effect. He even suggests literally drawing such a tree of your technologies.
- **Leaves fall, branches remain.** A viewer said he read a whole book on TLS and forgot the protocol details two months later. Fine — what stays is the branch: you still know [[https-tls|TLS]] has a certificate chain, a symmetric session key, and that forward secrecy is only guaranteed with Diffie-Hellman key exchange, not when the session key is exchanged via the private key. With the branch in place you can re-hang the leaves quickly whenever needed, and hook neighbouring branches onto it.
- Rule of thumb for what to learn: prefer fundamentals that won't lose relevance in a month or a year — things that hold for 2, 5, sometimes 10 years. The tree then compounds year after year, and you understand how distant leaves relate (or don't) to each other.
- Closing recommendation: the classic ~5-minute "MongoDB is web scale" cartoon (link under the video) — "absolute top" — because it's precisely about understanding a system's properties and internals instead of buying the hype ([[mongodb]]).

## Covered
[[deep-learning-of-fundamentals]], [[software-design]], [[career-and-growth]], [[https-tls]], [[mongodb]]
