import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Алгоритм сортування злиттям
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Підготовка даних
sizes = [100, 1000, 5000]
results = []

for size in sizes:
    lst = [random.randint(0, 10000) for _ in range(size)]
    setup = f"""
from __main__ import insertion_sort, merge_sort, lst
import random
lst = {lst}
"""
    
    time_insertion = timeit.timeit("insertion_sort(lst[:])", setup=setup, number=1)
    time_merge = timeit.timeit("merge_sort(lst[:])", setup=setup, number=1)
    time_timsort = timeit.timeit("sorted(lst)", setup=setup, number=1)

    results.append((size, time_insertion, time_merge, time_timsort))

for size, t1, t2, t3 in results:
    print(f"Розмір: {size} | Вставками: {t1:.5f} сек | Злиттям: {t2:.5f} сек | Timsort: {t3:.5f} сек")
