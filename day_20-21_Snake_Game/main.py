import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

# --- Screen Setup ---
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# TODO 1. Creating the snake body
snake = Snake()
food = Food()

# TODO 5. Create a score board
scoreboard = ScoreBoard()

# TODO 3. Control the snake with keys
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    # TODO 2. Move the snake
    snake.move()
    screen.update()
    time.sleep(0.08)

    # TODO 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # TODO 6. Detect collision with walls
    if snake.head.xcor() >= 590 or snake.head.xcor() <= -590 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game_is_on = False
        scoreboard.game_over()

    # TODO 7. Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()