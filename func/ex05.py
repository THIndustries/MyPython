def greet(*args):
    if len(args) < 2:
        name = args[0]
        return f"Hello, {name}!"
    else:
        mylist = ["Hello,"]
        for i in range(len(args)):
            if i == len(args) - 1:
                mylist.append(args[i]+"!")
            else:
                mylist.append(args[i])
            if i < len(args) -1:
                mylist.append('and')
    return " ".join(mylist)



assert (greet('Timur')) == 'Hello, Timur!'
assert (greet('Timur', 'Roman')) == 'Hello, Timur and Roman!'
assert (greet('Timur', 'Roman', 'Ruslan')) == 'Hello, Timur and Roman and Ruslan!'
print('all good')

