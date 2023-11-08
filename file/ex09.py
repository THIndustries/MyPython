with open("lines (1).txt", "r", encoding="utf-8") as myfile:
    text = [i.strip() for i in myfile.readlines()]
    maxlen = max([len(i) for i in text])
    reslist = list(filter(lambda x: len(x) == maxlen, text))
    for i in reslist:
        print(i)
