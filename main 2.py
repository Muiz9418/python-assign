"""
Day 51 - Higher/Lower Game (Flask Web Version)
Takes the console Higher/Lower game and turns it into a small
Flask website: a random number is chosen, and the player keeps
guessing until they land on it.
"""
from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)
print(f"(debug) The secret number is {answer}")
guess_count = 0


@app.route('/')
def home():
    return f'''
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://placehold.co/300x200?text=Guess+a+Number" >
    '''


@app.route('/<int:guess>')
def guess_number(guess):
    global guess_count
    guess_count += 1

    if guess == answer:
        return f"<h1>You got it! The answer was {answer}</h1><p>Guesses taken: {guess_count}</p>"
    elif guess > answer:
        return f"<h1>Too high, try again.</h1><p>Guesses taken: {guess_count}</p>"
    else:
        return f"<h1>Too low, try again.</h1><p>Guesses taken: {guess_count}</p>"


if __name__ == "__main__":
    app.run(debug=True)
