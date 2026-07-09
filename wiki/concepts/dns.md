---
type: concept
tags: [networking, dns, internet]
---
# DNS (Domain Name System)

The channel treats DNS as the flagship of its "How the Internet works" series. Before DNS (which arrived in 1985) the mapping of names to IPs lived in a hand-distributed `hosts.txt`; a residue survives as `/etc/hosts`, which the author edits live to spoof rozetka to a Google IP — showing the browser's own DNS cache and the fact that the *server* also inspects the domain in the HTTP request, so a matching IP alone isn't enough ([[how-dns-works-basics]]). He walks the common record types (A/AAAA/MX/TXT/SPF/NS), presents DNS round-robin (multiple IPs for one name) as crude load-balancing and failover, and covers DNS-over-HTTPS (DoH) as browsers moving resolution out of the OS. A favorite gotcha: DNS runs over UDP port 53 but falls back to TCP once the answer passes ~512 bytes (the truncated/TC flag flips to 1), demoed with a large TXT record — only 17% of 215 poll voters knew this. He also stresses that resolution is performed by glibc/libc, not the browser or kernel, and that systemd runs a caching resolver at 127.0.0.53.

The second episode answers "does every DNS server hold every domain?" — no ([[dns-recursive-resolution]]). Using a freshly bought itquiz.com plus a cloud server as the running example, he walks the hierarchy: root servers (zone `.`) → TLD servers (`.com`) → the authoritative server (Cloudflare) that holds the A record, with NS records returned at each hop and the resolver bootstrapping from ~13 root hints. He proves every hop by hand with `dig +norecurse` (the additional section carries glue IPs to save round-trips) and automates the whole walk with `dig +trace`. TTL gets a clear treatment: itquiz.com showed 300s, 24h is common; low TTL for frequently-changing IPs, high for stable ones — which is why IP changes propagate unevenly as caches expire.

DNS is also the attack surface in the DHCP episode: a rogue DHCP-supplied DNS server poisons name resolution, and he overrides itquiz.com to a Google IP via [[dnsmasq]], producing a certificate mismatch on the victim tablet ([[dhcp-cafe-wifi]]).

## Covered in
- [[how-dns-works-basics]] — hosts.txt history, /etc/hosts spoof, record types, round-robin, DoH, UDP→TCP at 512 bytes, glibc does the lookup
- [[dns-recursive-resolution]] — root→TLD→authoritative walk, dig +norecurse/+trace, glue records, TTL and cache propagation
- [[dhcp-cafe-wifi]] — rogue DNS poisoning via DHCP, live dnsmasq override
- [[speed-of-light-website-latency]] — DNS lookup as an uncounted extra latency component
- [[vm-network-isolation]] — guest DNS set to 8.8.8.8 via pfSense DHCP
- [[3-things-that-make-a-programmer-better]] — "who actually performs the DNS query?" as an example of hidden depth

## Related
[[dhcp]] — hands out the DNS server address; the rogue-DHCP attack hijacks DNS
[[nat-and-networking]] — layered resolver caching (browser/OS/router/provider) and the internet series framing
[[https-tls]] — the certificate check is what catches DNS spoofing
[[latency-and-speed-of-light]] — each lookup is many round-trips, motivating caching
[[dnsmasq]] — combined caching-DNS + DHCP server used in the demos
