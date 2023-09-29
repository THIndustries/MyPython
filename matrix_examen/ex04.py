"""
Снежинка
"""
n = int(input())
arr = [["*" if i == j or i == n - 1 - j or i == n // 2 \
               or j == n // 2 else "." for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()



