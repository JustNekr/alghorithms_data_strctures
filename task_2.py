# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import cProfile
import timeit

def sieve(n):
    a = [0] * n**2 # не могу ничем кроме как интуицией обусловить выбор ограничения списка для просеивания как n в
    # квадрате :-( но проверял на весьма крупных значениях и все работает
    for i in range(n**2):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n**2:
        if a[m] != 0:
            j = m * 2
            while j < n**2:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for k in a:
        if k != 0:
            b.append(k)
    return b[n - 1]

print(sieve(10))


def prime(n):
    if n == 1:
        return 2
    else:
        i = 1
        j = 2
        while i < n:
            j += 1
            d = 2
            while d * d <= j and j % d != 0:
                d += 1
            if d * d > j:
                i += 1
        return j

print(prime(3))

print(timeit.timeit('sieve(5)', number=100, globals=globals())) #0.0037175109999999997
print(timeit.timeit('sieve(10)', number=100, globals=globals())) #0.016563068
print(timeit.timeit('sieve(20)', number=100, globals=globals())) #0.075861877
print(timeit.timeit('sieve(50)', number=100, globals=globals())) #0.5279018010000001
print(timeit.timeit('sieve(100)', number=100, globals=globals())) #2.2381961949999996



print(timeit.timeit('prime(5)', number=100, globals=globals()))  # 0.0005910669999997786
print(timeit.timeit('prime(10)', number=100, globals=globals())) # 0.0018783110000000214
print(timeit.timeit('prime(20)', number=100, globals=globals())) # 0.006110623000000093
print(timeit.timeit('prime(50)', number=100, globals=globals())) # 0.02633840300000001
print(timeit.timeit('prime(100)', number=100, globals=globals())) # 0.07711734299999984

def main():
   a = sieve(100)
   b = prime(100)

cProfile.run('main()')
'''
      1235 function calls in 0.025 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_2.py:30(prime)
        1    0.000    0.000    0.025    0.025 task_2.py:61(main)
        1    0.023    0.023    0.024    0.024 task_2.py:7(sieve)
        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
     1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# к сожалению, каких-то глубоких выводов на основании полученных данных у меня сделать не получается. Но похоже что
# мой алгоритм с приминением решета имеет квадратичную сложность ибо увеличивая n в двара раз время увеличивается
# примерно в четыре раза. без решета же, при увеличении n в два раза время выполнения увеличивается примерно в три.
# Ну и соответственно с решетом все в разы дольше вычисляется, хотя возможно дело в моей реализации... как-то так :(

#посмотрел список простых чисел до пятисотого. если смотреть в этих пределах, то можно ограничить просеиваемый список
# n*10 вместо n**2

def sieve2(n):
    a = [0] * n*10
    for i in range(n*10):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n*10:
        if a[m] != 0:
            j = m * 2
            while j < n*10:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for k in a:
        if k != 0:
            b.append(k)
    return b[n - 1]

print(sieve2(10))

print(timeit.timeit('sieve2(5)', number=100, globals=globals())) #0.004183910999999707
print(timeit.timeit('sieve2(10)', number=100, globals=globals())) #0.008427956999999875
print(timeit.timeit('sieve2(20)', number=100, globals=globals())) #0.016767913000000245
print(timeit.timeit('sieve2(50)', number=100, globals=globals())) #0.05724742900000024
print(timeit.timeit('sieve2(100)', number=100, globals=globals())) #0.11346183700000001

# это в разы ускорило время выполнения и так же явно соркащает используемую память. Но что-то мне подсказывает что
# при бесконечном увеличении n в итоге алгоритм перестанет работать корректно. опять же мои познания в простых числах
# не столь велики



