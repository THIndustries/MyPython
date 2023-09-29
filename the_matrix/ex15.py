"""
Шахматная доска
"""
n, m = map(int, input().split())
myList = []
for row in range(n):
    temp = []
    for col in range(m):
        if (row % 2 + col % 2) % 2 == 0:
            temp.append(".")
        else:
            temp.append('*')
    myList.append(temp)

for i in myList:
    print(*i)






