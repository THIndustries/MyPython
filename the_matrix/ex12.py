"""
Дана квадратная матрица чисел. Напишите программу,
которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
"""
myList = [[int(j) for j in input().split()] for i in range(int(input()))]

n = len(myList)
for row in range(len(myList) // 2):
    myList[row], myList [n - row-1] = myList[n - row-1], myList[row]

for i in myList:
    print(*i)
