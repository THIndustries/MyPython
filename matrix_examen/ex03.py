"""
Транспонирование матрицы
"""
n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(arr[j][i], end=" ")
    print()



