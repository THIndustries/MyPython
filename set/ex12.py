"""Одинаковые цифры"""
a = [int(i) for i in input()]
b = list(map(int, input()))
print("NO" if set(a).isdisjoint(set(b)) else "YES")
