from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def set_random_color():
    return random.choice(COLORS)


def set_random_ycor():
    return random.randint(-260, 260)


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(set_random_color())
            new_car.goto(320, set_random_ycor())
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
