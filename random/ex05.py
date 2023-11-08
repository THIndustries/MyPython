from random import randint

def generate_ip():
    myList = []
    for i in range(4):
        myList.append(str(randint(0, 255)))
    return ".".join(myList)


print(generate_ip())
