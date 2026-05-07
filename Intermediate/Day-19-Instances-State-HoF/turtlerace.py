from turtle import Turtle, Screen
import random

screen = Screen()

class Racer(Turtle):
    def __init__(self, color, y_position):
        super().__init__()
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.goto(-200, y_position)
        self.pendown()

    def move(self):
        self.forward(random.randint(1, 10))

def start_race():
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    racers = []
    for i in range(len(colors)):
        racers.append(Racer(colors[i], i * 40 - 100))

    whoWins = screen.textinput("Make your bet", "Which turtle will win? (red, blue, green, yellow, orange, purple)")

    while True:
        for racer in screen.turtles():
            racer.move()
            if racer.xcor() >= 200:
                if whoWins == racer.color()[0]:
                    print(f"You've won! {racer.color()[0]} is the winner!")
                else:
                    print(f"You've lost! {racer.color()[0]} is the winner!")
                return
start_race()
screen.exitonclick()