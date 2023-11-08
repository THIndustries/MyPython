"""Интересная сортировка-2"""

nums = sorted([int(i) for i in input().split()])
nums = [str(i) for i in nums]
def mysort(arg):
    return sum(int(j) for j in arg)


print(*sorted(nums, key=mysort))











