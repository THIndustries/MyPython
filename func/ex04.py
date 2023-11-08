def mean(*args):
    if len(args) < 1:
        return 0
    else:
        mylist = [i for i in args if type(i) == int or type(i) == float]
        mysum = sum(mylist)
        if mysum == 0:
            return 0
        else:
            return  mysum / len(mylist)

assert (mean()) == 0.0
assert (mean(7)) == 7.0
assert (mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2))) == 2.0
assert (mean(True, ['stepik'], 'beegeek', (1, 2))) == 0.0
assert (mean(-1, 2, 3, 10, ('5'))) == 3.5
assert (mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == 5.5