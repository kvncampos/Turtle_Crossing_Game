from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
CLEAR_LEVEL = False


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.tilt(90)
        self.clear_level = CLEAR_LEVEL

    def go_up(self):
        """Moves the Turtle Up"""
        new_y = self.ycor() + MOVE_DISTANCE
        if self.ycor() == FINISH_LINE_Y:
            self.clear_level = True
        else:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the Turtle Down"""
        new_y = self.ycor() - MOVE_DISTANCE
        if self.pos() <= STARTING_POSITION:
            pass
        else:
            self.goto(self.xcor(), new_y)

    def check_finish_line(self):
        """if Turtle has reached Finish Line, Returns True."""
        if self.clear_level:
            self.clear_level = False
            return True

    def go_to_start(self):
        """Returns Turtle to Starting Position"""
        self.goto(STARTING_POSITION)

