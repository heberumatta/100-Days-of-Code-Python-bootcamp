print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill =+ 15
elif size == "M":
    bill =+ 20
else:
    bill =+ 25

if (pepperoni == "Y") and (size == "L" or size == "M"):
    bill = bill + 3
elif pepperoni == "Y":
    bill = bill+ 2

if extra_cheese == "Y": bill = bill+ 1

print("Pizza cost: ", bill)
