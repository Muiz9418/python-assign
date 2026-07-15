"""
Day 23 - Working with Data: NATO Phonetic Alphabet
Reads a CSV of the NATO alphabet and converts user input into its
phonetic spelling.
"""
import csv

with open("nato_phonetic_alphabet.csv") as data_file:
    reader = csv.reader(data_file)
    lines = list(reader)[1:]  # skip header row

nato_dict = {}
for row in lines:
    letter, code_word = row[0], row[1]
    nato_dict[letter] = code_word

word = input("Enter a word: ").upper()

output_list = []
for letter in word:
    if letter in nato_dict:
        output_list.append(nato_dict[letter])

print(output_list)
