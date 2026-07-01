from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score: {self.score}/50", align="center", font=("Arial", 10, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
