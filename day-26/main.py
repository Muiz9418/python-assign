"""
Day 26 - List and Dictionary Comprehension
Practice exercises manipulating a dataset (a Central Park squirrel
census) using comprehensions instead of manual loops.
"""
import pandas as pd

# Sample data standing in for the full squirrel census dataset
data = pd.DataFrame({
    "Unique Squirrel ID": ["37F-PM-1", "21B-AM-2", "12E-PM-3"],
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
})

# List comprehension: extract just the fur colors
colors = [color for color in data["Primary Fur Color"]]
print(colors)

# Dictionary comprehension: count occurrences of each fur color
color_count = {color: colors.count(color) for color in set(colors)}
print(color_count)

# Build a small DataFrame from the comprehension result and export it
df = pd.DataFrame(color_count.items(), columns=["fur_color", "count"])
df.to_csv("squirrel_count.csv", index=False)

# Comprehension with a conditional: only squirrels with a known ID prefix
am_squirrels = [sid for sid in data["Unique Squirrel ID"] if "AM" in sid]
print(am_squirrels)
