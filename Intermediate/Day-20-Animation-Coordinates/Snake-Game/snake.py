from turtle import Turtle,Screen
import random
screen = Screen()
screen.addshape("cube", ((-5, -5), (-5, 5), (5, 5), (5, -5)))

class Snake:
    def __init__(self):
        self.segments = []
        self.apples = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment((-15 * i, 0))

    def add_segment(self, position):
        new_segment = Turtle("cube")
        new_segment.color("white")
        new_segment.speed(1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def appleHere(self):
        position = self.segments[0].pos()
        for apple in self.apples:
            if apple.pos() == position:
                return (apple)
        return None

    def eatApple(self, apple=None):
        apple.hideturtle()
        self.extend()

    def move(self):
        apple_here = self.appleHere()
        if apple_here:
            self.eatApple(apple_here)
        for seg in range(len(self.segments)-1, -1, -1):
            if seg == 0:
                self.segments[0].forward(10)
            else:
                new_x = self.segments[seg-1].xcor()
                new_y = self.segments[seg-1].ycor()
                self.segments[seg].goto(new_x, new_y)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].speed(10)
            self.segments[0].setheading(90)
            self.segments[0].speed(1)
        
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].speed(10)
            self.segments[0].setheading(270)
            self.segments[0].speed(1)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].speed(10)
            self.segments[0].setheading(180)
            self.segments[0].speed(1)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].speed(10)
            self.segments[0].setheading(0)
            self.segments[0].speed(1)

    def generaApple(self):
        cor_x = random.randint(-300, 300)
        cor_y = random.randint(-300, 300)
        new_apple = Turtle("cube")
        new_apple.color("red")
        new_apple.penup()
        new_apple.goto(cor_x, cor_y)
        self.apples.append(new_apple)
        screen.ontimer(self.generaApple, 5000)
        