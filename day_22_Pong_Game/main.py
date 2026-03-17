import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from line import CenterLine

TOP_BOTTOM_WALL = 280

# --- Screen Setup ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("MidnightBlue")
screen.title("Pong Game")
screen.tracer(0)

# Creating Paddle objects
r_paddle = Paddle((350, 0), "crimson")
l_paddle = Paddle((-350, 0), "orange")

# Creating a Ball object
ball = Ball()

# Creating Scoreboard
scoreboard = Scoreboard()

center_line = CenterLine()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() >= TOP_BOTTOM_WALL or ball.ycor() <= -TOP_BOTTOM_WALL:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.ycor() <= r_paddle.ycor() + 50) and (ball.ycor() >= r_paddle.ycor() - 50) and (
            ball.xcor() == r_paddle.xcor() - 20):
        ball.bounce_x()

    # Detect collision with left paddle
    if (ball.ycor() <= l_paddle.ycor() + 50) and (ball.ycor() >= l_paddle.ycor() - 50) and (
            ball.xcor() == l_paddle.xcor() + 20):
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() <= -390:
        ball.reset_position()
        scoreboard.r_point()

    time.sleep(ball.pace)
    screen.update()

screen.exitonclick()
