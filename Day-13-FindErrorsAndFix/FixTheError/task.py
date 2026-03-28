try:        # "try" is used to catch exceptions that may occur during the execution of the code. 
    age = int(input("What is your age? "))
except ValueError:  # "except" is used to handle the exception that may occur in the "try" block. In this case, we are catching a ValueError, which occurs when the input cannot be converted to an integer.
    print("Invalid input. Please enter a number.")
    age = int(input("Please enter a valid number for your age: "))  # If a ValueError occurs, we ask the user to input their age again, this time with a prompt that indicates the error.

if age > 18:
    print(f"You can drive at age {age}.")