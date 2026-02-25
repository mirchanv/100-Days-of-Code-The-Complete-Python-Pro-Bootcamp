import random
from turtle import Turtle, Screen

def draw(turtle):
    for i in range(3, 11):
        turtle.pencolor(random.random(), random.random(), random.random())
        for _ in range(i):
            turtle.forward(100)
            turtle.right(360 / i)

tim = Turtle()
draw(tim)

screen = Screen()
screen.exitonclick()