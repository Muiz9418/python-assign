"""
Day 50 - Flask, Jinja Templating, and Static Files
Renders HTML templates with Jinja (variables, loops, conditionals)
and serves a linked CSS file from a static folder — the pattern
that later becomes the basis for a full Flask blog.
"""
from flask import Flask, render_template
import random

app = Flask(__name__)

posts = [
    {"title": "Getting Started with Flask", "subtitle": "The basics", "body": "Flask is a lightweight web framework..."},
    {"title": "Understanding Jinja", "subtitle": "Templating 101", "body": "Jinja lets you inject Python logic into HTML..."},
    {"title": "Serving Static Files", "subtitle": "CSS & images", "body": "Static assets live in the /static folder..."},
]


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    if post_id < 0 or post_id >= len(posts):
        return "Post not found", 404
    requested_post = posts[post_id]
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
