import time
from turtle import Screen
from player import Player
from trafficmanager import TrafficManager
from config import CLOCK_TIME, WINDOW_WIDTH, WINDOW_HEIGHT, NUMBER_OF_CARS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.tracer(0)

player = Player()
manager = TrafficManager(NUMBER_OF_CARS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT)

screen.listen()
screen.onkey(key='Up', fun=player.move)

game_on = True
while game_on:
    time.sleep(CLOCK_TIME)
    screen.update()
    TrafficManager.move_cars()

    # Detect Car Collision

    # Detect Finish Line
    if player.xcor() > 288:
        TrafficManager.increase_speed()

screen.exitonclick()    