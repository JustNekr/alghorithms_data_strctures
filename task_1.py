# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter

compCount = int(input('сколько предприятий анализируем: '))
compAnalyzer = Counter()

i = 0

while i < compCount:
    name = input(f'название {i+1} предприятия: ')
    for j in range(4):
        compAnalyzer[name] += float(input(f'введите прибыль за {j + 1} квартал предприятя {name}: '))
    i += 1


for key, value in compAnalyzer.most_common():
    compAnalyzer['avg'] += value

compAnalyzer['avg'] = compAnalyzer['avg'] / compCount

print('Предприятия с прибылью выше среднего: ')
for key, value in compAnalyzer.most_common():
    if key == 'avg':
        print('Предприятия с прибылью ниже среднего:')
    elif value == compAnalyzer['avg']:
        print(f'прибыль предприятия {key} идентична средней.')
    else:
        print(key)


