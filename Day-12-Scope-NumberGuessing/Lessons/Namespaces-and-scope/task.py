#We can't use a variable outside of the function it was created in. This is called scope. 
#The variable only exists within the function, and is not accessible outside of it.
#As well if we create a variable with the same name outside of the function, it will not affect the variable inside the function.

enemies = 1 # This variable is outside of the function, and is not affected by the variable inside the function.

def increase_enemies():
    enemies = 2 # This variable is inside the function, and the assignment of 2 does not affect the variable outside the function.
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
