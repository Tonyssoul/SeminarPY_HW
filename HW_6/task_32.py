# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = int(input('Введите колличество элиментов:'))
one = [random.randint(-10, 10) for i in range(n)]
print(one)
min_num = int(input('Введите начало диапазона: '))
max_num = int(input('Введите введите конец дипазона: '))
for i in range(n):
    if min_num <= one[i] <= max_num:
        print(i, end=" ")

#sorry forgot about work branches