"""
Напишите программу, которая меняет местами столбцы в матрице.
"""
n, m = int(input()), int(input())
myList = [[int(j) for j in input().split()] for b in range(n)]
i, j = map(int, input().split())

for row in range(n):
    myList[row][i], myList[row][j] = myList[row][j], myList[row][i]
    print(*myList[row])
