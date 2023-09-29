"""
Симметричная матрица
"""
n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
print("YES" if matrix[0][0]==matrix[-1][-1] else "NO")








