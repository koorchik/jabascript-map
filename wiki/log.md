# Log

Append-only record of wiki operations. Entry format: `## [YYYY-MM-DD] ingest|query|lint | Title`.

## [2026-07-09] ingest | Initial batch: all 40 channel videos

Bootstrapped the wiki from the full back-catalog of jabascript video subtitles
(`raw/*.uk.vtt`, Ukrainian tracks, cleaned into `transcripts/`). Created:

- 40 video pages
- 54 concept pages (hubs)
- 36 tool pages
- 37 book pages
- 6 cluster MOCs, plus `overview.md` and `index.md`

Notable naming decisions: the isolation concept is `sandboxing-and-isolation`
(the video slug `vm-network-isolation` was already taken); GoF book is
`design-patterns-gof` (concept owns `design-patterns`); DDD lives as a book
page only; Node.js slug is `nodejs`.

## [2026-07-09] lint | Post-ingest link check

Ran `scripts/lint_wiki.py` after the batch ingest; fixed broken links and
orphans found. See git history for details.

## [2026-07-10] update | Розділи (chapters) + рівні складності для всіх 40 відео

Додано часову розмітку: `scripts/vtt_to_timed.py` генерує
`transcripts/timed/<youtube_id>.uk.txt` з маркерами `[m:ss]` кожні ~20 с;
на їх основі у кожній відеосторінці зʼявився `## Розділи` (506 розділів
загалом; кожен час скопійовано з маркера таймованого транскрипту) та
frontmatter-поле `level:` (18 beginner / 18 intermediate / 4 advanced).
На всіх 6 кластерах стандартизовано `## Відео (порядок перегляду)`.

## [2026-07-10] update | Переклад усієї вікі українською

За рішенням користувача вікі повністю переведено на українську (173 сторінки:
відео, концепції, інструменти, книги, кластери, overview). Слаґи файлів,
frontmatter, теги й цілі wikilink-ів не змінювалися; заголовки секцій
перейменовано (`## Головне`, `## Розділи`, `## Теми`, `## Де розглядається`,
`## Повʼязане`). Назви книжок лишаються англійською. Конвенції оновлено в
CLAUDE.md; index.md перегенеровано; lint — 0 битих посилань.

## [2026-07-10] build | Сайт-навігатор website/ (українською)

`scripts/build_website.py` генерує статичний сайт: 6 треків з кроками
перегляду, 38 відеосторінок із вбудованим плеєром і клікабельними розділами
(deep-links на хвилину YouTube), бібліотека тем, книжкова полиця, мапа знань
(SVG-граф концепцій зі звʼязками) на головній. Два застарілі стріми
(google-io-2023-watch-party, qa-and-plans-for-2024) виключено з сайту
(константа `EXCLUDED`); у вікі вони лишаються. Збірка: 137 сторінок,
0 попереджень.
