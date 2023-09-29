myList = [i for i in input().split()]
n = int(input())
count = len(myList) // n
resList = []

for i in range(n):
    temp = []
    for j in range(i, len(myList), n):
        temp.append(myList[j])
    resList.append(temp)

print(resList)

"""
def chunked(myList, num) :
    resultList = []
    for i in range(0, len(myList), num):
        resultList.append(myList[i:i + num])

    return resultList


myList = input().split()
num = int(input())
print(chunked(myList, num))

"""
