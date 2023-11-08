"""Урок информатики"""
a, b, c = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
temp = set(a).intersection(b)
res = temp.difference(c)
print(*sorted(res, reverse=True))
