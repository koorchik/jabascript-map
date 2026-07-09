---
type: tool
tags: [virtualization, hypervisor, tooling]
---
# VirtualBox

Desktop hypervisor. On the channel it's the host for the VM-isolation build: he uses it to run both the guest VM and the pfSense router VM, and demonstrates its bridged vs NAT vs internal-network adapter modes as the actual mechanism for isolation — routing the guest through pfSense on an internal network so it can't roam the home LAN ([[vm-network-isolation]]).

## Covered in
- [[vm-network-isolation]] — host hypervisor; bridged/NAT/internal-network adapter modes as the isolation mechanism

## Related
[[nat-and-networking]] — the adapter modes map directly onto networking concepts
[[pfsense]] — the router VM it hosts
[[sandboxing-and-isolation]] — the isolation goal
