import time
from turtle import Screen
from player import Player
from trafficmanager import TrafficManager
from scoreboard import Scoreboard
from config import CLOCK_TIME, WINDOW_WIDTH, WINDOW_HEIGHT, NUMBER_OF_CARS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.tracer(0)

player = Player()
manager = TrafficManager(NUMBER_OF_CARS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=player.move)

game_on = True
while game_on:
    time.sleep(CLOCK_TIME)
    screen.update()
    manager.move_cars()

    # Detect Car Collision
    for car in manager.cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_on = False

    # Detect Finish Line
    if player.ycor() > 288:
       player.reset_position()
       manager.increase_speed()
       scoreboard.increase_score()

screen.exitonclick()    