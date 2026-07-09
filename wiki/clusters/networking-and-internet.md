---
type: cluster
tags: [networking, internet, cluster, moc]
---
# Networking and the Internet

This cluster gathers the channel's "How the Internet works" material — a deliberate multi-part series in which Viktor rebuilds the internet's plumbing from first principles and, characteristically, proves every claim live with `dig`, Wireshark, real cloud servers and small tools. The through-line is that the abstractions we take for granted (a URL resolving, a page loading "fast," a padlock meaning "safe") hide layers of round-trips, hierarchies and trust assumptions that mostly hold — until someone on your café Wi-Fi decides they don't. The series spans name resolution ([[dns]]), how a device joins a network ([[dhcp]]), the underlying transport and address translation ([[nat-and-networking]]), the physics that caps speed ([[latency-and-speed-of-light]]), and the trust layer on top ([[https-tls]]) — with side-trips into remote development and browser capabilities.

## Concepts
- [[dns]] — name resolution: hosts.txt history, record types, recursive resolution, UDP→TCP, TTL
- [[dhcp]] — how a device bootstraps onto a network, and the rogue-server attack
- [[nat-and-networking]] — TCP vs UDP, handshakes, address translation, the internet-series framing
- [[latency-and-speed-of-light]] — physics as the hard floor on website speed
- [[https-tls]] — what HTTPS actually guarantees (and what it doesn't)
- [[web-performance]] — Core Web Vitals and where they do/don't matter
- [[webgpu]] — direct GPU compute in the browser
- [[remote-development]] — full dev environments over SSH and in the browser
- [[language-server-protocol]] — the editor architecture that made remote dev cheap

## Videos
- [[how-dns-works-basics]] — DNS part 1: hosts.txt, record types, DoH, the UDP-to-TCP-at-512-bytes gotcha
- [[dns-recursive-resolution]] — DNS part 2: root→TLD→authoritative, proven by hand with dig
- [[dhcp-cafe-wifi]] — DHCP explained via a café-Wi-Fi rogue-server attack, built live with dnsmasq
- [[speed-of-light-website-latency]] — how the speed of light and TCP/TLS handshakes bloat a 20ms backend into ~420ms
- [[vm-network-isolation]] — isolating a VirtualBox VM from the home LAN via a pfSense router
- [[vscode-in-the-browser]] — full remote development over SSH and vscode.dev tunnels
- [[bloom-filter-and-firefox]] — certificate revocation and Firefox's CRLite cascade filters
- [[qa-1-will-https-protect-you]] — the ways HTTPS fails on a hostile network
- [[google-io-2023-watch-party]] — Chrome dropping the padlock, WebGPU, Core Web Vitals

## Tools
- [[dnsmasq]] — tiny DNS+DHCP server used to build the rogue-Wi-Fi demo
- [[pfsense]] — open-source virtual router/firewall for VM network isolation
- [[virtualbox]] — hypervisor whose adapter modes drive the isolation demo
- [[nginx]] — the LA test server for measuring real request latency
- [[firefox]] — DNS-timing dev tools and the CRLite revocation story
