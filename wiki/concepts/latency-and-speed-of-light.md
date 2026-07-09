---
type: concept
tags: [networking, performance, latency, internet]
---
# Latency and the Speed of Light

The channel's most striking "how the internet works" argument: your website's speed is bounded by physics, not bandwidth ([[speed-of-light-website-latency]]). Kyiv → LA is ~10,000 km; light in fiber travels ~200,000 km/s (versus 300,000 in vacuum), giving 50ms one way and a 100ms best-case ping — his memorable line is that you'll never get sub-100ms CS:GO ping to US servers. He then stacks the round-trips: request + backend + response already costs 120ms, six times a 20ms backend; adding the TCP handshake pushes it to 220ms; adding the TLS handshake takes it to ~420ms (21x the backend) — and that still ignores DNS lookup and TCP slow-start. The conclusion is that CDNs matter because they cut *latency*, not raw speed. A companion point in the DNS series: each lookup is itself many internet round-trips, which is exactly why DNS caching exists ([[dns-recursive-resolution]]).

## Covered in
- [[speed-of-light-website-latency]] — the core derivation: fiber speed, 100ms ping floor, stacked TCP/TLS round-trips turning a 20ms backend into ~420ms, why CDNs help
- [[dns-recursive-resolution]] — each DNS lookup is many round-trips, motivating caching

## Related
[[nat-and-networking]] — the TCP handshakes that stack up here
[[https-tls]] — the TLS handshake adds the biggest single chunk
[[dns]] — an extra, uncounted lookup on top of the request
[[web-performance]] — latency is one lever; Core Web Vitals is the other side
[[nginx]] — the LA test server used to measure real round-trips
