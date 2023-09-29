"""
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу,
которая выводит след заданной квадратной матрицы.
"""
def createArr(num):
    myArr = [[int(j) for j in input().split()] for i in range(num)]
    res = sum(myArr[i][i] for i in range(num))
    print(res)


createArr(int(input()))



