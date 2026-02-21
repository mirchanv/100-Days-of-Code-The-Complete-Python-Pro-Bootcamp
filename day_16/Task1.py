# Playing with turtle module

from turtle import Turtle, Screen

def draw_square(turtle_obj):
    for _ in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)

# creating new object in python, where timmy is the new object created from Turtle class blueprint
timmy = Turtle()
timmy.shape("turtle")
timmy.color("chartreuse3")
print(timmy)

draw_square(timmy)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()
