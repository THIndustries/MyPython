def print_products(*args):
    mylist = []
    for i in range(len(args)):
        if isinstance(args[i], str) and args[i] != "":
            mylist.append(args[i])

    if len(mylist) == 0:
        print("Нет продуктов")
    else:
        for i in range(len(mylist)):
            print(f"{i+1}){mylist[i]}")


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)