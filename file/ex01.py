myfile = open(input(), "r+", encoding='utf-8')
text = myfile.readlines()
for i in range(len(text)):
    if i == len(text) - 2:
        print(text[i].rstrip())

myfile.close()