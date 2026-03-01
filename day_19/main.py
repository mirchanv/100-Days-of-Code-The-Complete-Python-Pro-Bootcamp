from turtle import Turtle, Screen

def move_forward():
    tim.forward(50)

tim = Turtle()

screen = Screen()
screen.listen()

screen.onkey(fun=move_forward, key="space")
screen.exitonclick()
