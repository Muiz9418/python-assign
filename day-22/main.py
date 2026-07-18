"""
Day 22 - File Input/Output
Covers reading, writing, and appending to text files, plus a small
Rock Paper Scissors state-saving exercise.
"""

# Writing to a file (overwrites if it exists)
with open("my_file.txt", "w") as file:
    file.write("Hello world!\n")

# Appending to a file (adds without erasing existing content)
with open("my_file.txt", "a") as file:
    file.write("This line was appended.\n")

# Reading a file
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# Working with a starting text file: read, modify, save as new file
with open("weather_data.csv", "w") as file:
    file.write("day,temp\nMonday,12\nTuesday,14\nWednesday,15\n")

with open("weather_data.csv") as data_file:
    lines = data_file.readlines()
    print(lines)

# FileNotFoundError handling
try:
    with open("a_file_that_does_not_exist.txt") as file:
        file.read()
except FileNotFoundError:
    with open("a_file_that_does_not_exist.txt", "w") as file:
        file.write("This file was created because it didn't exist yet.")
