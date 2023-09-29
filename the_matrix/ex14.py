"""
Магический квадрат 🌶️
"""
n = int(input())
myList = [[int(j) for j in input().split()] for i in range(n)]
resArr = []
sumRow = 0
sumCol = 0
sumDiag = 0
sum_Diag = 0
for i in range(n):
    sum_Diag += myList[i][n - 1 - i]
    sumDiag += myList[i][i]
    for j in range(n):
        sumRow += myList[i][j]
        sumCol += myList[j][i]

first_element = myList[0][0]  # Получаем первый элемент матрицы

# Проверяем, что все значения в матрице равны первому элементу
all_equal = all(all(x == first_element for x in row) for row in myList)

if all_equal:
    print("NO")
else:
    print("YES") if sumDiag == sum_Diag == (sumCol/n) == sumRow/n else print("NO")





