with open("text.txt", 'r', encoding='utf-8') as myfile:
    text = myfile.read()
    print(text[::-1])