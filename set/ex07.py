"""Количество слов в тексте"""
res = input().lower().split()
resSet = set()
for i in res:
    temp = ""
    for j in i:
        if j not in ".,;:-?!":
            temp += j
    resSet.add(temp)
print(len(resSet))
