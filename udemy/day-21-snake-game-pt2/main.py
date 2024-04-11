from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        
screen.exitonclick()