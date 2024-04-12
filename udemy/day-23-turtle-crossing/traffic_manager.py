from car import Car
import random

class TrafficManager:
    def __init__(self, number_of_cars, start_speed, speed_increment):
        self.number_of_cars = number_of_cars
        self.speed = start_speed
        self.speed_increment = speed_increment
        self.cars = []

    def generate_cars(self):
        for i in range(len(self.number_of_cars)):
            self.cars.append(Car(self.speed))

    def increase_speed(self):
        self.speed += self.speed_increment