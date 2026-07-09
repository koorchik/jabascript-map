---
type: video
title_uk: "Що не так з Інтернетом в кафе? Розбираємо DHCP"
youtube_id: 1-VHB-dn4NM
tags: [networking, dhcp, security, internet, protocols]
date_ingested: 2026-07-09
---
# What's Wrong with Café Wi-Fi? Breaking Down DHCP

> Original: "Що не так з Інтернетом в кафе? Розбираємо DHCP" — https://youtu.be/1-VHB-dn4NM

Another episode in the "how the internet works" series, framed around a security-flavored scenario: you sit down in a café, connect to the Wi-Fi, and your laptop has zero network settings. The common assumption is that it asks the router for settings — but the author's point is that it's "worse than that": your device has no IP, no MAC of the router, nothing, so it can't ask anyone *specific*. It shouts a broadcast to everyone: "anybody, give me network settings." The answer can come from the router **or from any machine on the network** — someone at the next table running a rogue DHCP server on their phone/laptop can hand you a malicious [[dns]] server (feeding fake IPs) or a malicious default gateway (routing all your unencrypted traffic through their box). This is **[[dhcp]]** — Dynamic Host Configuration Protocol — and he then builds the attack live.

## Key takeaways
- Because the client has no settings yet, it can't use TCP (which needs a handshake to a known peer). **DHCP rides on UDP broadcast**: destination IP `255.255.255.255` (all bits 1) and MAC `FF:FF:FF:FF:FF:FF`. Broadcasts reach every host in the LAN but do not cross the router (not routed).
- Ports identify DHCP traffic: server listens on UDP **67**, client on **68**. That port is how a host tells a DHCP broadcast apart from, say, IPTV multicast.
- The DORA exchange: client broadcasts **Discover**, servers reply **Offer**, client picks one (usually whichever arrives first) and broadcasts a **Request** naming the chosen server, server records the MAC→IP binding with a **lease time** and confirms.
- **Lease renewal timers:** at ~50% of the lease (T1) the client tries to renew directly with the same server; if that fails, at ~87.5% (T2) it broadcasts to everyone again. These come from the RFC and are configurable.
- **The rogue-server race and how to win it:** with both a legit and a rogue server present it's a coin toss whose offer arrives first. The attacker doesn't even need to disable the router's DHCP — he just exhausts its pool. He set his server's range to only 10 addresses; an attacker sends ~10 Discover requests with different fake MACs, the server reserves all 10 for nonexistent machines, and the 11th real client gets "no addresses left" — so only the rogue server can answer.
- **Live demo:** he uses **dnsmasq** — a tiny combined caching-DNS + DHCP server — with ~5 config lines: upstream `server=8.8.8.8`, an override making `itquiz.com` resolve to a Google IP, a `dhcp-range`, plus `option:router` and `option:dns-server` pointing at his own machine. He disables his router's DHCP, sets a static IP on his PC, then on a tablet toggles Wi-Fi and watches in Wireshark (filtered on `dhcp`): the tablet issues a Request for its old IP but is refused because he changed its MAC, then goes through the full Discover/Offer/Request/Ack, receiving his poisoned DNS server. Opening `itquiz.com` on the tablet lands on Google with a certificate mismatch (red warning), proving the DNS spoof worked.

## Covered
[[dhcp]], [[dns]], [[nat-and-networking]], [[security-practices]], [[https-tls]]
