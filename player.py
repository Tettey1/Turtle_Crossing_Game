from turtle import *
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move_up(self):
        """Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move
        the turtle north """
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def goto_start(self):
        self.goto(STARTING_POSITION)






