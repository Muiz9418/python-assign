"""
Day 35 - Automated Birthday Wisher
Checks a CSV of birthdays daily; if today matches someone's
birthday, emails them a randomly chosen letter template.
Intended to be run once a day (e.g. via a scheduled task/cron job).
"""
import datetime as dt
import random
import smtplib
import pandas as pd

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_app_password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
