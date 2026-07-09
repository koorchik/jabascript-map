---
type: concept
tags: [tooling, development, vscode, architecture]
---
# Language Server Protocol (LSP)

The channel introduces LSP as the architectural decision that quietly paid off later ([[vscode-in-the-browser]]). VS Code runs language servers as separate, per-language processes that speak JSON-RPC (the Language Server Protocol) rather than baking every language's intelligence into the editor. Combined with the separate extension-host process, this decoupling is what made remote agents — over SSH, WSL, or the browser — "almost free architecturally": because the smarts already lived in detachable processes talking over a protocol, moving them to another machine was a matter of where you run the process, not a rewrite.

## Covered in
- [[vscode-in-the-browser]] — LSP + the separate extension-host process as the design that made remote development cheap

## Related
[[remote-development]] — the payoff this architecture enables
[[vs-code]] — the editor that popularized LSP
[[abstractions]] — a clean protocol boundary that keeps its promise
