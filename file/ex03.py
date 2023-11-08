myfile = open('numbers.txt', 'r', encoding='utf-8')
text = myfile.readlines()
mysum = 0
for i in text:
    mysum += int(i)
print(mysum)
myfile.close()

