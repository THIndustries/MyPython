"""Страны и города"""
n = int(input())
mydict = {}
for i in range(n):
    temp = input().split()
    mydict[temp[0]] = temp[1:]
m = int(input())
for i in range(m):
    town = input()
    for k,v in mydict.items():
        if town in v:
            print(k)
















