from turtle import Screen
from ball import Ball
from paddle import Paddle
from config import SCREEN_SIZE_X, SCREEN_SIZE_Y, RPADDLE_X_START, RPADDLE_Y_START, LPADDLE_X_START, LPADDLE_Y_START
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_SIZE_X, height=SCREEN_SIZE_Y)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((RPADDLE_X_START, RPADDLE_Y_START))
left_paddle = Paddle((LPADDLE_X_START,LPADDLE_Y_START))
ball = Ball()

screen.listen()

screen.onkeypress(key='Up', fun=right_paddle.go_up)
screen.onkeypress(key='Down', fun=right_paddle.go_down)
screen.onkeypress(key='w', fun=left_paddle.go_up)
screen.onkeypress(key='s', fun=left_paddle.go_down)

game_on = True
while game_on:
    time.sleep(0.08)
    screen.update()
    ball.move()    

    # Wall Detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Paddle Detection
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor()  < -320:
        ball.hit()

    # Out-of-Bounds Detection
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.goto(0,0)
        ball.x_vel = 10
        ball.y_vel = 10

screen.exitonclick()