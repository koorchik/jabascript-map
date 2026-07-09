---
type: tool
tags: [javascript, backend, runtime]
---
# Node.js

Node.js is the server-side JavaScript runtime and the channel's default backend platform. Viktor's recommendation is unambiguous: for backend learners he picks Node.js over Bun — it's the standard environment, has far more documentation and Stack Overflow answers, and LLMs know it much better ([[qa-and-plans-for-2024]]). His stack of choice for a new product would be a Node backend + JS frontend + React Native mobile, so the whole team shares one language, and he specifically praises how easy Node makes async work and WebSockets.

He also uses Node's standard `crypto` module as his teaching lab: all the runnable demos in the asymmetric-encryption video — RSA sign/verify and encrypt/decrypt, elliptic-curve signatures, AES-256-CBC — are plain Node scripts posted on GitHub, with the practical warning that `Math.random()` is insecure and cryptographic randomness must come from `crypto.getRandomValues` ([[asymmetric-encryption-digital-signatures]]).

## Covered in
- [[asymmetric-encryption-digital-signatures]] — Node's built-in `crypto` module powers every demo (RSA, ECC signatures, AES-256-CBC); Math.random() is not a source of secure randomness.
- [[qa-and-plans-for-2024]] — Node over Bun for learners; Node backend + JS frontend + React Native as his one-language stack; async/WebSocket ergonomics.

## Related
[[react]] — the frontend half of his one-language JS stack.
[[nextjs]] — the Node-based SSR framework his pet project runs on.
[[security-practices]] — the crypto-module demos illustrate the channel's security material.
