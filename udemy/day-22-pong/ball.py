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
        self.x_velocity = 10
        self.y_velocity = 10

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_velocity *= -1

    def bounce_y(self):
        self.y_velocity *= -1



        
        