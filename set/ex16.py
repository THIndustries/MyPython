"""Урок физики"""
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = set(list(map(int, input().split())))
print(*sorted(c.difference(a.union(b)), reverse=True))



