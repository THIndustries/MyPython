"""
Уникальные символы 1
"""
myList = [len(set(input().lower())) for i in range(int(input()))]
for i in myList:
    print(i)




