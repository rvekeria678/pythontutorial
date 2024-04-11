from turtle import Turtle
from config import BALL_COLOR, BALL_SHAPE, BALL_SPEED, BALL_STRETCH_WIDTH, BALL_STRETCH_LENGTH

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.shapesize(stretch_wid=BALL_STRETCH_WIDTH, stretch_len=BALL_STRETCH_LENGTH)
        self.goto(x=0,y=0)
        self.x_vel = 10
        self.y_vel = 10
    
    def move(self):
        new_x = self.xcor() + self.x_vel
        new_y = self.ycor() + self.y_vel
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_vel *= -1

    def hit(self):
        self.x_vel *= -1
        
        