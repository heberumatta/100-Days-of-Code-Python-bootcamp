from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.setheading(random.choice([45, 135, 225, 315]))
        self.move_speed = 0.1
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.color("black")
        self.goto(0, 0)
        self.bounce_x()
        self.color("white")
        