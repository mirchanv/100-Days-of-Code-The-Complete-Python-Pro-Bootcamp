import random
from turtle import Turtle, Screen

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=500)

START_LINE = -280
FINISH_LINE = 280

colors = ["red", "green", "yellow", "blue", "orange", "purple"]
all_turtles = []

# --- Setup Turtles ---
def setup_turtles():
    start_y = 130
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.goto(START_LINE, start_y)
        start_y -= 50
        all_turtles.append(turtle)

# --- Race Logic ---
def start_race():
    race_on = True
    while race_on:
        turtle = random.choice(all_turtles)
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() >= FINISH_LINE:
            race_on = False
            declare_winner(turtle)

# --- Result ---
def declare_winner(winning_turtle):
    winning_color = winning_turtle.pencolor()
    print(f"The {winning_color} turtle wins the race 🏁")

    if user_bet == winning_color:
        print("You won the bet!")
    else:
        print("You lost the bet!")

# --- Run Program ---
setup_turtles()

user_bet = screen.textinput(
    title="Make Your Bet",
    prompt="Which turtle will win the race? Enter a color:"
)

if user_bet:
    user_bet = user_bet.lower()
    start_race()

screen.exitonclick()