from turtle import Turtle, Screen
import random 

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

pen = Turtle()

def drawing(lines):
    angel = int(360/lines)
    #pen.shape("turtle")
    pen.color(random.choices(colours))
    for _ in range(lines):
        pen.forward(100)
        pen.right(angel)

for i in range(3,11):
    drawing(i)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()