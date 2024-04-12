import time
from turtle import Screen
from config import CLOCK_TIME, WINDOW_WIDTH, WINDOW_HEIGHT

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.tracer(0)

game_on = True
while game_on:
    time.sleep(CLOCK_TIME)
    screen.update()