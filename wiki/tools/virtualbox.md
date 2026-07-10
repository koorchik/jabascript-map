---
type: tool
tags: [virtualization, hypervisor, tooling]
---
# VirtualBox

Десктопний гіпервізор. На каналі це хост для збірки з ізоляцією VM: у ньому він запускає і гостьову віртуалку, і роутер-VM з pfSense, а режими мережевих адаптерів bridged / NAT / internal network демонструє як сам механізм ізоляції — гостьова система маршрутизується через pfSense у внутрішній мережі й не може гуляти домашньою LAN ([[vm-network-isolation|мережева ізоляція VM]]).

## Де розглядається
- [[vm-network-isolation]] — хостовий гіпервізор; режими адаптерів bridged/NAT/internal network як механізм ізоляції

## Повʼязане
[[nat-and-networking]] — режими адаптерів напряму лягають на мережеві концепції
[[pfsense]] — роутер-VM, яку він хостить
[[sandboxing-and-isolation]] — мета ізоляції
