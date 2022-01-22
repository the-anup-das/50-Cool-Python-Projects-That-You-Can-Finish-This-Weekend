from turtle import Turtle, Screen

pen = Turtle()
#pen.shape("turtle")
pen.color("aquamarine")
for _ in range(4):
    pen.forward(100)
    pen.right(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()