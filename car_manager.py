from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

STARTING_POSITIONS = [240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0,
                      -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.distance_speed = 0
        self.hideturtle()
        self.counter = 0
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def should_generate_car(self):
        """Checks for Counter: if its 6 New Car Should be created."""
        return self.counter % 6 == 0

    def create_car(self):
        """Creates a Car 20x40, Random Color, Right Side of Screen"""
        new_car = Turtle("square")
        new_car.penup()
        new_car.showturtle()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(280, random.choice(STARTING_POSITIONS))
        self.cars.append(new_car)
        self.counter = 0
        self.distance_speed = 0

    def update_counter(self):
        """Simple counter for Car Addition Pace"""
        self.counter += 1

    def move_cars(self):
        """Move Cars by STARTING_MOVE_DISTANCE Speed"""
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())
            if car.xcor() >= 320:
                car.hideturtle()

    def check_collision(self, player):
        """Check for Collision of Car to Player. Less than 25 distance."""
        for car in self.cars:
            if car.distance(player) < 25:
                # print("testing collision")
                return True

    def speed_up(self):
        """Speeds up the Cars by 5 via MOVE_INCREMENT"""
        self.car_speed += MOVE_INCREMENT
