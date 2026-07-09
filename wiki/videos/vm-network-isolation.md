---
type: video
title_uk: "Як не дати віртуальній машині лазити по вашій домашній мережі. (офтоп відео для спонсорів)"
youtube_id: L5Em64f-Qjw
tags: [networking, security, virtualization, homelab, channel-meta]
date_ingested: 2026-07-09
---
# Stopping a VM from Roaming Your Home Network (Sponsors Off-topic)

> Original: "Як не дати віртуальній машині лазити по вашій домашній мережі. (офтоп відео для спонсорів)" — https://youtu.be/L5Em64f-Qjw

The first of the channel's unedited, off-topic videos made specifically for paying sponsors — recorded live without montage, effectively a screen-share hack session. The problem: when you run a VirtualBox VM in **bridged** mode, it gets a real IP from the home router's [[dhcp]] and sits directly on your LAN — so if the VM (or something you run inside it, e.g. untrusted code, an AI model) is compromised, it can scan and reach every device on your home network. NAT mode isolates the VM but the author wants something more deliberate. His solution: put a **virtual router** between the VM and the home LAN and lock it down with firewall rules, so the VM gets internet but cannot touch the home network.

## Key takeaways
- Bridged mode is the danger: the VM appears as just another host on the home subnet (e.g. `192.168.50.x`), fully able to ping and reach home devices. NAT mode hides it, but he wants an explicit, controllable boundary.
- **The architecture:** a second VM acting as a router, with two adapters — a **bridged** adapter as WAN (gets a home-LAN IP via the router's DHCP, provides internet) and an **internal-network** adapter as LAN. The target Ubuntu VM sits only on that internal network, so all its traffic must pass through the virtual router.
- **Tools tried:** he mentions flashing real routers with OpenWRT/DD-WRT historically, and notes ready-made virtual-router images — a MikroTik **Cloud Hosted Router (CHR)** image for VirtualBox (free tier limited to ~1 Mbit, tiny footprint) — but settles on **pfSense** (FreeBSD-based, open source, needs ~512 MB RAM and a small disk). He installs it into a VM, assigns WAN via DHCP and configures the internal LAN interface with a static subnet (e.g. `10.10.10.1/24`) plus its own DHCP range (`10.10.10.50–100`) to hand addresses to the guest VMs.
- The pfSense DHCP server on the internal LAN issues IPs, gateway (`10.10.10.1`), and a DNS server (he set `8.8.8.8`) to the Ubuntu guest.
- **Firewall lockdown (the point of the exercise):** by default he keeps the anti-lockout rule so he doesn't lose admin access, then adds rules to (a) allow the guest out to the internet, (b) **block the guest from reaching the home LAN subnet** (`192.168.x.x`), and (c) block access to the pfSense admin UI itself from the guest. He iterates live in Wireshark/ping, fixing rule-priority mistakes (floating rules), until the end state holds: the Ubuntu guest can reach `google.com` but cannot ping the home router or any home device, and cannot open the pfSense admin page — full isolation with working internet.
- Closing note: future sponsor videos in this rough format may cover experimenting with local neural nets / running Stable Diffusion and Llama on his RTX 3090 (24 GB).

## Covered
[[nat-and-networking]], [[dhcp]], [[dns]], [[security-practices]], [[sandboxing-and-isolation]]
