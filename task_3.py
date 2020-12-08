#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 8
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_idx = 0
max_idx = 0
for i in range(len(array)):
    if array[i] < array[min_idx]:
        min_idx = i
    elif array[i] > array[max_idx]:
        max_idx = i
# tmp = array[min_idx]
# array[min_idx] = array[max_idx]
# array[max_idx] = tmp
array[max_idx], array[min_idx] = array[min_idx], array[max_idx] #сначала забыл что так можно

print(array)
