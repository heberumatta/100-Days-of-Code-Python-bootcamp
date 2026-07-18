from turtle import Turtle, Screen
import random

class Apple:
    def __init__(self):
        self.apple = Turtle()
        self.apple.shape("circle")
        self.apple.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.apple.color("red")
        self.apple.penup()
        self.random_position()

    def random_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.apple.goto(x, y)
                