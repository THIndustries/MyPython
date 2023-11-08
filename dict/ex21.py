"""Секретное слово"""
shifr = input()
mydict1, mydict2 = {}, {}
for i in shifr:
    mydict1[i] = mydict1.get(i, 0) + 1
n = int(input())
for i in range(n):
    temp = input().split(": ")
    mydict2[int(temp[1])] = temp[0]
sorted(mydict1.items(), key= lambda x: x[1])
for k,v in mydict1.items():
    mydict1[k] = mydict2[v]
for i in shifr:
    print(mydict1[i], end="")






    