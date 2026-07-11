import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RockPaperScissors = [rock, scissors, paper]

player = RockPaperScissors[(int(input("Type 1 to choose rock, 2 for paper, or 3 for scissors: "))-1)]
computer = random.choice(RockPaperScissors)

if computer == player:
    print("-----------¡Draw!-----------")
elif ((computer == scissors) and (player == rock)) or ((player == paper) and (player == rock)) or ((player == scissors) and (computer == paper)):
    print("-----------!Win¡-----------")
else: print("-----------¡Lose!-----------")
print("Player:\n",player)
print("Computer:\n",computer)
