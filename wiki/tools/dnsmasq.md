---
type: tool
tags: [networking, dns, dhcp, tooling]
---
# dnsmasq

A tiny combined caching-DNS + DHCP server. On the channel it's the central demo tool for the café-Wi-Fi episode: with roughly five config lines he sets an upstream resolver (8.8.8.8), a domain override, a `dhcp-range`, and `option:router` / `option:dns-server` pointing at his own machine — enough to stand up a rogue DHCP server that hands victims a poisoned DNS and reroutes name resolution, watched live in Wireshark ([[dhcp-cafe-wifi]]).

## Covered in
- [[dhcp-cafe-wifi]] — used to build the rogue DHCP+DNS server and spoof itquiz.com on a victim tablet

## Related
[[dhcp]] — the protocol it serves in the demo
[[dns]] — the resolution it poisons
[[pfsense]] — a heavier router alternative used in the VM-isolation episode
