"""
Day 7 - Hangman
Classic word-guessing game with ASCII art stages.
"""
import random

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

stages = [r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
""", r"""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
""", r"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
""", r"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""", r"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""", r"""
   +---+
   |   |
   O   |
       |
       |
       |
=========
""", r"""
   +---+
   |   |
       |
       |
       |
       |
========="""]

word_list = ["aardvark", "baboon", "camel", "elephant", "flamingo", "giraffe"]
chosen_word = random.choice(word_list)

lives = 6
display = ["_" for _ in chosen_word]
game_over = False

print(logo)

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    print(" ".join(display))

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
