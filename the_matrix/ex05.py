"""
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
"""
myArr = [[int(j) for j in input().split()] for i in range(int(input()))]
resArr = [myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr)) if (i == j)
          or (i > j and i <= len(myArr) - 1 - j) or (i < j and i >= len(myArr) - 1 - j)]
print(max(resArr))
