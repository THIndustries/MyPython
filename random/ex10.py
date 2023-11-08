import random
n = 5
myset = set()
while len(myset) < 25:
    myset.add(random.randint(1, 75))
myList = [list(myset)[i:i + n] for i in range(0, 25, n)]
myList[2][2] = 0

for i in range(n):
    for j in range(n):
        print(str(myList[i][j]).ljust(3),end=" ")
    print()
