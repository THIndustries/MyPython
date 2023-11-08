def count_args(*args):
    return len(args)


assert (count_args()) == 0
assert (count_args(10)) == 1
assert (count_args('stepik', 'beegeek')) == 2
assert (count_args([], (''), 'a', 12, False)) == 5

print("проверки пройдены")