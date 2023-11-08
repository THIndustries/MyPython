text = input().lower().split()
for i in range(len(text)):
    if text[i][-1] in '.,!?:;-':
        temp = text[i][:-1]
        text[i] = temp


mydict = {}
for i in text:
    mydict[i] = mydict.get(i, 0) + 1
mymin = min(mydict.values())

reslist = list()
for i in mydict:
    if mydict[i] == mymin:
        reslist.append(i)

reslist.sort()
print(reslist[0])