---
type: concept
tags: [security, access-control, best-practices]
---
# Least privilege

Scope credentials to the task — the channel teaches this through one unforgettable war story from WebbyLab's early days ([[voice-1-admin-keys-for-developers]]). The team needed a Redmine API key for a reporting script and debated: admin key or normal key? They chose admin — "nothing bad will happen." Later a developer copy-pasted example code from a GitHub library's README, which happened to demonstrate the API by deleting user #2, renaming user #5, and so on. The result: co-founder Anton Morozov's account was deleted, and a Ukrainian client named Oleksandr was renamed to "Raul." The damage surfaced gradually over days — lost logins, mysteriously renamed client records.

The moral Viktor draws: you don't need a malicious actor for elevated rights to hurt you. Even honest, non-malicious, copy-pasted code is dangerous when it runs with more permissions than the job requires. A read-only reporting key would have made the whole incident impossible.

## Covered in
- [[voice-1-admin-keys-for-developers]] — the core lesson and the full "Raul" story: admin Redmine key + copy-pasted example code = deleted co-founder and renamed client

## Related
[[security-practices]] — least privilege as a pillar of defense-in-depth.
[[social-engineering]] — the same root cause (misplaced trust and convenience), with a human instead of a script.
[[sandboxing-and-isolation]] — the network-level analogue: give the VM internet, not the whole home LAN.
