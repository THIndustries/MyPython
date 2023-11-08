"""Числа первой строки"""
a = [int(i) for i in input().split()]
b = list(map(int, input().split()))
res = set(a).difference(set(b))
print(*sorted(res))

