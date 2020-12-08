#Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = array[0]
max_cnt = 1
for i in range(len(array) - 1):
    cnt = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            cnt +=1
    if cnt > max_cnt:
        max_cnt = cnt
        num = array[i]

print(f'чаще всего встречается {num} \n{max_cnt} раз(а)')