# Висновки щодо ефективності алгоритмів сортування

У цьому дослідженні порівнювалися три алгоритми сортування:

- **Сортування вставками** (Insertion Sort)
- **Сортування злиттям** (Merge Sort)
- **Timsort** (вбудована функція `sorted()` в Python)

## Результати

- **Insertion Sort** швидко працює лише на маленьких наборах даних. При зростанні обсягу значно гальмує.
- **Merge Sort** показав стабільну продуктивність незалежно від розміру списку.
- **Timsort** перевершив обидва інші алгоритми на всіх тестових наборах, що підтверджує його ефективність.

## Висновок

**Timsort**, як гібридний алгоритм, що поєднує сортування злиттям та вставками, виявився найефективнішим. Це і пояснює, чому саме його використовує Python у функціях `sort()` та `sorted()`.

Для реальних завдань рекомендовано використовувати вбудовані алгоритми Python, адже вони оптимізовані та перевірені роками практики.
