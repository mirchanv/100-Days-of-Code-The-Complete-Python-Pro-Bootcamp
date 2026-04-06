import turtle
import pandas
from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT_STYLE = ('Courier', 10, 'normal')

screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
missed_states = {
    "state": []
}

def add_state_to_map(state, x, y):
    pin = Turtle()
    pin.penup()
    pin.hideturtle()
    pin.goto(x, y)
    pin.write(f'{state}', align=ALIGNMENT, font=FONT_STYLE)

def check_missed_states():
    for current_state in all_states:
        if current_state not in guessed_states:
            missed_states["state"].append(current_state)

def write_to_file():
    data_frame = pandas.DataFrame(missed_states)
    data_frame.to_csv("states_to_learn.csv")

while len(guessed_states) < len(all_states):
    user_input = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()

    if user_input == "Exit":
        break

    if user_input in all_states:
        guessed_states.append(user_input)
        state_info = data[data["state"] == user_input]
        x_cor = state_info.x.item()
        y_cor = state_info.y.item()
        add_state_to_map(user_input, x_cor, y_cor)

check_missed_states()
write_to_file()


