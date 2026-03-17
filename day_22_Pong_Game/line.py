from turtle import Turtle

class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("alice blue")
        self.shapesize(stretch_wid=0.25, stretch_len=0.25)
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(90)
        self.draw_line()

    def draw_line(self):
        while self.ycor() >= -300:
            self.stamp()
            self.penup()
            self.goto(0, self.ycor() - 15)