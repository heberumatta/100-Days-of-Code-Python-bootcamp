import random

def select_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 7
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid choice. Defaulting to 'easy' difficulty.")
        return 10

print("Welcome to the Number Guessing Game!")
lives = select_difficulty()
print(f"You have {lives} lives to guess the number.")

number = random.randint(1, 100)
print("I have selected a number between 1 and 100. Can you guess it?")

playing = True
while playing:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        playing = False
    else:
        lives -= 1
        if lives > 0:
            if guess < number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
            print(f"You have {lives} lives remaining.")
        else:
            print(f"Game over! You've run out of lives. The number was {number}.")
            playing = False
