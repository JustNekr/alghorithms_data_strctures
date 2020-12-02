import random

x = int(random.random() * 100)
i = 0
while i < 10:
    y = int(input('введите число от 0 до 100: '))
    if y == x:
        print('вы угадали')
        break
    else:
        if y > x:
            print('ваше число больше загаданного')
        else:
            print('ваше число меньше загаданного')
    i += 1
print(f'это число {x}')

