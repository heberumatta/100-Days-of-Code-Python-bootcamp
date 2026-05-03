from turtle import Turtle, Screen

t = Turtle()
t.shape('turtle')
t.speed(10)
t.pensize(5)
t.bk(50)

t.fd(100)
t.lt(90)

t.fd(100)
t.lt(45)

t.fd(1.41*50)
t.lt(90)
t.fd(1.41*50)

t.lt(45)
t.fd(100)
t.bk(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.penup()
t.pensize(2)
t.fd(15)
t.pd()
t.rt(90)
t.circle(10)

t.lt(90)
t.fd(20)
t.bk(10)
t.lt(90)
t.fd(10)
t.bk(20)
t.penup()
t.setpos(0,100)
t.pd()
t.pensize(5)
t.lt(180)
t.fd(50)

t.penup()
t.setpos(10,0)
t.pd()

t.lt(90)
t.fd(40)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(40)

t.penup()
t.setpos(7,18)
t.pd()
t.pensize(1)
t.lt(180)
t.circle(2)

t.penup()
t.setpos(1000,0)






screen = Screen()
screen.exitonclick()