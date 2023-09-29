"""
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
"""
n, m = int(input()), int(input())
myArr = [[str(i * j) for j in range(m)] for i in range(n)]
for i in myArr:
    for j in i:
        print(j.ljust(2), end=" ")
    print()
