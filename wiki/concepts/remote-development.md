---
type: concept
tags: [tooling, development, remote, vscode]
---
# Remote Development

The channel's take, inspired by Google's "open a URL and you have a dev environment" setups, is that VS Code's process architecture makes remote development almost free ([[vscode-in-the-browser]]). He proves that Remote-SSH secretly installs a `vscode-server` on the target machine (comparing the process list before and after), that extensions split into local vs remote halves (Prettier gets installed on the *server*), that ports auto-forward (a remote `:3000` shows up on `127.0.0.1:3000` locally), and that the debugger works exactly as if it were local. The browser-only variant uses `vscode.dev` plus the standalone `code tunnel` CLI with GitHub device authentication — full development, extensions, port forwarding and debugger, from a bare browser tab. He also maps the wider option space: WSL, Codespaces (the same mechanism, he reckons), and dev containers as "zero-click setup." The reason it all works over NAT and firewalls is that both the browser and the dev server dial *outward* to a proxy that stitches them together, which is why tunnels need a GitHub sign-in.

## Covered in
- [[vscode-in-the-browser]] — Remote-SSH's hidden vscode-server, local/remote extension split, port auto-forwarding, vscode.dev tunnels, WSL/Codespaces/dev containers

## Related
[[language-server-protocol]] — the per-language-process design that made remote agents cheap
[[nat-and-networking]] — outbound-proxy tunnels traversing NAT/firewalls
[[vs-code]] — the editor whose architecture enables all of this
[[ssh-key-authentication]] — how the Remote-SSH connection authenticates
[[sandboxing-and-isolation]] — dev containers as isolated environments
