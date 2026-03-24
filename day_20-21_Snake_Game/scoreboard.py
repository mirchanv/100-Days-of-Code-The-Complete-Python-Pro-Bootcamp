import os
from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ('Courier', 30, 'normal')

def get_high_score():
    with open("high_score.txt", "r") as data:
        return data.read()

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(get_high_score())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT_STYLE)

    def reset(self):
        if self.score > self.high_score:
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def save_high_score(self):
        with open("high_score.txt", "w") as data:
            self.high_score = self.score
            data.write(f'{self.high_score}')



