from turtle import Turtle
from config import PADDLE_WIDTH, PADDLE_HEIGHT

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=PADDLE_WIDTH,stretch_len=PADDLE_HEIGHT, outline=None)
        self.goto(position)

    def rise(self):
        pass

    def fall(self):
        pass