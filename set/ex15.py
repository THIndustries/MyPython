"""Урок математики"""
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = set(list(map(int, input().split())))
res = list()
res.extend(a)
res.extend(b)
res.extend(c)
resSet = set()
for i in sorted(res):
    if res.count(i) < 3:
        resSet.add(i)
print(*sorted(resSet))








