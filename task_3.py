# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран
num = int(input("введите число: "))
new_num = 0
while num > 0:
    new_num = new_num * 10 + num % 10
    num = num // 10
print(new_num)
#только код не очень корректно будет работать в случае если последней цифрой будет 0
#посему прилагаю решение этой задачи через рекурсию блок-схема будет на странице task_3.2

num = int(input("введите число: "))
def reverse(num):
     if num < 10:
         return f'{num}'
     else:
         return f'{num % 10}{reverse(num // 10)}'

new_num = reverse(num)
print(new_num)