import random
from art import logo


def card_values(hand, as_flag):
    value = 0
    for card in hand:
        card_value = card[0]
        if card_value in ["K", "J", "Q", "1"]:
            value += 10
        elif card_value == "A":
            if as_flag and (input(f"What value of {card} do you want?(11/1):") == "11"):
                value += 11
            else: value += 1
        else:
            value += int(card_value)
    return value

def choose_bet(money):
    selected_bet = int(input("Please choose a bet: "))
    while selected_bet > money:
        print("You don't have enough money")
        selected_bet = int(input("Please choose a bet: "))
    return selected_bet



deck_of_cards = [ "A♠️", "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️", "A♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️", "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️", "A♣️", "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️" , "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️"]

play_flag = True
wallet = 1000

print(logo)
while play_flag:
    computer_cards = []
    player_cards = []
    computer_value = 0
    player_value = 0
    random.shuffle(deck_of_cards)
    print("Your credit:", wallet)
    bet = choose_bet(wallet)
    wallet -= bet
    if wallet == 0:
        wallet += 100
    input("Press any key to start playing...")
    player_cards.append(deck_of_cards.pop())
    computer_cards.append(deck_of_cards.pop())
    player_cards.append(deck_of_cards.pop())
    computer_cards.append(deck_of_cards.pop())
    computer_value += card_values([computer_cards[0]], True)
    print("First dealer card:", computer_cards[0], ", value: ", computer_value)
    player_value += card_values(player_cards, True)
    print("Your first cards:", player_cards, "value: ", player_value)
    while (player_value < 21) and (input("Do you want to stand or hit?(stand/hit):").lower() == "hit"):
        player_cards.append(deck_of_cards.pop())
        player_value = card_values(player_cards, False)
        print("Your cards are:", player_cards, ", value:",player_value)
    computer_value = card_values(computer_cards, True)
    print("Dealer cards:", computer_cards, "value:", computer_value)
    while (computer_value < 18):
        computer_cards.append(deck_of_cards.pop())
        computer_value = card_values(computer_cards, False)
        print("Dealer cards:", computer_cards, "value:", computer_value)

    if computer_value == player_value:
        print("DRAW")
        wallet += bet
    elif computer_value < player_value and player_value < 22 and computer_value < 22:
        print("YOU WIN")
        wallet += bet*2
    else:
        print("YOU LOSS")

    if input("Do you want to keep playing?(y/n)") == "n":
        play_flag = False
