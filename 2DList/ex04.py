"""
На вход программе подаются две строки: на одной – символы, на другой – число
n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.
"""


def chunked(myList, num) :
    resultList: list[[str]] = []
    for i in range(0, len(myList), num):
        resultList.append(myList[i:i + num])

    return resultList


myList = input().split()
num = int(input())
print(chunked(myList, num))
