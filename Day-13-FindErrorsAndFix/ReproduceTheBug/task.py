from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_num)
print(dice_images[dice_num])

# The code is meant to simulate rolling a dice and print the corresponding dice image.
# The problem is that it throws an IndexError because the list index starts at 0 and goes up to 5
# The randint function generates a number between 1 and 6, which is used as an index to access the dice_images list.
# We can put a print statement to check the value of dice_num and see that it is indeed between 1 and 6, which is 
# out of range for the list index.
# To fix the problem, we can change the randint function to generate a number between 0 and 5, or we can adjust 
# the index when accessing the list by subtracting 1 from dice_num.