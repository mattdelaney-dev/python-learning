from turtle import Turtle

class Write_State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def mark_state(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 10, "normal"))