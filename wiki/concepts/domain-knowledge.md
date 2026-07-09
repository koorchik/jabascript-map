---
type: concept
tags: [engineering-craft, domain, architecture]
---
# Domain knowledge

First of the three skills in the channel's opening video: the domain, not patterns, dictates architecture ([[3-things-that-make-a-programmer-better]]). His chat example makes it concrete — the same "typing indicator" UI may need long-polling (comments under orders), plain 100-req/s polling (a 100-user corporate chat), or WebSockets, and only domain understanding tells you which. Domain knowledge also drives motivation: friends of his loved building the e-commerce parts of a project and lost all motivation on the logistics module — until they learned the business behind it and the work became interesting again.

The concept carries his central architectural warning: architecture quality depends on domain understanding, and at project start you almost never know the domain well enough — which is precisely why cutting microservice boundaries on day one is the underestimated killer of that architecture ([[microservices-main-problem]]), and why he loves the principle that good architecture *defers* decisions until you understand the domain better.

## Covered in
- [[3-things-that-make-a-programmer-better]] — domain dictates architecture (the typing-indicator example) and fuels motivation (the logistics story)
- [[microservices-main-problem]] — you never know the domain well enough on day one to slice service boundaries right

## Related
[[software-design]] — the domain is the primary design input
[[microservices]] — the architecture most punished by shallow domain understanding
[[abstractions]] — good boundaries are domain boundaries
[[domain-driven-design]], [[implementing-domain-driven-design]] — the books he recommends for exactly this
