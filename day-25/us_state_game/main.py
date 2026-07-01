from pathlib import Path
import pandas
from turtle import Turtle, Screen
from state_turtle import Write_State
from scoreboard import Scoreboard

file_path = Path(__file__).parent / "50_states.csv"

write_state = Write_State()
turtle = Turtle()
screen = Screen()
screen.title("USA States Game")
image = Path(__file__).parent / "blank_states_img.gif"
screen.addshape(str(image))
scoreboard = Scoreboard()

turtle.shape(str(image))
game_on = True
states = pandas.read_csv(file_path)
state_list = states["state"].to_list()

while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's Another state's name?").title()

    if answer_state == "Exit":
        new_data = pandas.DataFrame(state_list, columns=["state"])
        output_file = Path(__file__).parent / "states_to_learn.csv"
        new_data.to_csv(output_file, index=False)
        break

    if answer_state in state_list:
        row = states[states["state"] == answer_state]
        x = int(row["x"].iloc[0])
        y = int(row["y"].iloc[0])
        write_state.mark_state(x, y, answer_state)
        scoreboard.add_score()
        state_list.remove(answer_state)
    
    if len(state_list) == 0:
        game_on = False
