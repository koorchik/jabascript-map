---
type: tool
tags: [networking, firewall, router, tooling]
---
# pfSense

A FreeBSD-based open-source virtual router and firewall (runs happily in ~512MB RAM with a tiny disk). On the channel it's the main tool for isolating a VirtualBox VM from the home LAN: installed as its own VM with two adapters, it acts as a WAN/LAN router that NATs the guest out to the home network, runs a DHCP server on the internal LAN (handing the guest 10.10.10.50–100, gateway 10.10.10.1, DNS 8.8.8.8), and enforces firewall rules that block the guest's direct access to the home router ([[vm-network-isolation]]).

## Covered in
- [[vm-network-isolation]] — the virtual router/firewall that gates and firewalls the isolated guest VM

## Related
[[nat-and-networking]] — the WAN/LAN NAT topology it implements
[[dhcp]] — runs the legitimate DHCP server on the isolated LAN
[[virtualbox]] — the hypervisor hosting both it and the guest
[[sandboxing-and-isolation]] — the isolation goal it serves
