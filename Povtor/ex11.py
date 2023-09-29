"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
Теперь он использует их в качестве серверов "Пегого дудочника".
Помогите владельцу фирмы отыскать все зараженные холодильники.
"""

n = int(input())
myList = [input() for i in range(n)]
word = ['a', 'n', 't', 'o', 'n']
resMylist = [''.join(j for j in i if j in word) for i in myList]
res = [i[:-1] for i in resMylist]
newList = []
for i in res:
    temp = ""
    for j in i:
        if j not in temp:
            temp += j
    newList.append(temp)

print(newList)

