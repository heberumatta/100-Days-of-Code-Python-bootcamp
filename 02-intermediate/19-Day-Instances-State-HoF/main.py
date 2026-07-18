import turtle as t

screen = t.Screen()

jim = t.Turtle()
jim.shape("turtle")

def move_forward():
    jim.forward(10)

def move_backward():
    jim.backward(10)

def turn_left():
    jim.left(15)

def turn_right():
    jim.right(15)

def clear_screen():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.mainloop()
screen.exitonclick()
screen.listener()



