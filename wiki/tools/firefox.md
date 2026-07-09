---
type: tool
tags: [browser, networking, security, tooling]
---
# Firefox

Web browser. It shows up on the channel in two roles. In the DNS basics episode he uses Firefox dev tools to display DNS-resolution timing metrics, disabling its DNS-over-HTTPS and the OS cache to demonstrate plain resolution ([[how-dns-works-basics]]). In the Bloom-filter episode Firefox is the hero of the story: its CRLite uses cascade Bloom filters to ship *all* ~4M revoked certificates in ~300 KB/day (now 30–50 KB deltas) plus a 4 MB snapshot every 45 days, fully deployed since 2025 — giving deterministic certificate-revocation checks with zero extra network requests, where Chrome ships only the top ~1% of revocations ([[bloom-filter-and-firefox]]).

## Covered in
- [[how-dns-works-basics]] — dev-tools DNS timing, disabling DoH and OS cache
- [[bloom-filter-and-firefox]] — CRLite cascade Bloom filters for full certificate-revocation coverage

## Related
[[dns]] — the resolution it visualizes
[[bloom-filter]] — the structure behind CRLite
[[https-tls]] — certificate revocation is a TLS trust problem
