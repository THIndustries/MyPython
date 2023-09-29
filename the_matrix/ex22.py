"""
Заполнение диагоналями
"""
n, m = map(int, input().split())  # считываем размеры матрицы
matrix = []  # создаем пустую матрицу
count = 1
for i in range(n):
    temp = []
    for j in range(m):
        if i == j:
            pass

    matrix.append(temp)

# Выводим матрицу
for row in matrix:
    print(*row)  # выводим строки матрицы через пробел












