from turtle import Turtle
from config import SCOREBOARD_LOCATION, SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.shape(name=None)
        self.color('white')
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=(SCOREBOARD_FONT,SCOREBOARD_FONT_SIZE,'normal'))
        self.score += 1