#Посчитать четные и нечетные цифры введенного натурального числа
num = int(input("введите число: "))
even = 0
odd = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных {even}, нечетных {odd}")

def even_odd ()