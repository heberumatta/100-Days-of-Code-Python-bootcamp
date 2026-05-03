from turtle import Turtle, Screen, colormode
import random
import colorgram

def extract_colors(image_path, num_colors):
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append(color.rgb)
    return rgb_colors

colormode(255)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

tt = Turtle()
tt.speed("fastest")

def square(t):
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

def differentShapes(t):
	t.pensize(3)
	t.penup()
	t.setpos(-25,500)
	t.pd()
	colors ="#000000"
	for i in range(3,20):
		t.color(colors)
		for j in range(i):
			t.fd(50)
			t.rt(360/i)

def randomwalk(t):
	t.pensize(15)
	for i in range(200):
		t.color(random_color())
		t.fd(30)

		t.setheading(random.choice([0,90,180,270]))

def spirograph(t):
	t.pensize(1)
	for i in range(1,360,5):
		t.color(random_color())
		t.circle(100)
		t.setheading(i)

def hirstPainting(t):
	t.penup()
	t.setpos(-250,-250)
	t.pd()
	colors = extract_colors('image.jpg', 30)
	for i in range(10):
		for j in range(10):
			t.color(random.choice(colors))
			t.dot(20)
			t.penup()
			t.fd(50)
		t.bk(500)
		t.lt(90)
		t.fd(50)
		t.rt(90)



hirstPainting(tt)

screen = Screen()
screen.exitonclick()