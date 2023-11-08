s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
mylist = s.split()
mydict = {}
for i in mylist:
    mydict[i] = mydict.get(i, 0) + 1
mymax = max(mydict.values())

reslist = list()
for i in mydict:
    if mydict[i] == mymax:
        reslist.append(i)

print(min(reslist))





