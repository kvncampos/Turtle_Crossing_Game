# Turtle_Crossing_Game

This is a simple implementation of the Turtle Crossing game using Python's Turtle graphics library. The goal of the game is to help the turtle cross the road without getting hit by cars.

# How to Play

Use the Up arrow key to move the turtle up.
Use the Down arrow key to move the turtle down.
Avoid getting hit by the cars moving across the screen.
Reach the other side of the road safely to score points and level up.

# Dependencies

This game requires the following dependencies:

Python (version 3.x)
Turtle graphics library
You can install the required libraries using pip:

Copy code
pip install python-turtle

# How to Run

To run the game, simply execute the Python script:

Copy code
python turtle_crossing.py

# Game Features

The turtle starts at the bottom of the screen and can be moved up and down using the arrow keys.
Cars will be generated from the right side of the screen and move towards the left.
The player earns points and levels up by safely crossing the road.
As the level increases, the speed of the cars and the score requirements for leveling up also increase.
If the turtle gets hit by a car, the game ends, and the final score is displayed.

# Game Controls

Up Arrow: Move the turtle up
Down Arrow: Move the turtle down

# Code Overview

The code is structured into several classes:

Player: Represents the turtle controlled by the player.
CarManager: Manages the generation, movement, and collision detection of cars.
Scoreboard: Keeps track of the player's score and level.
The game logic is implemented using a while loop that runs until the game is over. It continuously updates the screen, moves the cars, checks for collision, and updates the score and level.

Feel free to modify and enhance the game as per your requirements and have fun playing Turtle Crossing!
