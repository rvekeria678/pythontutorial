from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        with open('highscore.txt',mode='w') as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def get_highscore(self):
        with open('highscore.txt') as file:
            return int(file.read())

#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
