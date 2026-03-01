import turtle
from turtle import Turtle, Screen

MOVE_DISTANCE = 20
TURN_ANGLE = 10

tim = Turtle()
tim.speed("fastest")
tim.penup()

drawing_mode = False  # drawing mode state


# -------- MOVEMENT -------- #

def move_forward():
    tim.forward(MOVE_DISTANCE)


def move_backward():
    tim.backward(MOVE_DISTANCE)


def turn_left():
    tim.left(TURN_ANGLE)


def turn_right():
    tim.right(TURN_ANGLE)


# -------- DRAW MODE CONTROL -------- #

def enable_drawing():
    global drawing_mode
    drawing = True
    tim.pendown()

def disable_drawing():
    global drawing_mode
    drawing = False
    tim.penup()

def clear_screen():
    tim.reset()


# -------- SCREEN -------- #

screen = Screen()
screen.listen()

# Movement keys
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

# Toggle drawing with space-bar
screen.onkeypress(enable_drawing, "space")
screen.onkeyrelease(disable_drawing, "space")

screen.onkeypress(clear_screen, "c")

screen.exitonclick()