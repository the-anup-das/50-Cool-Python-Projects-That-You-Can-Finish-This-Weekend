from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_print()

    def score_increase(self):
        self.user_score +=1
        self.clear()
        self.score_print()

    def score_print(self):
        self.write(f"Score: {self.user_score}", align="center", font={"Arial", 24, "normal"})

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font={"Arial", 24, "normal"})
