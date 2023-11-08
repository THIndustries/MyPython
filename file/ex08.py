with open('data.txt', 'r', encoding='utf-8') as myfile:
    text = [i.strip() for i in myfile.readlines()]
    for i in text[::-1]:
        print(i)