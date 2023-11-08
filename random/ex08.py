import random
myset = set()
while len(myset) < 100:
    num = random.randint(1000000,9999999)
    myset.add(num)

for i in myset:
    print(i)
