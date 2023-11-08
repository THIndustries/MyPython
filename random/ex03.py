from random import randint

length = int(input())

for i in range(length):
    typeletter = randint(0,1)
    if typeletter == 0:
        big = randint(65, 90)
        print(chr(big),end="")
    else:
        small = randint(97, 122)
        print(chr(small),end="")