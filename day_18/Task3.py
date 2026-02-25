from turtle import Turtle, Screen

# TODO 1. draw a dashed line
def draw_dashed_line(turtle, paces):
    for _ in range(10):
        turtle.forward(paces)
        turtle.penup()
        turtle.forward(paces)
        turtle.pendown()


tim = Turtle()
tim.color("green")

draw_dashed_line(tim, 10)

screen = Screen()
screen.exitonclick()