"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
"""
myArr = [[int(j) for j in input().split()] for _ in range(int(input()))]
print("YES") if [myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
                 if (i < j and (i <= len(myArr) - 1 - j)) or (i<j and(i > len(myArr) - 1 - j))] \
                == [myArr[i][j] for i in range(len(myArr)) for j in range(len(myArr))
                 if (i > j and (i <= len(myArr) - 1 - j)) or (i>j and(i > len(myArr) - 1 - j))] else \
    print("NO")

is_symmetric = (myArr[i][j] == myArr[j][i] for i in range(n) for j in range(n) if (i < j and i <= n - 1 - j) or (i < j and i > n - 1 - j))




