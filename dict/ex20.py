"""Телефонная книга"""
n = int(input())
mydict = {}
for i in range(n):
    text = input().lower().split()
    if text[1] not in mydict:
        mydict[text[1]] = text[0]
    else:
        mydict[text[1]] += " " + text[0]
print(mydict)
m = int(input())
for j in range(m):
    print(mydict.get(input().lower(), "абонент не найден"))








