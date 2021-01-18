# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

array = [15.38, 6.06, 25.58, 12.29, 45.58, 30.62, 15.29]

array2 = [79, -9, 30, 67, 44, 93, 30, 10, 10, 10, 10]

# пытался без сортировуи, не додумался
# def median(arr):
#     for i in arr:
#         bigger = 0
#         smaller = 0
#         equal = 0
#         for j in range(len(arr)):
#             if arr[j] > i:
#                 bigger += 1
#             elif arr[j] < i:
#                 smaller +=1
#             else:
#                 equal += 1
#         if bigger > smaller:
#             if ((equal - (bigger - smaller)) - 1) // 2 == 0:
#                 return i
#         else:
#             if ((equal - (smaller - bigger)) - 1) // 2 == 0:
#                 return i
#
#
#
# в итоге взял Гномью сортировку


def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i +=1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


print(f'******* исходный: {array} \nпосле сортировки: {gnome_sort(array)} \nмедиана: {array[len(array) // 2]}')
print(f'******* исходный: {array2} \nпосле сортировки: {gnome_sort(array2)} \nмедиана: {array2[len(array2) // 2]}')
