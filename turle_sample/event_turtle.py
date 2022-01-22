from turtle import Turtle, Screen
import turtle
import random 

turtle.colormode(255)
pen = Turtle()
#pen.pensize(5)
#pen.speed("fastest")

my_screen = Screen()

def move_foward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def move_upward():
    pen_heading = pen.heading() + 10
    pen.setheading(pen_heading)

def move_downward():
    pen_heading = pen.heading() - 10
    pen.setheading(pen_heading)

def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


my_screen.listen()
my_screen.onkey(move_foward,"d")
my_screen.onkey(move_backward,"a")
my_screen.onkey(move_upward,"w")
my_screen.onkey(move_downward,"s")
my_screen.onkey(clear,"c")
my_screen.exitonclick()