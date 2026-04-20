import turtle as t
import random

#jim = t.Turtle()
#jim.shape("turtle")
#jim.color("blue")
#for steps in range(100):
#    jim.forward(random.randint(1, 50))
#    jim.right(random.randint(1, 360))


#my_screen = t.Screen()
#my_screen.exitonclick()

import prettytable as pt

table = pt.PrettyTable()
table.add_column("Kilo", [1,'','','','',''])
table.add_column("Deca", [1,0,'','','',''])
table.add_column("Hecto", [1,0,0,'','',''])
table.add_column("Unit", [1,0,0,0,'',''])
table.add_column("Deci", [1,0,0,0,0,''])
table.add_column("Centi", [1,0,0,0,0,0])
print(table)