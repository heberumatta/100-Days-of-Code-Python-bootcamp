import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
gameflag = True
chosen_word = random.choice(word_list)
display = "_"*len(chosen_word)
correct_letters = list(display)

print(logo)
input("Press Enter to start...")

while gameflag:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    print(stages[lives])
    print(display)
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        gameflag = False
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if display == chosen_word:
        gameflag = False
        print("****************************YOU WIN****************************")


