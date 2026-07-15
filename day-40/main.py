"""
Day 40 - Automated Amazon Price Tracker
Fetches a product page, parses the price with BeautifulSoup, and
emails an alert if the price drops below a target amount.
"""
import smtplib
import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/dp/EXAMPLE_PRODUCT_ID"
BUY_PRICE = 150.00

MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_app_password"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find(id="productTitle").get_text().strip()
price_string = soup.find(class_="a-price-whole").get_text()
price_as_float = float(price_string.replace(",", "").replace(".", ""))

print(f"{title}: ${price_as_float}")

if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Price Drop Alert!\n\n{title} is now ${price_as_float}, "
                f"below your target of ${BUY_PRICE}.\n{PRODUCT_URL}"
        )
