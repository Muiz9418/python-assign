"""
Day 9 - Higher Lower Game
Compares two items (e.g. social media accounts) by follower count,
using a list of dictionaries.
"""
import random
import os

logo = """
 _   _ _       _                 _                          
| | | (_) __ _| |__   ___ _ __  | | _____      _____ _ __ 
| |_| | |/ _` | '_ \\ / _ \\ '__| | |/ _ \\ \\ /\\ / / _ \\ '__|
|  _  | | (_| | | | |  __/ |    | | (_) \\ V  V /  __/ |   
|_| |_|_|\\__, |_| |_|\\___|_|    |_|\\___/ \\_/\\_/ \\___|_|   
         |___/                                              
"""

vs = """
######################
# 🆚 #
######################
"""

data = [
    {"name": "Instagram", "follower_count": 476000000},
    {"name": "Cristiano Ronaldo", "follower_count": 215000000},
    {"name": "Ariana Grande", "follower_count": 197000000},
    {"name": "The Rock", "follower_count": 189000000},
    {"name": "Kim Kardashian", "follower_count": 179000000},
    {"name": "Selena Gomez", "follower_count": 178000000},
]


def format_data(item):
    return f'{item["name"]}, a {item.get("description", "public figure/account")}, from {item.get("country", "the internet")}'


def get_random_account():
    return random.choice(data)


def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_a = get_random_account()

while game_should_continue:
    account_b = get_random_account()
    while account_b == account_a:
        account_b = get_random_account()

    print(f"Compare A: {account_a['name']}")
    print(vs)
    print(f"Against B: {account_b['name']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('clear')

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
