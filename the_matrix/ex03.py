"""
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки.
"""
myArr = [[int(j) for j in input().split()] for i in range(int(input()))]
res = [[sum(1 for j in i if j > sum(i) / len(i))]for i in myArr]
print('\n'.join(map(str, res)))



