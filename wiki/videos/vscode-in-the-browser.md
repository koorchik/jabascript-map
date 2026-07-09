---
type: video
title_uk: "Як налаштувати повноцінну розробку в Visual Studio Code в браузері？"
youtube_id: VtKjgQLgus0
tags: [vs-code, remote-development, tooling, architecture]
date_ingested: 2026-07-09
---
# How to Set Up Full Development in VS Code in the Browser

> Original: "Як налаштувати повноцінну розробку в Visual Studio Code в браузері？" — https://youtu.be/VtKjgQLgus0

When the author joined Google, what struck him was how fast you can spin up a project: open a browser, open a URL — and you have a full code editor; nothing on your laptop but a browser. This video is his attempt to recreate that outside Google using [[vs-code]]. He structures it in three parts: first the architecture history of VS Code (why its multi-process design made remote development almost free), then a live demo of [[remote-development|remote development]] over SSH against a real server he spun up in Google Cloud, then the fully-in-browser setup via vscode.dev and tunnels — ending with working extensions, terminal, port forwarding and a step-through debugger, all from a bare browser.

## Key takeaways
- VS Code's history explains its remote powers: it began (~2011) as the Monaco web editor (still embeddable in your own apps today), moved onto Electron (Node.js APIs + browser APIs, UI in HTML/CSS), and when plugins were added they were deliberately put in a *separate process* talking to the core — for fast startup and stability.
- To support many languages, Microsoft added [[language-server-protocol|language servers]]: yet another separate process per language, speaking JSON-RPC over the Language Server Protocol. So the editor was already core + extension-host + language-server processes.
- Windows Subsystem for Linux forced the next step: run the UI on Windows but the code/processes in Linux. Since extensions were already a separate process, the solution was an *agent* (with its own extensions and language servers) that the core talks to — and an SSH agent is barely different from a local one. Pure-browser support was hardest (the core had to drop all Node.js API dependencies) and only landed in 2020.
- SSH demo: with the Remote-SSH extension, connecting to a host makes VS Code silently *install its own vscode-server on the remote machine* — he proves it by showing no processes before connect and a running VS Code server plus `~/.vscode-server` directory after.
- Everything then works "as if local": the terminal is remote, ports are auto-forwarded (his Node.js hello-world on remote port 3000 opens on 127.0.0.1:3000 locally), and extensions are split into "local" and "remote" — he installs Prettier *onto the server*, and format-on-save plus breakpoint debugging just work.
- Browser-only setup: go to vscode.dev, sign in with GitHub, then on the server download the standalone VS Code CLI binary and run `code tunnel`; authorize once via the github.com/login/device code, name the machine, and you get a vscode.dev tunnel URL usable from any machine.
- Why GitHub sign-in is needed: you don't connect to your server directly — both your browser and the server connect out to a proxy (he believes over WebSockets), which stitches the tunnel together. That's why it works even when both ends sit behind [[nat-and-networking|NAT]] and firewalls; the debugged app itself gets a special devtunnels URL instead of localhost.
- His summary of the option space (matching Microsoft's own docs diagram): SSH remoting, WSL, GitHub Codespaces (works the same way as the tunnel setup, he reckons), browser tunnels, and dev containers — the latter he calls especially cool: the app and all extensions run in a container for a zero-click reproducible setup.

## Covered
[[vs-code]], [[remote-development]], [[language-server-protocol]], [[nat-and-networking]]
