"""Словарь синонимов"""
mydict = {}
for i in range(n := int(input())):
    text = input().split(" ")
    mydict[text[0]] = text[1]

check = input()
if check in mydict:
    print(mydict.get(check))
else:
    for i, j in mydict.items():
        if j == check:
            print(i)