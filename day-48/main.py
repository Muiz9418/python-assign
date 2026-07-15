"""
Day 48 - Web Scraping Practice: Pagination & Data Export
Scrapes a multi-page site (quotes.toscrape.com), following the
"Next" link across pages, and saves the results to a CSV.
"""
import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
url = BASE_URL

all_quotes = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all(class_="quote")
    for block in quote_blocks:
        text = block.find(class_="text").get_text()
        author = block.find(class_="author").get_text()
        all_quotes.append({"quote": text, "author": author})

    next_button = soup.find(class_="next")
    if next_button:
        next_href = next_button.find("a")["href"]
        url = BASE_URL + next_href
    else:
        url = None

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print(f"Scraped {len(all_quotes)} quotes across all pages.")
