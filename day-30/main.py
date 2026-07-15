"""
Day 30 - Errors, Exceptions & JSON Data
Upgrades the Day 29 Password Manager to store data as JSON
(website -> {email, password}) and adds a search feature that
handles the FileNotFoundError and KeyError cases gracefully.
"""
import json
import random
from tkinter import *
from tkinter import messagebox


def generate_password():
    letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(0, 10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
canvas.create_text(100, 100, text="🔒", font=("Arial", 60))
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "you@example.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
