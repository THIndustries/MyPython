n, m = map(int, input().split())
matrix = []
count = 1
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(count)
        count += 1
    matrix.append(temp)

for i in matrix:
    for j in i:
        print(str(j).ljust(2), end=" ")
    print()











