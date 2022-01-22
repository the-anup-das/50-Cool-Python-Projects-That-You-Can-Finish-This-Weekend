from turtle import Turtle, Screen, colormode, shape
import turtle
import random 

turtle.colormode(255)
colors = ['red','blue','green','purple','yellow'] 


my_screen = Screen()
my_screen.setup(width=500, height=400)


def draw_turtle(racer,t_color,x,y):
    racer.color(t_color)
    racer.penup()
    racer.goto(x,y)
    return racer

def game():
    racers = []
    user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \n red/blue/green/purple/yellow")
    FLAG_RACE_ON = False
    x = -230
    y = -100
    for color in colors:
        racers.append(draw_turtle(Turtle(shape="turtle"),color,x,y))
        y = y + 40


    #pen.pensize(5)
    #pen.speed("fastest")

    if user_bet:
        FLAG_RACE_ON = True

    while FLAG_RACE_ON:
        for racer in racers:
            #230 is 250 - half the width of the turtle.
            if racer.xcor() > 230:
                FLAG_RACE_ON = False
                winner = racer.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")
            rand_distance = random.randint(0,10)
            racer.forward(rand_distance)
            

def reset(racer):
    racer.reset()

def restart():
        game()
        # for racer in racers:
        #     racer.clear()
        #     racer.penup()
        #     racer.home()

game()
my_screen.listen()

my_screen.onkey(restart,"r")
my_screen.exitonclick()