from turtle import Turtle
from config import SCOREBOARD_TEXT_COLOR, SCOREBOARD_POSITION, SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_WEIGHT, GAMEOVER_WEIGHT, GAMEOVER_FONT_SIZE 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color(SCOREBOARD_TEXT_COLOR)
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level {self.level}:', align="center", font=(SCOREBOARD_FONT, SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_WEIGHT))

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.home()
        self.write(f'GAME OVER\nYou made it to Level {self.level}', align="center", font=(SCOREBOARD_FONT, GAMEOVER_FONT_SIZE, GAMEOVER_WEIGHT))
