from turtle import Turtle, Screen
import turtle
import random 

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#creating random color using rgb
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


pen = Turtle()
#pen.pensize(5)
pen.speed("fastest")

def sprio(circles):
    degree = 360 / circles
    for _ in range(circles):
        pen.color(random_color())
        pen.circle(80)
        penhead = pen.heading()+degree
        pen.setheading(penhead)

sprio(360)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()