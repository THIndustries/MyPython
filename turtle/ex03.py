import turtle
def hexagon(side):
    for i in range(11):
        step(side)

def step(arg):
    turtle.left(60)
    turtle.forward(side)

side = 50
for i in range(6):
    turtle.left(120)
    hexagon(side)
turtle.mainloop()