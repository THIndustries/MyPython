"""Анаграммы 2"""

mydict1 = {}
for i in input().lower():
    if i not in ".,!?:;-" and i != " ":
        mydict1[i] = mydict1.get(i, 0) + 1

mydict2 = {}
for j in input().lower():
    if j not in ".,!?:;-" and j != " ":
        mydict2[j] = mydict2.get(j, 0) + 1

print("YES") if mydict1 == mydict2 else print("NO")




