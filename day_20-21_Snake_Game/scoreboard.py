from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ('Courier', 30, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
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
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT_STYLE)
