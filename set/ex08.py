"""Встречалось ли число раньше?"""
myList = input().split()

for i in range(len(myList)):
    if myList[:i].count(myList[i].lstrip('0')) < 1:
        print("NO")
    else:
        print("YES")













