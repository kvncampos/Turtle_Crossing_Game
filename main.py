import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
# Control the Turtle Up/Down
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Update counter
    car.update_counter()

    # Increases Level Score, Speed of Cars and Turtle back to Starting Position
    if player.check_finish_line():
        scoreboard.level_up()
        car.speed_up()
        player.go_to_start()

    # Check if it's time to create a new car
    if car.should_generate_car():
        car.create_car()
    # Move the cars from right to left of screen
    car.move_cars()

    # Checks for Collision of Cars to Player by Position < 25
    if car.check_collision(player):
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
