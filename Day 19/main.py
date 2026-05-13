from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for color in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[color])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle wins!")
            else:
                print(f"You lose! The {winning_color} turtle wins!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()