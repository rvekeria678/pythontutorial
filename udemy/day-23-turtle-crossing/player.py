from turtle import Turtle
from config import PLAYER_STARTING_POSITION, PLAYER_MOVE_DISTANCE, PLAYER_SHAPE, PLAYER_COLOR

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.penup()
        self.setheading(90)
        self.goto(PLAYER_STARTING_POSITION)
        
    def move(self):
        self.goto(self.xcor(), self.ycor() + PLAYER_MOVE_DISTANCE)

    def reset_position(self):
        self.goto(PLAYER_STARTING_POSITION)