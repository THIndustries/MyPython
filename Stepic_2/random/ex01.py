import random

n = int(input())
for i in range(n):
    num = random.randint(1)
    if num == 0:
        print("Орел")
    else:
        print("Решка")
