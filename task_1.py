# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
import random
size = 10
MIN = -100
MAX = 99
array = [random.randint(MIN, MAX) for _ in range(size)]
print(f'Исходный массив: {array}')
random.random()
# Улучшил добавлением проверки на упорядоченность вводного массива (подглядел в методичке)


def bubble_sort(arr):
    spam = True
    for _ in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                spam = False
        if spam:
            return arr
    return arr


bubble_sort(array)
print(f'Отсортированный массив: {array}')


