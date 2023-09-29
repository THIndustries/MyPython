"""
Напишите программу, которая вычисляет сумму элементов:
 верхней четверти; правой четверти; нижней четверти; левой четверти.
"""

myArr = [[int(j) for j in input().split()] for i in range(int(input()))]
print("Верхняя четверть:", sum([myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
        if i < j and (i < len(myArr) - 1 - j)]))

print("Правая четверть:", sum([myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
        if i < j and (i > len(myArr) - 1 - j)]))

print("Нижняя четверть:", sum([myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
        if i > j and (i > len(myArr) - 1 - j)]))

print("Левая четверть:", sum([myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
        if i > j and (i < len(myArr) - 1 - j)]))


