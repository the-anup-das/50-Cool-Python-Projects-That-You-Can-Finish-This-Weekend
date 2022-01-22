from turtle import Turtle, Screen
import turtle
import random 

colours = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
(65, 66, 56)]

turtle.colormode(255)
pen = Turtle()
#pen.pensize(5)
#pen.speed("fastest")
pen.penup()
pen.hideturtle()
pen.setheading(225)
pen.forward(300)
pen.setheading(0)

def hist_painting(number_of_dots):
    for dot_count in range(1, number_of_dots + 1):
        pen.dot(20, random.choice(colours))
        pen.forward(50)

        if dot_count % 10 == 0:
            pen.setheading(90)
            pen.forward(50)
            pen.setheading(180)
            pen.forward(500)
            pen.setheading(0)


hist_painting(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()