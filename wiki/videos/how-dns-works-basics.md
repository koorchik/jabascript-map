---
type: video
title_uk: "Як працює Інтернет? Основні питання про DNS"
youtube_id: bUKkYCdloH4
tags: [networking, dns, internet, protocols]
date_ingested: 2026-07-09
---
# How the Internet Works: The Basics of DNS

> Original: "Як працює Інтернет? Основні питання про DNS" — https://youtu.be/bUKkYCdloH4

First of a three-video mini-series on how the internet works, this episode explains what [[dns]] is and why we need name resolution. The author starts from the problem: when you type `rozetka.ua` or `google.com`, how does the browser know which server IP to hit, given that a big site runs on many servers that change over time? He traces the history — before DNS (introduced 1985) there was just a `hosts.txt` file copied between machines — and demonstrates live editing his own hosts file to point `rozetka.com.ua` at a Google IP, showing that (a) the browser caches DNS so nothing changes until you restart it, and (b) even hitting Google's IP you get a certificate/host error, because the server also inspects the domain name sent in the HTTP request. He then walks through a batch of practical questions using the `dig` tool and Wireshark packet captures.

## Key takeaways
- The OS itself knows nothing about DNS servers — the DNS server address comes from your network settings (from the DHCP server on the router, from the provider, or set manually; on Linux see `/etc/resolv.conf`). He manually set his resolver to Google's `8.8.8.8` to demonstrate.
- A single domain can return multiple IPs. `dig` on `my.talks.net` returned four addresses, and repeating the query shows the order rotating — this is **DNS round-robin**, a crude load-balancing and failover mechanism (browsers will try another IP if one is down; "better than nothing").
- Record types matter: `A` = IPv4, `AAAA` = IPv6, `MX` = mail servers, `TXT` (e.g. Google site verification, SPF), `NS` = which nameservers hold a domain's config. `A`/`AAAA` are the most common because that's what you need to reach a site.
- **DNS uses UDP, but sometimes TCP.** He ran a poll on his channel — only 17% of 215 voters got this right. In Wireshark he shows a normal query going out UDP port 53. UDP datagrams cap around 512 bytes; if the answer doesn't fit, the server sets the **truncated (TC) flag** to 1 and the client retries over TCP. He demonstrates this with a deliberately large TXT record (`jabascript` under his domain), showing the TC=1 flag then the TCP handshake and multi-segment reassembled response. TCP isn't used first because the handshake costs extra round-trips.
- DoH (DNS over HTTPS) adds privacy via encryption; Firefox (as of 2022, incl. Ukraine) and Chrome increasingly do DNS over HTTPS. He disabled DoH and OS caching in Firefox specifically to demonstrate plain resolution, noting caching happens at every level: browser, OS, router, provider.
- **Who actually makes the query — browser or OS?** Neither reimplements DNS. Processes load the standard C library (**glibc** on Linux) which does the work, checks `hosts`, uses `/etc/nsswitch.conf` ordering, etc. On systemd systems a local caching resolver runs at `127.0.0.53` and supports DNSSEC. War-story tip: **Alpine Linux** uses **musl libc** instead of glibc, and musl historically did NOT support DNS-over-TCP fallback — so oversized responses could silently fail on tiny Alpine (node:alpine, python:alpine) Docker images. He notes this was being fixed (post dated May 16, 2023).
- Practical advice: if you're a developer, buy a domain and play with the records (he manages his on Cloudflare) to understand things end-to-end. Static IPs can be pinned to a DNS name; **Dynamic DNS** re-registers your changing home IP automatically, and many home routers support it, letting you reach your home machine from outside.

## Covered
[[dns]], [[nat-and-networking]], [[dhcp]], [[latency-and-speed-of-light]], [[deep-learning-of-fundamentals]], [[firefox]]
