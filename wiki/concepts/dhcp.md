---
type: concept
tags: [networking, dhcp, internet, security]
---
# DHCP (Dynamic Host Configuration Protocol)

The channel's angle on DHCP is "what's actually wrong with café Wi-Fi?" ([[dhcp-cafe-wifi]]). A device that just joined a network has no settings, so it can't address a request to anyone specific — it UDP-*broadcasts* (IP 255.255.255.255, MAC FF:FF:FF:FF:FF:FF) asking for configuration, and those broadcasts don't cross the router. The server listens on UDP port 67, the client on 68. He walks the DORA exchange (Discover / Offer / Request / Ack), lease times, and the renewal timers T1 (~50%) and T2 (~87.5%) that come from the RFC but are configurable. The security payoff: because *any* machine on the LAN can answer, a rogue DHCP server can hand out a malicious DNS server or default gateway. The attacker wins the race by exhausting the legitimate server's address pool — ~10 fake-MAC Discover requests until the real client is told "no addresses left."

He builds this live with [[dnsmasq]] and Wireshark, and returns to it in Q&A: DHCP starvation is trivial (a ~100-line loop of DHCP requests with random MACs drains 100–10,000 addresses), and manually setting your DNS to 8.8.8.8 doesn't save you — the attacker just hands you a malicious *default gateway* and routes all your traffic through himself ([[qa-1-will-https-protect-you]]). In the VM-isolation build, DHCP appears in a benign role: pfSense runs a DHCP server on the internal LAN handing the guest an IP (10.10.10.50–100), gateway 10.10.10.1, and DNS, while the WAN interface gets its own address from the home router's DHCP ([[vm-network-isolation]]).

## Covered in
- [[dhcp-cafe-wifi]] — full breakdown: broadcast bootstrapping, ports 67/68, DORA, lease/renewal timers, rogue-server + pool-exhaustion attack
- [[how-dns-works-basics]] — named as the source of your DNS server setting
- [[vm-network-isolation]] — pfSense DHCP on the isolated LAN vs WAN address from the home router
- [[qa-1-will-https-protect-you]] — DHCP starvation and the malicious-gateway follow-up

## Related
[[dns]] — the setting most often poisoned via rogue DHCP
[[nat-and-networking]] — why DHCP must broadcast over UDP and stay inside the LAN
[[https-tls]] — the last line of defense once your gateway/DNS are hijacked
[[dnsmasq]] — the tiny DHCP+DNS server used to build the attack
[[pfsense]] — runs the legitimate DHCP server in the VM-isolation setup
