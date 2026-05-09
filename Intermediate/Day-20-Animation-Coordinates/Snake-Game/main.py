from turtle import Turtle, Screen
from snake import Snake

Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")

snake = Snake()
Screen.ontimer(snake.generaApple, 1)
Screen.listen()
Screen.onkey(snake.up, "Up")
Screen.onkey(snake.down, "Down")
Screen.onkey(snake.left, "Left")
Screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    Screen.update()
    snake.move()