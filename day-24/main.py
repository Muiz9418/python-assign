"""
Day 24 - List/Dictionary Comprehension
Refactors the Day 23 NATO alphabet project using Pandas and a
dictionary comprehension instead of a manual loop.
"""
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# {row.letter: row.code for (index, row) in data.iterrows()}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic(word):
    return [nato_dict[letter] for letter in word.upper() if letter in nato_dict]


while True:
    word = input("Enter a word: ")
    try:
        output_list = generate_phonetic(word)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        continue
    else:
        print(output_list)
        break
