"""
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
"""
myList = [[int(j) for j in input().split()] for i in range(int(input()))]
n = len(myList)
m = len(myList)
for i in range(n):
    for j in range(m-1, -1, -1):
        print(myList[j][i], end=" ")
    print()





