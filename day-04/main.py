"""
Day 4 - Rock, Paper, Scissors
Uses randomisation and Python lists / ASCII art.
"""
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! Rock smashes scissors")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose! Rock smashes scissors")
    elif user_choice == 1 and computer_choice == 0:
        print("You win! Paper covers rock")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose! Paper covers rock")
    elif user_choice == 2 and computer_choice == 1:
        print("You win! Scissors cuts paper")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose! Scissors cuts paper")
