#В массиве найти максимальный отрицательный элемент.
#Вывести на экран его значение и позицию в массиве

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 2
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_num = 0
for i in array:
    if i < min_num:
        min_num = i

idx = 0
for id, i in enumerate(array):
    if min_num < i < 0:
        min_num = i
        idx = id
print(f'максимальный отрицательный элемент: {min_num} его позиция {idx + 1}')
#не уверен на счет термина "позиция",
#потому в выводе к индексу еденицу прибавил, чтобы было логичнее для "человеческого" понимания

#понимая что два перебора для этой задачи это много,
#подглядел в интернетах более оптимальное решение.
#своими руками его переписал, логику действий понял

i = 0
idx = - 1
while i < len(array):
    if array[i] < 0 and idx == -1:
        idx = i
    elif array[idx] < array[i] < 0:
        idx = i
    i += 1
print(f'максимальный отрицательный элемент: {array[idx]} его позиция {idx + 1}')
