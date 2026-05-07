from turtle import Turtle, Screen

sc = Screen()
sc.screensize(600,600,"black")
sc.addshape("cube",((0,0), (5,0), (5,5), (0,5)))
t = Turtle()
t.shape("cube")
t.color("white")
t2 = Turtle()
t2.shape("cube")
t2.color("white")
t.goto((t2.pos())+(5,0))
sc.exitonclick()