"""
На вход программе подается число
�
n. Напишите программу, которая создает и выводит построчно вложенный список, состоящий из
�
n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
"""
num = int(input())
for i in range(1, num+1):
    temp = []
    for j in range(1, i+1):
        temp.append(j)
    print(temp)
