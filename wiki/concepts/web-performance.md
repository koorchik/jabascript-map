---
type: concept
tags: [performance, web, frontend, google]
---
# Web Performance (Core Web Vitals)

The channel's fullest take comes from the Google I/O watch party ([[google-io-2023-watch-party]]). Google converged on user-centric metrics — LCP (≤2.5s), CLS, and an interaction-latency target around 100ms (INP replacing FID) plus `fetchpriority` — precisely because the older PageSpeed metrics got gamed while pages still visibly twitched into place as they loaded. His contrarian addition: for logged-in thick-client apps behind auth, it's the *users'* opinion that matters, not Google's — metric-chasing is really for SEO and content sites. He runs live audits on stream (an Odesa JS site scores well). This sits alongside the physics side of speed covered in the latency episode: Core Web Vitals is the perceived-experience lever, latency is the hard floor.

## Covered in
- [[google-io-2023-watch-party]] — Core Web Vitals (LCP/CLS/INP), fetchpriority, why old metrics got gamed, and his "metrics are for SEO, not thick clients" take

## Related
[[latency-and-speed-of-light]] — the physical floor under any performance metric
[[webgpu]] — another Google I/O browser-capability topic
[[nextjs]] — SSR/framework choices that affect these metrics
[[react]] — thick-client apps where he argues Google's metrics matter less
