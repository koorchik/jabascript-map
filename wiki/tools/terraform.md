---
type: tool
tags: [infrastructure-as-code, devops, cloud]
---
# Terraform

Terraform — стандартний інструмент infrastructure-as-code. На каналі він зʼявляється у звʼязці з конкретним анонсом I/O 2023 ([[google-io-2023-watch-party|watch party Google I/O 2023]]): ресурси Firebase стало можливо описувати в Terraform, тобто infra-as-code нарешті покриває Firebase. Обговорення на watch party далі йде в практику — звʼязок між JSON-конфігом Firebase і HCL, генерація динамічних ресурсів із розпарсеного JSON, і спостереження, що в цій ролі Terraform працює як тонка обгортка над конфігурацією рівня Firebase, а не як глибока абстракція.

## Де розглядається
- [[google-io-2023-watch-party]] — Firebase стає описуваним у Terraform; JSON-конфіг проти HCL, динамічні ресурси з розпарсеного JSON, Terraform як тонка обгортка.

## Повʼязане
[[firebase]] — платформа, на яку націлене нове покриття Terraform.
[[google-cloud-run]] — сусідній шматок Google Cloud у тому самому стеку.
