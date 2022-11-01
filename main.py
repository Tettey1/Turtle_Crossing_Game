import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.listen()
player = Player()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.onkey(player.move_up, 'Up')

car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    # detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # detect when turtle reaches other side
    if player.is_at_finish_line():
        scoreboard.update_level()
        player.goto_start()
        car_manager.level_up()





screen.exitonclick()




