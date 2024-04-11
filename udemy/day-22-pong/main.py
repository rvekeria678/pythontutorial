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

right_paddle = Paddle((RPADDLE_X_START, RPADDLE_Y_START))
left_paddle = Paddle((LPADDLE_X_START,LPADDLE_Y_START))

screen.update()

screen.listen()

screen.onkeypress(key='Up', fun=right_paddle.rise)
screen.onkeypress(key='Down', fun=right_paddle.sink)
screen.onkeypress(key='w', fun=left_paddle.rise)
screen.onkeypress(key='s', fun=left_paddle.sink)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    
    

screen.exitonclick()