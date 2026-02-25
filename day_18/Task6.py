import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) # tuple
    return random_color

def draw_spirograph(turtle_obj, size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle_obj.pencolor(get_random_color())
        turtle_obj.circle(100)
        turtle_obj.setheading(tim.heading() + size_of_gap)

tim = Turtle()
tim.speed("fastest")
draw_spirograph(tim, 5)

screen = Screen()
screen.exitonclick()