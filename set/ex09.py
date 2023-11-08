"""
Общие числа
"""

a = map(int, input().split())
b = map(int, input().split())
res = list(set(a).intersection(set(b)))
res.sort()
print(*res)









