# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random
n = int(input('Введите число эллемнтов Массива: '))
x = int(input('Введите число Х: '))
lst = [random.randint(0, 10) for i in range(n)]
print(lst)
cnt = 0
for i in lst:
    if lst[i] == x:
        cnt += 1

print(cnt)