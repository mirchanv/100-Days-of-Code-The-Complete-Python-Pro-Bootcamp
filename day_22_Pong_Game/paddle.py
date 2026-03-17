from turtle import Turtle

DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position, clr):
        super().__init__()
        self.shape("square")
        self.color(clr)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - DISTANCE)