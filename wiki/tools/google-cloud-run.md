---
type: tool
tags: [cloud, serverless, containers, google]
---
# Google Cloud Run

Cloud Run — serverless-платформа для контейнерів у Google Cloud: приносиш будь-який контейнер і отримуєш scale-to-zero, метрики та CI/CD «у два кліки» — і це буквально продукт, який будувала команда Віктора в Google ([[qa-2-answering-questions]]). Він говорить про нього і як інсайдер, і як задоволений клієнт: переніс усі свої pet-проєкти з DigitalOcean на Cloud Run і виявив, що це «значно дешевше» (пара доларів за маленький сервіс), а ще розкриває, що Cloud Functions v2 під капотом — це буквально контейнер Cloud Run ([[qa-and-plans-for-2024]]). Його порада щодо витрат: не вірте калькулятору запитів — просимулюйте день реального трафіку і помножте на 30. На watch party з I/O 2023 співведучий Микита (теж із команди Cloud Run) додає деталей до пітчу: перевірка підпису образів на етапі деплою, кастомні домени, нарешті інтегровані через Firebase Hosting, і його mytalks.tech, що працює на Cloud Run приблизно втричі дешевше, ніж на DigitalOcean ([[google-io-2023-watch-party]]). У [[qa-2-answering-questions]] Віктор анонсує підтримку GPU — «serverless 2.0» — націлену на inference-навантаження.

Cloud Run — це ще й сцена його найособистішої історії з Google ([[voice-5-why-i-left-google]]): його проєкт Application Canvas дозволяв перетягувати сервіси Cloud Run і бази даних на канву, деплоїти цілі застосунки та зливати архітектури. Спершу він вийшов як «Cloud Run integrations», його показували на кіноутах Google Cloud Next і хвалило топменеджмент — а потім проєкт скасували й видалили, що обнулило його трек на підвищення до L6 і стало однією з причин піти з Google.

## Де розглядається
- [[google-io-2023-watch-party]] — пітч від інсайдерів команди: будь-який контейнер, scale-to-zero, перевірка підписів образів, домени через Firebase Hosting, mytalks.tech утричі дешевше за DigitalOcean.
- [[qa-2-answering-questions]] — «продукт його команди»; анонс підтримки GPU як serverless 2.0 для inference.
- [[qa-and-plans-for-2024]] — pet-проєкти, мігровані з DigitalOcean, Cloud Functions v2 = контейнер Cloud Run, оцінка витрат через симуляцію трафіку.
- [[voice-5-why-i-left-google]] — історія злету і скасування Application Canvas, що обнулила його promo.

## Повʼязане
[[firebase]] — прошарок без бекенду, що маршрутизує і хостить поверх Cloud Run.
[[docker]] — формат контейнерів, який споживає Cloud Run.
[[terraform]] — той самий стек Google з боку infrastructure-as-code.
[[career-and-growth]] — історія Application Canvas як карʼєрний урок про великі компанії.
