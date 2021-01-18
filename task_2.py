import random
from sum_memory import sum_memory

MIN_ITEM = -10
MAX_ITEM = 2

# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
array = [-5, -6, -10, -2, -9, -5, -1, 2, 2, 1]
print(array)

x = 0
idx = - 1
while x < len(array):
    if array[x] < 0 and idx == -1:
        idx = x
    elif array[idx] < array[x] < 0:
        idx = x
    x += 1
print(f'[{idx}][{array[idx]}]')

print(sum_memory(locals()))

