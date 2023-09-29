"""
Побочная диагональ
"""
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][n - 1 - i] = 1
    for j in range(n):
        if (i >= j and i > n - 1 - j) or (i <= j and i > n - 1 - j):
            matrix[i][j] = 2

# Вывод матрицы
for row in matrix:
    print(*row)
