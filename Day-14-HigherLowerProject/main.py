import random 
from art import logo, vs
from game_data import data

def string_of_data(account):
    """Format the account data into printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def compare(account_a, account_b):
    """Compare the follower count of two accounts."""
    if account_a['follower_count'] >= account_b['follower_count']:
        return 'a'
    else:
        return 'b'

# Initialize the variables for the game
score = 0
game_should_continue = True

"""For this we shuffle the data and pop, this ensures that we don't get the same account twice"""
deck = data[:]
random.shuffle(deck)
account_a = deck.pop()
account_b = deck.pop()
print(logo)


while game_should_continue:

    print(f"Compare A: {string_of_data(account_a)}.")
    print(vs)
    print(f"Against B: {string_of_data(account_b)}.")

    while (guess := input("Who has more followers? Type 'A' or 'B': ").lower()) not in ['a', 'b']:
        print("Invalid input. Please type 'A' or 'B'.")
    if guess == compare(account_a, account_b):
        score += 1
        print("\n" + "-"*50 + "\n")
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        try:
            account_b = deck.pop()
        except IndexError:
            print("No more accounts to compare. You've completed the game!")
            break
    else:
        game_should_continue = False
        print("\n" + "-"*50 + "\n")
        print(f"Sorry, that's wrong. Final score: {score}.")
    print("\n" + "-"*50 + "\n")
