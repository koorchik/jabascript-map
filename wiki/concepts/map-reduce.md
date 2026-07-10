---
type: concept
tags: [distributed-systems, big-data, search, algorithms]
---
# Map-reduce

Розглядається не як біг-дата-баззворд, а як практичний трюк, що дозволив Вікторові побудувати інвертований індекс на 16,5 млн рядків, не тримаючи 10–15 ГБ у RAM. Він проходить по статті Google про MapReduce 2004 року, Hadoop і Hadoop streaming, а потім демонструє потокову модель звичайними Unix-інструментами: map-крок на Node.js видає пари (token, doc), Unix `sort` грає роль shuffle, а reduce-крок групує postings за токенами. Ті самі скрипти можна запускати на справжньому Hadoop — саме для цього він написав власний npm-модуль `hadoop-streaming-utils` ([[full-text-search-inverted-indexes|відео про інвертовані індекси]]).

## Де розглядається
- [[full-text-search-inverted-indexes]] — увесь розбір: стаття Google 2004 року, Hadoop streaming з map на Node.js і Unix sort у ролі shuffle, а також його модуль hadoop-streaming-utils

## Повʼязане
[[inverted-index]] — артефакт, який продукує цей конвеєр
[[full-text-search]] — задача, яка розв’язується
[[algorithmic-complexity]] — компроміс «пам’ять чи стримінг» у дії
