"""
Максимум в таблице
"""
n, m = int(input()), int(input())
myArr = [[int(j) for j in input().split()] for i in range(n)]

myMax = []
temp = myArr[0][0]
for i in range(n):
    for j in range(m):
        if myArr[i][j] > temp:
            temp = myArr[i][j]
            myMax = [i, j]
print(*myMax) if len(myMax) > 0 else print(0, 0)