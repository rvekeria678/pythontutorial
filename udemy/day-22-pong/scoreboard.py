from turtle import Turtle
from config import SCOREBOARD_TEXT_COLOR, SCOREBOARD_FONT_WEIGHT, SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color(SCOREBOARD_TEXT_COLOR)
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align="center", font=(SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()