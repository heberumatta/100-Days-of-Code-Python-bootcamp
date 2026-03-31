#IMPORTANT: THIS SOLUTION WAS BECAUSE I DIDN'T KNOW ABOUT random.shuffle(x) 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letters_cont = 0
symbols_cont = 0
numbers_cont = 0
list_char = []
password = ''

for i in range(nr_letters + nr_symbols + nr_numbers):
    #Here we control what list have been used
    letters_yes = False
    symbols_yes = False
    numbers_yes = False
    if letters_cont < nr_letters: letters_yes = True
    if symbols_cont < nr_symbols: symbols_yes = True
    if numbers_cont < nr_numbers: numbers_yes = True

    if letters_yes and symbols_yes and numbers_yes:
        list_char = random.choice([letters, symbols, numbers])
    elif letters_yes and symbols_yes:
        list_char = random.choice([letters, symbols])
    elif letters_yes and numbers_yes:
        list_char = random.choice([letters, numbers])
    elif numbers_yes and symbols_yes:
        list_char = random.choice([numbers, symbols])
    elif numbers_yes: list_char = numbers
    elif letters_yes: list_char = letters
    elif symbols_yes: list_char = symbols

    #Here we choose a random list and then the character
    random_char = random.choice(list_char)

    if list_char == letters:
        letters_cont += 1
    elif list_char == symbols:
        symbols_cont += 1
    elif list_char == numbers:
        numbers_cont += 1
    password = password + random_char

print("Your new password is:",password)
