import turtle
from random import choice
from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
turtle.colormode(255)
tim.hideturtle()

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188),
 (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
 (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8),
 (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
 (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

tim.penup()
tim.speed('fastest')
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.pencolor(choice(color_list))
        tim.pendown()
        tim.dot(20)
        tim.forward(5)
        tim.penup()
        tim.forward(50)
        tim.penup()
    tim.forward(10)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(560)
    tim.right(180)









screen.exitonclick()