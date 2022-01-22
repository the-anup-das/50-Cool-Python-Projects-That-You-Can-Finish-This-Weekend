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


degree = [0,90,180,270]
pen = Turtle()
pen.pensize(10)
pen.speed("fastest")

for _ in range(1000):
    pen.color(random_color())
    pen.forward(30)
    pen.setheading(random.choices(degree)[0])


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()