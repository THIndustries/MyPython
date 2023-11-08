numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
mydict = {}
for num in numbers:
    mydict[num] = mydict.get(num, 0) + 1
print(mydict)