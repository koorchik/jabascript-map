---
type: video
title_uk: "Як працює Інтернет? Як працює рекурсивний пошук в DNS?"
youtube_id: IgF7VwIKqX8
tags: [networking, dns, internet, protocols]
date_ingested: 2026-07-09
---
# How the Internet Works: DNS Recursive Resolution

> Original: "Як працює Інтернет? Як працює рекурсивний пошук в DNS?" — https://youtu.be/IgF7VwIKqX8

The second DNS episode answers the question left hanging from the first: does every DNS server in the world hold records for every website? No. The author walks — first on a whiteboard, then live in the terminal — through how **recursive resolution** works. He uses a concrete running example: you buy `itquiz.com` from a registrar, rent a server from a cloud provider (DigitalOcean/Google Cloud/Amazon — "doesn't matter"), and add an `A` record in the registrar's admin so visitors reach your box. The core puzzle: your provider's resolver has never heard of `itquiz.com` — how does it find the right authoritative server?

## Key takeaways
- The resolver your browser talks to (provider's DNS, a caching resolver on your home router, or `8.8.8.8`) is almost never the server where you added the record. It has to *discover* the answer.
- The hierarchy walked top-down: **root servers** (the zone `.`) know the nameservers for TLD zones (`.com`, `.org`, `.edu`…); the **TLD servers** (`.com`) return the `NS` records for `itquiz.com`; those point to the **authoritative DNS server** (in his case Cloudflare) that actually stores the `A` record. Resolution returns `NS` records step by step, then finally the `A` record.
- The resolver bootstraps from **root hints** — the IPs of the ~13 root servers baked into its config, so it always knows where to start.
- He proves every step by hand with `dig +norecurse`: querying `8.8.8.8` non-recursively returns nothing (Google hasn't cached it); `dig . NS` gets the 13 root servers; grab a root's IP, ask it for `.com` NS servers (the reply includes IPs in the **additional section** to save a round-trip), ask a `.com` server for `itquiz.com` NS (gets two Cloudflare nameservers + their IPv4/IPv6), then finally ask Cloudflare for the `A` record. Doing this manually is exactly what `8.8.8.8` does under the hood automatically.
- `dig +trace` automates the whole recursive walk from your local machine and prints each hop (root → `.com` TLD → authoritative), so you can watch it happen.
- **Caching + TTL:** because each lookup is many internet round-trips, servers cache. Every record carries a **TTL in seconds** — `itquiz.com` showed 300s (5 min), but 24h is common. You set it in the registrar admin. If TTL is 24h and you change your IP, the change doesn't propagate at once: different resolvers cached at different times, so some see it in minutes, others up to a full TTL later. Frequent IP changes → use a low TTL; stable IPs → use a high TTL.

## Covered
[[dns]], [[nat-and-networking]], [[latency-and-speed-of-light]], [[deep-learning-of-fundamentals]]
