import turtle as t
import random

jim = t.Turtle()
jim.shape("turtle")
jim.color("blue")
for steps in range(100):
    jim.forward(random.randint(1, 50))
    jim.right(random.randint(1, 360))


my_screen = t.Screen()
my_screen.exitonclick()