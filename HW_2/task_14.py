# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input("Введите число n: "))
k = 1

while 2 ** k < n:
    print(2 ** k, end = ';')
    k += 1