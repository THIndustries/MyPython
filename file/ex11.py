"""Сумма чисел в файле"""

summa = 0

with open('nums (1).txt') as file:
    for line in file.readlines():
        result_line = ''
        for elem in line:
            result_line += elem if elem.isdigit() else ' '
        summa += sum([int(elem) for elem in result_line.split()])
print(summa)