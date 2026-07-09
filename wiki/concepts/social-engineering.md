---
type: concept
tags: [security, social-engineering, scams]
---
# Social engineering

The channel's take: the weakest link is rarely the crypto — it's the human being talked into cooperating. The flagship treatment is [[voice-4-phone-scammers]], where Viktor plays an actual recording of scammers calling him and dissects their script. It opens with a robotic "recorded by order of the National Bank of Ukraine, your card is blocked" message — a framing trick that makes an inbound call feel like something official the victim initiated, so they forget *they* were called. Then a live "operator" named Svitlana escalates trust. He walks through the tells: the bank name silently shifts from National Bank to Oshchadbank, they mention PrivatBank he never named, and simply asking what the purpose of the call is collapses the whole script. The defense he repeats (he recorded the video to warn his parents as much as subscribers): real banks never ask you to say confidential identifiers — PIN, passport data, code word — aloud on a call. Sobering detail: they already knew his name and number, meaning his contact details had leaked into a scam database.

The same manipulation pattern shows up in technical attacks: in [[qa-1-will-https-protect-you]] the rogue-certificate attack only works because the victim is convinced to double-click and install a certificate "to enable the café internet" — the crypto is sound, the human is the exploit. And [[voice-1-admin-keys-for-developers]] shows the adjacent failure mode: no attacker at all, just trust and convenience leading to over-broad access and real damage.

## Covered in
- [[voice-4-phone-scammers]] — a real scam call recorded and dissected: the manufactured-trust script, its tells, and how one question collapses it
- [[qa-1-will-https-protect-you]] — the rogue-certificate attack works by convincing the victim to install a cert to "enable café internet"
- [[voice-1-admin-keys-for-developers]] — the human/process-error cousin: risk born from trust and convenience rather than an attacker

## Related
[[security-practices]] — technical defenses are useless if the human hands over the keys.
[[least-privilege]] — limits the blast radius when trust is misplaced.
[[https-tls]] — a valid padlock means nothing if you installed the attacker's certificate yourself.
