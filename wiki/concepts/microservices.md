---
type: concept
tags: [architecture, microservices, distributed-systems]
---
# Microservices

Viktor opens with Simon Brown's line: *"what makes you think you can build microservices if you can't build a monolith?"* ([[microservices-main-problem]]). He runs through the known costs people at least discuss: you need an orchestration platform; rollbacks demand version-compatibility guarantees between services; per-service databases kill transactionality ("distributed transactions — just forget it," illustrated with a bookkeeping example); network calls fail in ways in-memory monolith calls never do; the polyglot argument has dubious economics; and hiring gets harder.

But the underestimated killer, in his view, is about [[domain-knowledge]]: on day one you almost never understand the domain well enough to slice service boundaries correctly — and unlike a monolith, you can't cheaply refactor the cut. Wrong abstractions happen in monoliths too, but fixing them in one codebase is easy; across microservices in different languages owned by different teams it is incredibly hard. Making each individual service simple doesn't remove complexity either — it migrates to the communication level and "turns into porridge." He ties this to Robert C. Martin's idea he loves: the architect's job is to *defer* decisions, because domain understanding improves daily, so later decisions are better ([[microservices-main-problem]]). Verdict: in ~90% of cases start with a modular monolith and split later — he cites Medium's migration article as evidence.

## Covered in
- [[microservices-main-problem]] — the whole argument: known costs, the domain-boundary trap, complexity migrating to communication, "defer decisions," modular-monolith-first verdict

## Related
[[domain-knowledge]] — the root problem: you can't cut boundaries in a domain you don't yet understand
[[abstractions]] — a service boundary is an abstraction you can no longer cheaply refactor
[[software-design]] — good architecture maximizes decisions not made
[[technical-debt]] — wrong service cuts as the most expensive debt
[[clean-architecture]] — source of the defer-decisions principle
