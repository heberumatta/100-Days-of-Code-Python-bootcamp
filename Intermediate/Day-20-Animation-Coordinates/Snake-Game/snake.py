from turtle import Turtle,Screen
import random
screen = Screen()
screen.addshape("cube", ((-5, -5), (-5, 5), (5, 5), (5, -5)))
silueta_manzana = (
    (-3.5, -5), (-4, 4), (4, 4), (3.5, -5)
)
screen.addshape("apple", silueta_manzana)

class Snake:
    def __init__(self):
        self.segments = []
        self.apples = []
        self.create_snake()

    def create_snake(self):
        for i in range(10):
            self.add_segment((-10 * i, 0))

    def add_segment(self, position):
        new_segment = Turtle("cube")
        new_segment.color("white")
        new_segment.speed(1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def eatApple(self):
        head_pos = self.segments[0].onpos()
        for apple in self.apples:
            if apple.onpos() == head_pos:
                self.extend()
                apple.delete()

    def move(self):
        for seg in range(len(self.segments)-1, -1, -1):
            if seg == 0:
                self.segments[0].forward(10)
            else:
                new_x = self.segments[seg-1].xcor()
                new_y = self.segments[seg-1].ycor()
                self.segments[seg].goto(new_x, new_y)
        self.eatApple()
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
        new_apple = Turtle("apple")
        new_apple.color("red")
        new_apple.penup()
        new_apple.goto(cor_x, cor_y)
        self.apples.append(new_apple)
        screen.ontimer(self.generaApple, 5000)
        