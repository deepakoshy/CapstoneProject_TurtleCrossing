import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(turtle.move, "Up")

score = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.new_car()
    car.car_move()

    if turtle.ycor() >= 280:
        score.update_level()
        turtle.start()
        car.speed_up()

    for one_car in car.all_cars:
        if turtle.distance(one_car) <= 20:
            score.over()
            game_is_on = False


screen.exitonclick()
