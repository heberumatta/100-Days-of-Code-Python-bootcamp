from turtle import Turtle,Screen
import random
screen = Screen()

class Snake:
    def __init__(self):
        self.segments = []
        self.has_turned = False
        self.create_snake()
    
    def create_snake(self):
        for pos in [(0,0),(-20,0),(-40,0)]:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
        
    def movement(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.has_turned = False

    def turn_up(self):
        if not self.has_turned and self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.has_turned = True
    
    def turn_down(self):
        if not self.has_turned and self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.has_turned = True

    def turn_left(self):
        if not self.has_turned and self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.has_turned = True
    
    def turn_right(self):
        if not self.has_turned and self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.has_turned = True

    def check_collision_with_body(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.distance(segment) < 10:
                return True
        return False
    
    def check_collision_with_wall(self):
        head = self.segments[0]
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            return True
        return False
    
    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)
    
    def head(self):
        return self.segments[0]
