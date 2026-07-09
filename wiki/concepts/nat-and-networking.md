---
type: concept
tags: [networking, internet, nat, tcp-udp]
---
# NAT and Networking Fundamentals

This is the connective tissue of the channel's "How the Internet works" series — the plumbing that the DNS, DHCP and latency episodes all sit on top of. The opening episode contrasts TCP and UDP: the TCP handshake (SYN / SYN-ACK / ACK) and its recurring ACKs are the price of reliability, while UDP skips them ([[speed-of-light-website-latency]]). The DHCP episode explains why a device with no settings *must* use UDP broadcast rather than TCP — you can't complete a handshake before you have an address — and why broadcasts stay inside the LAN ([[dhcp-cafe-wifi]]).

On addressing and resolution, he stresses that the resolver you actually query (your provider, your home router's cache, or 8.8.8.8) is almost never the authoritative server where you added the record ([[dns-recursive-resolution]]), and that caching is layered across the browser, OS, router and provider. He mentions Dynamic DNS as the trick for reaching a home machine on a changing IP ([[how-dns-works-basics]]). NAT itself gets a hands-on treatment in the VM-isolation build: he contrasts VirtualBox's bridged vs NAT vs internal-network adapter modes and constructs a two-interface WAN/LAN router topology that NATs the guest out to the home network ([[vm-network-isolation]]). The same NAT-traversal idea explains VS Code tunnels — both the browser and the dev server connect *outward* to a proxy (he believes over WebSockets) that stitches them together, so both ends can sit behind NAT and firewalls and it still works ([[vscode-in-the-browser]]).

## Covered in
- [[speed-of-light-website-latency]] — TCP handshake vs UDP, ACKs as the reliability cost
- [[how-dns-works-basics]] — where the resolver address comes from, layered caching, Dynamic DNS
- [[dns-recursive-resolution]] — the resolver you query vs the authoritative server
- [[dhcp-cafe-wifi]] — why bootstrapping needs UDP broadcast, broadcasts stay in the LAN
- [[vm-network-isolation]] — VirtualBox bridged/NAT/internal modes, WAN/LAN router with NAT
- [[vscode-in-the-browser]] — outbound-proxy tunnels traversing NAT and firewalls

## Related
[[dns]] — name resolution layered over this plumbing
[[dhcp]] — how a device bootstraps onto the network
[[latency-and-speed-of-light]] — round-trips are what the handshakes cost you
[[https-tls]] — another handshake stacked on top of TCP
[[virtualbox]] — provides the adapter modes demonstrated
[[pfsense]] — the virtual router doing the NAT
