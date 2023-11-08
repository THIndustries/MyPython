n = int(input())
mydict = {}
for i in range(n):
    text = input().split(': ')
    mydict[text[0].lower()] = text[1]

m = int(input())
for i in range(m):
    temp = input().lower()
    if temp in mydict:
        print(mydict[temp])
    else:
        print("Не найдено")
