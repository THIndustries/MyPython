"""
Обмен диагоналей
"""
matrix = [[int(j) for j in input().split()] for i in range(int(input()))]
n = len(matrix)

for i in range(n):
    matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

for row in matrix:
    print(" ".join(map(str, row)))

















