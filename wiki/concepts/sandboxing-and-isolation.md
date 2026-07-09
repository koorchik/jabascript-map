---
type: concept
tags: [security, virtualization, networking]
---
# Sandboxing and isolation

Contain the untrusted thing so that even if it's compromised, it can't reach anything that matters. The channel's hands-on treatment is [[vm-network-isolation]], an unedited screencast triggered by a real concern: VirtualBox's default bridged mode puts a VM directly on the home subnet (192.168.50.x), able to reach every device in the house — which is dangerous when the VM runs untrusted code or AI agents. Viktor's fix is a network sandbox built from another VM: a pfSense virtual router with two adapters — a bridged WAN adapter and an internal-network LAN adapter — with the target Ubuntu VM attached only to the internal network (he also mentions MikroTik CHR and OpenWRT/DD-WRT as alternatives).

The firewall ruleset is the lesson in [[least-privilege]] applied to packets: keep the anti-lockout rule, allow the guest out to the internet, block the guest from the home LAN subnet, and block access to the pfSense admin UI itself. End state: the guest reaches google.com but cannot ping home devices, the home router, or the router's admin page. The whole exercise is framed as defense-in-depth ([[security-practices]]) — assume the sandbox contents are hostile and make the blast radius zero.

## Covered in
- [[vm-network-isolation]] — the full build: why bridged mode is dangerous, pfSense virtual router with WAN + internal-net adapters, and the four firewall rules that let the VM online but keep it off the home LAN

## Related
[[security-practices]] — defense-in-depth: assume compromise, limit reach.
[[least-privilege]] — same principle, applied to network access instead of credentials.
[[nat-and-networking]] — the routing/subnet machinery the sandbox is built from.
