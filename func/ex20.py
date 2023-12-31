"""Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
в котором каждое значение будет результатом применения переданной функции к переданному списку."""


def func_apply(func, *args):
    for i in args:
        return [func(j) for j in i]



def add3(x):
    return x + 3


def mul7(x):
    return x * 7

assert (func_apply(mul7, [1, 2, 3, 4, 5, 6])) == [7, 14, 21, 28, 35, 42]
assert (func_apply(add3, [1, 2, 3, 4, 5, 6])) == [4, 5, 6, 7, 8, 9]
assert (func_apply(str, [1, 2, 3, 4, 5, 6])) == ['1', '2', '3', '4', '5', '6']
print("Проверки пройдены")