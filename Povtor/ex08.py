"""
Напишите программу для определения, является ли число произведением двух чисел из данного набора.
Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
"""

#Вводим кол-во чисел:
n = int(input())

#Заполняем лист значениями:
myList = [int(input()) for i in range(n)]

#Вводим значение ожидаемого результата умножения
result = int(input())

#В цикле проходмся по списку и ищем совпадения:
isGood = False
for i in range(len(myList)):
    for j in range(i+1, n):
        if myList[i] * myList[j] == result:
            isGood = True


print("ДА") if isGood else print("НЕТ")

