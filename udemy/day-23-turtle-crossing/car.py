from turtle import Turtle
from config import CAR_COLORS
import random

class Car(Turtle):
    def __init__(self, y_position, speed):
        super().__init__()
        self.position = y_position
        self.speed = speed
        self.shape('square')
        self.penup()
        self.color(random.choice(CAR_COLORS))
    
    def move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.position)