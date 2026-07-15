"""
Day 53 - Intermediate Flask: Blog Powered by an API
Fetches blog post data from a hosted JSON endpoint (e.g. npoint.io)
instead of a database, and renders it with Flask/Jinja — a
stepping stone before adding a real database in later days.
"""
from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_API_URL = "https://api.npoint.io/YOUR_NPOINT_ID"


@app.route('/')
def home():
    response = requests.get(BLOG_API_URL)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:index>')
def show_post(index):
    response = requests.get(BLOG_API_URL)
    all_posts = response.json()
    requested_post = next((post for post in all_posts if post["id"] == index), None)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
