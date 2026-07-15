"""
Day 45 - Top 100 Movies Website Generator
Scrapes a "greatest movies" list, reverses the ranking (#1 at the
bottom, since it's revealed by scrolling up), and generates a
static HTML page listing them, reusing a template file.
"""
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_tags = soup.select(".title")
all_movies = [movie.get_text() for movie in movie_tags]

# Reverse so #1 appears last (revealed last when scrolling up the page)
all_movies.reverse()

with open("template.html") as file:
    html_content = file.read()

for i, movie in enumerate(all_movies, start=1):
    html_content = html_content.replace("<!-- INSERT_LIST_ITEM -->",
                                         f"<li>{movie}</li>\n<!-- INSERT_LIST_ITEM -->")

with open("movies.html", "w") as file:
    file.write(html_content)

print("movies.html generated.")
