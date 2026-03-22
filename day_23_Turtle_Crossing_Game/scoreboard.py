from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.update_scoreboard()

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align="center", font=FONT)
