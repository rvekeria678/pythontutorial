from turtle import Turtle
from config import PADDLE_STRETCH_WIDTH, PADDLE_STRETCH_LENGTH, MOVE_DISTANCE, PADDLE_COLOR, PADDLE_SHAPE

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH,stretch_len=PADDLE_STRETCH_LENGTH, outline=None)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)