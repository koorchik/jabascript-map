---
type: tool
tags: [react, ssr, framework, frontend]
---
# Next.js

Next.js is the React framework for server-side rendering and static generation. Viktor's verdict is love with a caveat ([[qa-and-plans-for-2024]]): his mytalks project runs on it, and he values exactly what it delivers — isomorphic SSR, SEO and fast page loads. Coming from someone who wrote an award-winning production-SSR article back when you had to build it yourself, that endorsement carries weight. The criticism targets its internal architecture: it isn't parametrizable enough — he couldn't configure the static-page cache to live on S3, the kind of extension point he expects a framework to expose.

## Covered in
- [[qa-and-plans-for-2024]] — loves it for SSR/SEO/speed (mytalks runs on it); criticizes the non-parametrizable static-page cache (no S3 option).

## Related
[[react]] — the library underneath, and his hand-rolled-SSR prehistory.
[[nodejs]] — the runtime Next.js servers run on.
[[web-performance]] — SSR and fast loads as the reason to use it.
[[software-design]] — the missing cache extension point as a design critique.
