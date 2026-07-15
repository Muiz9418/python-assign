"""
Day 33 - ISS Overhead Notifier
Checks the International Space Station's current position and
whether it's currently dark at your location; if the ISS is close
overhead AND it's night time, sends an email alert.
Runs in a loop, checking every 60 seconds.
"""
import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 51.507  # your latitude
MY_LONG = -0.128  # your longitude
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_app_password"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and \
           (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky right now."
            )
