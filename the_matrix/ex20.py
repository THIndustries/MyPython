n, m = map(int, input().split())

matrix = [i for i in range(1, m + 1)]

for i in range(n):
    for j in range(m):
        print(matrix[j], end=' ')
    pop = matrix.pop(0)
    matrix.append(pop)
    print()
