from turtle import Turtle, Screen
from snake import Snake
from apple import Apple
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

#Snake and Apple objects
snake = Snake()
apple = Apple()

#Message turtle
message = Turtle()
message.hideturtle()
message.color("red")
message.penup()
message.goto(0, 0)

#Scoreboard turtle
score = Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(0, 275)
score.write("Score: ", align="center", font=("Arial", 12, "bold"))

#Score counter
counter = Turtle()
counter.hideturtle()
counter.color("white")
counter.penup()
counter.goto(35, 275)
score_counter = 0
counter.write(f"{score_counter}", align="center", font=("Arial", 12, "bold"))

#Screen setup
screen.update()
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

#Main game loop
game_is_on = True
while game_is_on:
    snake.movement()
    if snake.check_collision_with_body() or snake.check_collision_with_wall():
        message.write("¡Perdiste!", align="center", font=("Arial", 24, "bold"))
        game_is_on = False
    if snake.head().distance(apple.apple) < 15:
        counter.clear()
        score_counter += 1
        counter.write(f"{score_counter}", align="center", font=("Arial", 12, "bold"))
        apple.random_position()
        snake.grow()
    time.sleep(0.15)
    screen.update()
screen.exitonclick()