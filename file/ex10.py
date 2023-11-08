"""Сумма чисел в строках"""

with open("numbers (1).txt", 'r', encoding='utf-8') as file:
    nums = [i.split() for i in file.readlines()]
    for i in nums:
        temp = list(map(int, i))
        print(sum(temp))





