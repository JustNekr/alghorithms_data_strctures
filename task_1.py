abc = int(input("Введите трехзначное число: "))
a = abc // 100
b = (abc - a * 100) // 10
c = abc - a * 100 - b * 10
d = a + b + c
abc = a*b*c

print(f'сумма равна: {d} \nпроизведение равно: {abc}')

