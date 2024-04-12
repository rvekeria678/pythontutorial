from turtle import Turtle
from config import CAR_COLORS
import random

class Car(Turtle):
    def __init__(self, start_position, speed):
        super().__init__()
        self.speed = speed
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=1.75)
        self.color(random.choice(CAR_COLORS))
        self.goto(start_position)

    def move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())
