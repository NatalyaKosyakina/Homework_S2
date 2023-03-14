# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("ВВедите число N: "))

count = 0
result = 1
while result < number :
    result = 2**count
    count += 1
    if result >= number :
        break
    print(result)