#Привером взял 5е задание к 3му уроку где необходимо "В массиве найти максимальный отрицательный элемент"
#Так как еще в самом дз к 3му уроку уже написал две возможных реализации.

import cProfile
import timeit
import random

MIN_ITEM = -10
MAX_ITEM = 2

# 1й вариант
def maxSubZero1_1(array):
    min_num = 0
    for i in array:
        if i < min_num:
            min_num = i
    idx = 0
    for id, i in enumerate(array):
        if min_num < i < 0:
            min_num = i
            idx = id
    return idx, min_num

#для сравнения я увиличивал длинну массива передаваемого для обработки
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
print(timeit.timeit('maxSubZero1_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(100)]
print(timeit.timeit('maxSubZero1_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]
print(timeit.timeit('maxSubZero1_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10000)]
print(timeit.timeit('maxSubZero1_1(array)', number=1000, globals=globals()))
# при длине массива 10
# 0.0031768000000000005
# длина массива 100
# 0.021392314000000003
# длина массива 1000
# 0.21533847199999998
# длина массива 1000
# 2.3594391889999997



#2й вариант
def maxSubZero2_1(arr):
    x = 0
    idx = - 1
    while x < len(arr):
        if arr[x] < 0 and idx == -1:
            idx = x
        elif arr[idx] < arr[x] < 0:
            idx = x
        x += 1
    return idx, arr[idx]

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
print(timeit.timeit('maxSubZero2_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(100)]
print(timeit.timeit('maxSubZero2_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]
print(timeit.timeit('maxSubZero2_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10000)]
print(timeit.timeit('maxSubZero2_1(array)', number=1000, globals=globals()))

# при длине массива 10
# 0.006143377999999977
# длина массива 100
# 0.05299116200000009
# длина массива 1000
# 0.5704454050000001
# длина массива 10000
# 5.865991767000001

#3й вариант в котором я так ничего и не придумал, кроме как
# модернизировать первый заменив нахождение минимального числа массива встроенной функцией min()
def maxSubZero3_1(array):
    min_num = min(array)
    idx = 0
    for id, i in enumerate(array):
        if min_num < i < 0:
            min_num = i
            idx = id
    return idx, min_num

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10)]
print(timeit.timeit('maxSubZero3_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(100)]
print(timeit.timeit('maxSubZero3_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]
print(timeit.timeit('maxSubZero3_1(array)', number=1000, globals=globals()))
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(10000)]
print(timeit.timeit('maxSubZero3_1(array)', number=1000, globals=globals()))

# длина массива 10
# 0.003150400999999192
# длина массива 100
# 0.019587335999998956
# длина массива 1000
# 0.2061126479999995
# длина массива 10000
# 2.033142969

# Вывод: сложность линейная, время увиличивается примерно в то же колличество раз что и длинна передаваемого
# массива, что и ожидалось. А вот удивило меня то, что 1й и 3й(самый быстрый, само собой) варианты отрабатывают быстрее
# 2го, хотя в них массив перебирается дважды.


# Затем, мне захотелось навести красоту при вызове timeit, чтобы было как на уроке
# три ровных вывода print() и чтобы только одна переменная менялась, потому генерацию массива засунул внутрь самой
# функции. Далее, так же сравнивал увиличивая длинну массива.
def maxSubZero1_2(min_item, max_item, size):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    min_num = 0
    for i in array:
        if i < min_num:
            min_num = i
    idx = 0
    for id, i in enumerate(array):
        if min_num < i < 0:
            min_num = i
            idx = id
    return idx, min_num

print(timeit.timeit('maxSubZero1_2(-10, 2, 10)', number=1000, globals=globals())) # 0.024109557999999254
print(timeit.timeit('maxSubZero1_2(-10, 2, 100)', number=1000, globals=globals())) # 0.21654456100000097
print(timeit.timeit('maxSubZero1_2(-10, 2, 1000)', number=1000, globals=globals())) # 2.198624057


def maxSubZero2_2(min_item, max_item, size):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    x = 0
    idx = - 1
    while x < len(array):
        if array[x] < 0 and idx == -1:
            idx = x
        elif array[idx] < array[x] < 0:
            idx = x
        x += 1
    return idx, array[idx]

print(timeit.timeit('maxSubZero2_2(-10, 2, 10)', number=1000, globals=globals())) # 0.02772684800000036
print(timeit.timeit('maxSubZero2_2(-10, 2, 100)', number=1000, globals=globals())) # 0.24661269799999985
print(timeit.timeit('maxSubZero2_2(-10, 2, 1000)', number=1000, globals=globals())) # 2.5820650389999997


def maxSubZero3_2(min_item, max_item, size):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    min_num = min(array)
    idx = 0
    for id, i in enumerate(array):
        if min_num < i < 0:
            min_num = i
            idx = id
    return idx, min_num

print(timeit.timeit('maxSubZero3_2(-10, 2, 10)', number=1000, globals=globals())) # 0.02452755799999906
print(timeit.timeit('maxSubZero3_2(-10, 2, 100)', number=1000, globals=globals())) # 0.22010758300000077
print(timeit.timeit('maxSubZero3_2(-10, 2, 1000)', number=1000, globals=globals())) # 2.192861034

#Вывод: хорошо что сразу так не сделал. Судя по результатам куда больше времени тратится на создание собственно
# массива, нежели на операцию проводимую с ним в рамках данной фонкции, а зависимость все так же линейная и топ по
# быстродействию все тот же самый быстрый 3й потм 1й и 2й замыкающий


def main():
   arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]
   a = maxSubZero1_1(arr)
   b = maxSubZero2_1(arr)
   c = maxSubZero3_1(arr)

cProfile.run('main()')
"""
         6223 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
     1000    0.003    0.000    0.009    0.000 random.py:200(randrange)
     1000    0.002    0.000    0.011    0.000 random.py:244(randint)
     1000    0.004    0.000    0.006    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 task_1.py:12(maxSubZero1_1)
        1    0.000    0.000    0.016    0.016 task_1.py:165(main)
        1    0.001    0.001    0.013    0.013 task_1.py:166(<listcomp>)
        1    0.002    0.002    0.002    0.002 task_1.py:45(maxSubZero2_1)
        1    0.000    0.000    0.000    0.000 task_1.py:76(maxSubZero3_1)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
     1001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     1000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1213    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
# чуть не забыл про cProfile, тут так же заметно что 2й вариант реализации занимает наибольшее время