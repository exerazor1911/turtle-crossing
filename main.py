import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

eze = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(eze.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(eze) < 20:
            game_is_on = not game_is_on
            scoreboard.game_over()

    if eze.ycor() > FINISH_LINE_Y:
        eze.reset_turtle()
        car_manager.increment_car_speed()
        scoreboard.increase_score()

screen.exitonclick()
