
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)

"""leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)"""

"""i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1"""

leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.speed(30)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()

bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.pencolor("pink")
bob.fillcolor(32, 67, 93)
bob.speed(80)

side_length: int = 300
 
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

done()


