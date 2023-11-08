from random import randint
num = 7
myset = set()
for i in range(7):
    myset.add(randint(1,49))

for i in sorted(list(myset)):
    print(i, end=" ")