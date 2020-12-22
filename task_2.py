# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
         'C': 12, 'D': 13, 'E': 14, 'F': 15}

a = deque(input('первое число: ').upper())
b = deque(input('второ число: ').upper())

if len(a) > len(b):
    for _ in range(len(a) - len(b)):
        b.appendleft('0')
else:
    for _ in range(len(b) - len(a)):
        a.appendleft('0')

summa = deque()
v_ume = 0
a.reverse()
b.reverse()

for i, j in zip(a, b):
    x = (table[i] + table[j] + v_ume) % 16
    for k, v in table.items():
        if x == v:
            summa.appendleft(k)
    v_ume = (table[i] + table[j] + v_ume) // 16

if v_ume != 0:
    for k, v in table.items():
        if v_ume == v:
            summa.appendleft(k)
print(f'сумма чисел: {list(summa)}')

composition = deque()
spam_result = deque()
comp_count = 0
for i in a:
    v_ume2 = 0
    spam_result.clear()
    for j in b:
        spam_result.appendleft((table[i] * table[j] + v_ume2) % 16)
        v_ume2 = (table[i] * table[j] + v_ume2) // 16
    if v_ume2 != 0:
        spam_result.appendleft(v_ume2)

    for _ in range(comp_count):
        spam_result.append(0)
    comp_count += 1

    if len(composition) > len(spam_result):
        for _ in range(len(composition) - len(spam_result)):
            spam_result.appendleft(0)
    else:
        for _ in range(len(spam_result) - len(composition)):
            composition.appendleft(0)
    v_ume3 = 0
    z = 0
    spam_composition = deque()
    composition.reverse()
    spam_result.reverse()
    for x, y in zip(composition, spam_result):
        spam_composition.appendleft((x + y + v_ume3) % 16)
        v_ume3 = (x + y + v_ume3) // 16
    if v_ume3 != 0:
        spam_composition.appendleft(v_ume3)
    composition = spam_composition

for i in enumerate(composition):
    for k, v in table.items():
        if i[1] == v:
            composition[i[0]] = k

print(composition)
