import random
import turtle
from turtle import Turtle, Screen

# TODO: Generate a random walk 

def get_random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)

def get_random_steps():
    return random.randint(1, 50)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) # tuple
    return random_color

turtle.colormode(255)
tim = Turtle()
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.pencolor(get_random_color())
    tim.forward(get_random_steps())
    tim.setheading(get_random_direction())





screen = Screen()
screen.exitonclick()