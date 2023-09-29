n = int(input())
myList = [[int(j) for j in input().split()] for i in range(n)]
print(max([myList[i][j] for i in range(n) for j in range(n) if (i >= j and i >= n - 1 - j) \
           or (i <= j and i >= n - 1 - j)]))
