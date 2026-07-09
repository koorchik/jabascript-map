---
type: tool
tags: [editor, tooling, remote-development]
---
# VS Code

VS Code is Microsoft's code editor, and the channel treats it less as a tool tip and more as an architecture case study. The dedicated deep-dive ([[vscode-in-the-browser]]) traces the whole lineage — the Monaco editor born in the browser in 2011, the Electron desktop app, the split into a separate extension process, and why full browser support only landed in 2020 (the core first had to shed its Node.js API dependencies) — then demos complete remote development against his Google Cloud server via Remote-SSH and vscode.dev tunnels: extensions, port forwarding and the debugger all running from a bare browser. In [[vibe-coding-part-2]] Monaco doubles as his favorite performance lesson: VS Code won and Atom lost because its authors deliberately rejected general-purpose web frameworks in favor of a specialized text-rendering engine.

Personally, though, he admits VS Code is his streaming tool more than his daily driver — normally he works from a Quake-style dropdown terminal (Yakuake/iTerm2) and dev containers with Claude installed via `postCreateCommand` ([[vibe-coding-new-project]]). He also notes that Google's internal code editor is now built on VS Code, evidence for his point that Google skills transfer because the toolchain converges on common technology ([[voice-5-why-i-left-google]]).

## Covered in
- [[vscode-in-the-browser]] — the full deep dive: Monaco-to-Electron history, the extension process, and hands-on Remote-SSH and vscode.dev tunnel setups.
- [[vibe-coding-part-2]] — the Monaco performance story: a specialized text-rendering engine over generic frameworks is why VS Code beat Atom.
- [[vibe-coding-new-project]] — used on stream for convenience; his real setup is a dropdown terminal plus dev containers.
- [[voice-5-why-i-left-google]] — Google's internal editor now builds on VS Code; internal toolchains converge on common tech.

## Related
[[remote-development]] — the concept the browser-VS-Code video is really about.
[[language-server-protocol]] — the protocol ecosystem that grew out of VS Code's architecture.
[[claude-code]] — installed into his dev containers alongside the editor.
[[web-performance]] — the Monaco lesson in deliberate performance engineering.
