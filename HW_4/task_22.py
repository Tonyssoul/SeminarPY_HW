# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random
n = int(input('Введите колличество элиментов первого массива: '))
m = int(input('Введите колличество элиментов второго массива: '))

lst_1 = [random.randint(-10,10) for i in range(n)]
lst_2 = [random.randint(-10,10) for i in range(m)]
print(lst_1)
print(lst_2)

l_1 = set(lst_1)
l_2 = set(lst_2)
print(l_1)
print(l_2)

l_unite = l_1 & l_2
print(*sorted(l_unite))