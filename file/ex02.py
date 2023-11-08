from random import randint
myfile = open('lines.txt', 'r', encoding='utf-8')
line = myfile.readlines()
print(line[randint(0, len(line))].rstrip())
myfile.close()