from turtle import Turtle
from config import PADDLE_STRETCH_WIDTH, PADDLE_STRETCH_LENGTH, MOVE_DISTANCE

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH,stretch_len=PADDLE_STRETCH_LENGTH, outline=None)
        self.goto(position)

    def rise(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def sink(self):
        self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)