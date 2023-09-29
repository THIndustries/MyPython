n, m = map(int, input().split())
matrix = []
count = 1
for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(count)
        count += 1
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix[j][i], end= " ")
    print()



