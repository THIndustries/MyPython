"""
На вход программе подается число
�
n. Напишите программу, которая создает и выводит построчно список, состоящий из
�
n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число
�
n.

Формат выходных данных
Программа должна вывести построчно указанный список.
"""
n = int(input())
myList = []
for i in range(1, n+1):
    temp = []
    for j in range(1, n+1):
        temp.append(j)
    myList.append(temp)

for item in myList:
    print(item)