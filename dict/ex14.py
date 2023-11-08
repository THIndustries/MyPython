text = input().split()

mydict = {}
for i in text:
    mydict[i] = mydict.get(i, 0) + 1
    if mydict[i] == 1:
        print(i, end=" ")
    else:
        print(f"{i}_{mydict[i] - 1}", end=" ")








