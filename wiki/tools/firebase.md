---
type: tool
tags: [cloud, backend-as-a-service, google]
---
# Firebase

Firebase — платформа Google для застосунків без власного бекенда; на каналі вона розкрита через watch party по I/O 2023, де співведучий Микита Галкін проводить екскурсію ([[google-io-2023-watch-party]]). Ключова рамка: Firebase сидить поверх Google Cloud з одним білінговим акаунтом і спільним проєктом, тож він компонується з рештою стека, а не живе у власному силосі. Найцікавіше з екскурсії: preview-канали Hosting на кожен pull request; rewrites у Hosting, які маршрутизують шляхи `/api` прямо в сервіси Cloud Run (отримуєш безкоштовний кастомний домен і сертифікати для контейнерів); два режими Firestore і realtime-синхронізація; маркетплейс Extensions (платежі Stripe, email тощо); і відкриття, що Cloud Functions тепер під капотом побудовані на контейнерах Cloud Run.

## Де розглядається
- [[google-io-2023-watch-party]] — повна екскурсія: preview-канали, rewrites у Cloud Run, режими Firestore, маркетплейс Extensions, Functions поверх Cloud Run.

## Повʼязане
[[google-cloud-run|Google Cloud Run]] — контейнерна платформа, куди маршрутизує Firebase Hosting і на якій працюють Functions.
[[terraform|Terraform]] — після I/O 2023 ресурси Firebase можна описувати в Terraform.
