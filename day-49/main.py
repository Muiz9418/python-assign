"""
Day 49 - Introduction to Backend Web Development with Flask
Covers routes, dynamic URLs, HTML in responses, and Flask's
built-in debug/reload server.
"""
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to my Flask app!</h1><p>This is the home page.</p>"


@app.route('/username/<name>')
def greet(name):
    return f"<h1>Hello there, {name}!</h1>"


@app.route('/username/<name>/<int:number>')
def greet_with_number(name, number):
    return f"<h1>Hello {name}, you are guest number {number}!</h1>"


@app.route('/bye')
def bye():
    random_number = random.randint(1, 10)
    if random_number % 2 == 0:
        return "<h1 style='color:blue'>Goodbye!</h1>"
    else:
        return "<h1 style='color:red'>Goodbye!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
