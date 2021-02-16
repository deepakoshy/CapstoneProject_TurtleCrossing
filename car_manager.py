from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new = Turtle("square")
            new.color(random.choice(COLORS))
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.penup()
            new.goto(310, random.randint(-240, 240))
            self.all_cars.append(new)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
