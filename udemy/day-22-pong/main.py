from turtle import Screen
from ball import Ball
from paddle import Paddle
from config import SCREEN_SIZE_X, SCREEN_SIZE_Y, RPADDLE_X_START, RPADDLE_Y_START, LPADDLE_X_START, LPADDLE_Y_START
import time

screen = Screen()
screen.bgcolor('black')
screen.screensize(canvwidth=SCREEN_SIZE_X, canvheight=SCREEN_SIZE_Y)
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((LPADDLE_X_START, LPADDLE_Y_START))
right_paddle = Paddle((RPADDLE_X_START, RPADDLE_Y_START))
screen.update()

screen.listen()

#screen.onkey(key='w')
#screen.onkey(key='s')
#screen.onkey(key='Up')
#screen.onkey(key='Down')

screen.exitonclick()