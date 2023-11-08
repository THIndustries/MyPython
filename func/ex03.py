def sq_sum(*args):
    return sum([i**2 for i in args])


assert (sq_sum()) == 0
assert (sq_sum(2)) == 4
assert (sq_sum(1.5, 2.5)) == 8.5
assert (sq_sum(1, 2, 3)) == 14
assert (sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == 385

print("проверки пройдены")