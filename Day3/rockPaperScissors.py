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

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computerChoice = random.randint(0,2)
gameImage = [rock, paper, scissors]

print(f'Computer chooses {gameImage[computerChoice]}')


if playerChoice < 0 or playerChoice > 2:
    print("Please give a value between 0 and 2")
else: 
    print(f'You choose {gameImage[playerChoice]}')
    if playerChoice == 0:
        if computerChoice == 1:
            print("You lose!")
        elif computerChoice == 2:
            print("You win!")
    elif playerChoice == 1:
        if computerChoice == 0:
            print("You win!")
        if computerChoice == 2:
            print("You lose!")
    elif playerChoice == 2:
        if computerChoice == 0:
            print("You lose!")
        if computerChoice == 1: 
            print("You Win!")
    elif playerChoice == computerChoice:
        print("Tie game")
    else:
        print("Please enter proper value")

