from turtle import Turtle
from config import SCOREBOARD_LOCATION, SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE, SCOREBOARD_ALIGNMENT

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.shape(name=None)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=SCOREBOARD_ALIGNMENT, font=(SCOREBOARD_FONT,SCOREBOARD_FONT_SIZE,'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=(SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()