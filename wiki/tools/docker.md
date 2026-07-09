---
type: tool
tags: [containers, infrastructure, isolation]
---
# Docker

Docker is the standard containerization tool, and on the channel it serves as the flagship example of why deep understanding beats surface knowledge. Viktor's take on the perennial complaint that "Docker is 2x slower on macOS" ([[3-things-that-make-a-programmer-better]]): it's not a bug but a feature of the architecture. Containers don't actually exist even in Linux — they are an abstraction over kernel isolation subsystems — and on macOS there is a Linux VM running underneath Docker, so every syscall crosses two kernels. Once you understand how things really work, the "mystery" performance penalty is obvious and expected.

## Covered in
- [[3-things-that-make-a-programmer-better]] — the macOS 2x slowdown explained: containers as a kernel-isolation abstraction, plus a VM layer on macOS.

## Related
[[deep-learning-of-fundamentals]] — the Docker story is the channel's canonical "know how it works underneath" example.
[[sandboxing-and-isolation]] — the kernel mechanisms containers are built from.
[[abstractions]] — "container" as an abstraction with a leaky performance cost.
[[google-cloud-run]] — where his containers actually run in production.
