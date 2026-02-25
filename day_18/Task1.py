from turtle import Turtle, Screen

# TODO 1. draw a square
def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

draw_square(timmy)

screen = Screen()
screen.exitonclick()