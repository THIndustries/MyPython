"""
Латинский квадрат
"""

n = int(input())
base = [i for i in range(1, n+1)]
matrix = [[int(j) for j in input().split()] for i in range(n)]
isGood = True
for i in matrix:
    if sorted(i) != base:
        isGood = False
        break
for col in zip(*matrix):
    if sorted(col)!= base:
        isGood = False
print("YES" if isGood else "NO")

