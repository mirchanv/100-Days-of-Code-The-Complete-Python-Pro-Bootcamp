import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating a turtle player object
turtle_player = Player()

# Creating scoreboard
scoreboard = Scoreboard()

# Creating a car manager object
car_manager = CarManager()

screen.listen()
screen.onkeypress(turtle_player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()

    # remove cars which have crossed the screen
    for car in car_manager.all_cars:
        if car.xcor() < -320:
            car_manager.remove_car(car)

    # move all the cars
    car_manager.move_cars()

    # check if level cleared
    if turtle_player.has_cleared_level():
        turtle_player.go_to_start()
        car_manager.update_speed()
        scoreboard.increment_level()

    # Detect collision with car
    for car in car_manager.all_cars:
        if turtle_player.distance(car) < 22:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
