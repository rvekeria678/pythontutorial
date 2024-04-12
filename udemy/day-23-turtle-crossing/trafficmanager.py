from car import Car
from config import START_POSITION
import random

class TrafficManager:
    def __init__(self, number_of_cars, start_speed, speed_increment):
        self.number_of_cars = number_of_cars
        self.traffic_speed = start_speed
        self.speed_increment = speed_increment
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        for _ in range(self.number_of_cars):
            new_position = (random.randint(-270,280), random.randint(-230,230))
            self.cars.append(Car(start_position=new_position, speed=self.traffic_speed))

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -280:
                car.goto(280, random.randint(-230,230))

    def increase_speed(self):
        self.traffic_speed += self.speed_increment
        for car in self.cars:
            car.speed = self.traffic_speed
