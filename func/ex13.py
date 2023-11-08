"""Интересная сортировка-1"""

nums = input().split()


def mysort(arg):
    return sum([int(j) for j in arg])


print(*sorted(nums, key=mysort))
