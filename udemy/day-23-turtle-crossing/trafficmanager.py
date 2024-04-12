from car import Car
import random

class TrafficManager:
    def __init__(self, number_of_cars, start_speed, speed_increment):
        self.number_of_cars = number_of_cars
        self.speed = start_speed
        self.speed_increment = speed_increment
        self.cars = []

    def generate_cars(self):
        for _ in range(len(self.number_of_cars)):
            random_position = (280, random.randint(-250,250))
            self.cars.append(Car(self.speed, random_position))

    def move_cars(self):
        for car in self.cars:
            car.move()

    def increase_speed(self):
        self.speed += self.speed_increment
