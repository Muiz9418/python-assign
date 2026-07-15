"""
Day 47 - Coffee & Wifi Capstone
Scrapes cafe recommendations submitted via a public Google Form
(rendered as a spreadsheet-style webpage) and re-formats them into
a clean HTML page grouping cafes by location.
"""
import requests
from bs4 import BeautifulSoup

FORM_RESULTS_URL = "https://example.com/coffee-and-wifi-results"  # published Google Sheet/Form page

response = requests.get(FORM_RESULTS_URL)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")[1:]  # skip header row

cafes_by_location = {}
for row in rows:
    cells = row.find_all("td")
    if len(cells) < 3:
        continue
    cafe_name = cells[0].get_text(strip=True)
    location = cells[1].get_text(strip=True)
    wifi_rating = cells[2].get_text(strip=True)

    cafes_by_location.setdefault(location, []).append((cafe_name, wifi_rating))

html_output = "<html><body><h1>Coffee & Wifi</h1>"
for location, cafes in cafes_by_location.items():
    html_output += f"<h2>{location}</h2><ul>"
    for name, wifi in cafes:
        html_output += f"<li>{name} — Wifi: {wifi}</li>"
    html_output += "</ul>"
html_output += "</body></html>"

with open("coffee_and_wifi.html", "w") as file:
    file.write(html_output)

print("coffee_and_wifi.html generated.")
