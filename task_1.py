import random
from sum_memory import sum_memory

MIN_ITEM = -10
MAX_ITEM = 2

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
#array = [-5, -6, -10, -2, -9, -5, -1, 2, 2, 1]
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


print(f'[{idx}][{min_num}]')
print(sum_memory(locals()))
