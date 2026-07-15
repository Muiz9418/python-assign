"""
Day 12 - Scope & The Number Guessing Game
Demonstrates local vs global scope using a guessing game with
difficulty-based lives.
"""
import random

logo = """
 ██████╗ ██╗   ██╗███████╗███████╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
╚██████╔╝╚██████╔╝███████╗███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝

██╗    ██╗██╗  ██╗ ██████╗      ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██║    ██║██║  ██║██╔═══██╗     ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║███████║██║   ██║     ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║███╗██║██╔══██║██║   ██║     ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║╚██████╔╝     ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against actual answer, returns remaining turns."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return None


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        result = check_answer(guess, answer, turns)
        if result is None:
            return
        turns = result

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


game()
