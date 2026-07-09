---
type: video
title_uk: "Як швидкість світла обмежує швидкість твого веб-сайту? Розбираємо на реальному прикладі"
youtube_id: dRnAeHeLRS8
tags: [networking, performance, latency, internet, protocols]
date_ingested: 2026-07-09
---
# How the Speed of Light Limits Your Website's Speed

> Original: "Як швидкість світла обмежує швидкість твого веб-сайту? Розбираємо на реальному прикладі" — https://youtu.be/dRnAeHeLRS8

The opening video of the "how the internet works" series. Its thesis: when people talk about web performance they focus on frontend, backend, First Meaningful Paint — but there's a huge limiter they ignore, and it's **the speed of light** (more precisely, latency). The author builds a running back-of-the-envelope calculation and then verifies it against a real server, showing that a request whose backend takes 20 ms can easily take 400–800 ms in practice, dominated entirely by round-trips.

## Key takeaways
- **The setup:** backend in LA/San Francisco processing in 20 ms, client in Kyiv, ~10,000 km apart. Even under absurdly optimistic assumptions — a single straight fiber cable, no Wi-Fi, no routing, no providers — physics sets a floor.
- **The math:** light in vacuum is 300,000 km/s but in fiber ~200,000 km/s (a third slower). 10,000 km one way = 50 ms, so ping round-trip = 100 ms *at best*. His concrete conclusion: you'll never play CS:GO on US servers from Kyiv under 100 ms ping — the speed of light won't let you.
- **Stacking the round-trips:** request (50 ms) + backend (20 ms) + response (50 ms) = 120 ms, already 6× the backend time. Add the **TCP handshake** (SYN / SYN-ACK / ACK) — the ACK can carry the request data so it's ~one extra round-trip → 220 ms (11× the backend). Add **TLS handshake** (Hello, certificate, key exchange, each direction) → ~420 ms, 21× the 20 ms of actual work. And he notes this still ignores the DNS lookup and TCP slow-start (can't blast 50 KB at full speed immediately).
- This is *why* CDNs matter — not raw speed but reducing latency by putting static files/images closer to the user.
- **Real-world verification:** he stood up an nginx server in LA, made a subdomain, and captured plain HTTP and HTTPS requests in Wireshark. TCP handshake alone measured ~190–192 ms per round-trip; the plain-HTTP request/response was ~400 ms; the full HTTPS request came to ~800 ms — roughly 2× his theoretical 420 ms. A raw `ping` confirmed ~192 ms round-trip, worse than ideal because of real Wi-Fi, providers, and indirect routing.
- He points out ACKs recurring through the capture: TCP must acknowledge received data (UDP doesn't), which is the core reliability trade-off and part of the cost.

## Covered
[[latency-and-speed-of-light]], [[nat-and-networking]], [[dns]], [[https-tls]], [[deep-learning-of-fundamentals]]
