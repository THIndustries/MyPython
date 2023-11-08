import turtle


def square(side):
    turtle.showturtle()

    step1(side)
    turtle.left(90)
    turtle.forward(side/2)
    step2(side)

def step1(side):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


def step2(side):
    turtle.left(90)
    turtle.forward(side)
    turtle.back(side/2)
    turtle.left(90)
    turtle.forward(side/2)
    turtle.back(side)



def turtleback(side):
    turtle.forward(side/2)
    turtle.right(90)
    turtle.back(side/2)
    turtle.back(side / 4)
    turtle.left(90)
side = 400
square(side)
turtleback(side)
turtle.setheading(45)
square(side)
turtle.mainloop()