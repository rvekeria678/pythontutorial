from turtle import Turtle
import config

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in config.STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(config.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != config.DOWN:
            self.head.setheading(config.UP)

    def down(self):
        if self.head.heading() != config.UP:
            self.head.setheading(config.DOWN)

    def left(self):
        if self.head.heading() != config.RIGHT:
            self.head.setheading(config.LEFT)

    def right(self):
        if self.head.heading() != config.LEFT:
            self.head.setheading(config.RIGHT)