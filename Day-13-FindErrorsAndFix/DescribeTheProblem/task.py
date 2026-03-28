# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("You got it!")

# my_function()

# Describe the problem - Write your answers as comments in the code below: 
# The function is meant to loop through numbers 1 to 19 and print "You got it!" when it reaches 20. 
# The problem is that "You got it!" is never printed.
# 1. What is the loop doing?
# The loop is iterating through numbers 1 to 19.
# 2. When is the function meant to print "You got it!"?
# The function is meant to print "You got it!" when it reaches 20.
# 3. What are your assumptions about the value of it?
# The assumption is that the loop will include the number 20, but it does not because the range 
# function stops before the end value.

def my_function():
    for i in range(1,21):   #The problem was the range of the loop, it should go up to 21 to include 20.
        if i == 20:
            print("You got it!")

my_function()