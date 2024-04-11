from turtle import Turtle
from config import BALL_COLOR, BALL_SHAPE, BALL_SPEED, BALL_STRETCH_WIDTH, BALL_STRETCH_LENGTH

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.shapesize(stretch_wid=BALL_STRETCH_WIDTH, stretch_len=BALL_STRETCH_LENGTH)
        self.goto(x=0,y=0)
    
    def move(self):
        self.goto(x=self.xcor()+BALL_SPEED,y=self.ycor()+BALL_SPEED)
        
        