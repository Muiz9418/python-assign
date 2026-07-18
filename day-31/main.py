"""
Day 31/32 - Flash Card App
Shows a word (e.g. French) that flips to reveal its English
translation, using Tkinter, Pandas, and window.after() timing.
Words already learned are removed and saved so they don't show
again in future sessions.
"""
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError or NameError:
    data = pd.read_csv("french_words.csv")

to_learn = data.to_dict(orient="records")

current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    import random
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy - French Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png") if False else None
card_back_img = PhotoImage(file="images/card_back.png") if False else None

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_rectangle(0, 0, 800, 526, fill="white", outline="")
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Simple text-based cross/check buttons instead of image assets
unknown_button = Button(text="❌", font=("Ariel", 20), command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(text="✅", font=("Ariel", 20), command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
