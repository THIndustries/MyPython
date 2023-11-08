"""Урок биологии"""
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = set(list(map(int, input().split())))
d = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(*sorted(d - (a | b | c)))
