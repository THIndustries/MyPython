"""
Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв,
составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.
"""

mydict1 = {}

for i in input().lower():
    mydict1[i] = mydict1.get(i, 0) + 1

mydict2 = {}

for j in input().lower():
    mydict2[j] = mydict2.get(j, 0) + 1

print("YES") if mydict2 == mydict1 else print("NO")



