from functools import reduce

myfile = open('prices.txt', 'r', encoding='utf-8')
text = myfile.readlines()
text = list(map(lambda x: x.split('\t'), text))
mysum = 0
for i in text:
    temp = int(i[1]) * int(i[2])
    mysum += temp
print(mysum)

myfile.close()
