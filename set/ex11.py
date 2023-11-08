"""
Общие цифры
"""
num = int(input())
myList = [[int(j) for j in input()] for i in range(num)]
res = set(myList[0])
for i in range(1, num):
    res.intersection_update(set(myList[i]))
print(*sorted(res))

