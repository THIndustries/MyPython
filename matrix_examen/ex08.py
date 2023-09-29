"""
Диагонали параллельные главной
"""
n = int(input())
myList = [[0*n] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(abs(i-j), end=" ")
    print()






