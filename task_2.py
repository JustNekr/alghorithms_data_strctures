# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

size = 10
MAX = 50
array = [round(random.random() * MAX, 2) for _ in range(size)]
print(f'Исходный массив: {array}')


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    lt_idx = 0
    rt_idx = 0
    arr = []
    while lt_idx < len(left) or rt_idx < len(right):
        if lt_idx == len(left):
            arr.append(right[rt_idx])
            rt_idx += 1
        elif rt_idx == len(right):
            arr.append(left[lt_idx])
            lt_idx += 1
        elif left[lt_idx] < right[rt_idx]:
            arr.append(left[lt_idx])
            lt_idx += 1
        else:
            arr.append(right[rt_idx])
            rt_idx += 1
    return arr


merge_sort(array)
print(f'Отсортированный массив: {merge_sort(array)}')

# не могу взять в толк, почему в первой задаче с пузырьковой сортировкой
# моя функция изменяла сам входящий массив
# а тут функция не меняет его, а только выдает результат сама никуда его не сохраняя
