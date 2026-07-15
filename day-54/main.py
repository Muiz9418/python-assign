"""
Days 54-57 - Blog Capstone (WTForms + Bootstrap + full CRUD)
A multi-day build treated as one project here since the course
adds to the same app each day:
  Day 54: form-based "New Post" page with WTForms + Bootstrap-Flask
  Day 55: styling the blog with Bootstrap, header/footer includes
  Day 56: Edit and Delete functionality for posts
  Day 57: Finishing touches — full CRUD blog complete

Data is kept in-memory here for simplicity; Day 59-60 introduces a
real database, and Days 61-62 add user accounts on top of this.

Requires: pip install flask flask-wtf flask-bootstrap5 flask-ckeditor
"""
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-secret-key-change-this'


class PostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = StringField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


# In-memory "database" of posts
all_posts = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Who knew houseplants could be this interesting?",
        "author": "Angela",
        "date": "June 9, 2026",
        "img_url": "https://placehold.co/900x400?text=Cactus",
        "body": "Cacti are more fascinating than they get credit for...",
    }
]
next_id = 2


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = next((post for post in all_posts if post["id"] == post_id), None)
    return render_template("post.html", post=requested_post)


# --- Day 54: New Post form ---
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        global next_id
        new_post = {
            "id": next_id,
            "title": form.title.data,
            "subtitle": form.subtitle.data,
            "author": form.author.data,
            "date": date.today().strftime("%B %d, %Y"),
            "img_url": form.img_url.data,
            "body": form.body.data,
        }
        all_posts.append(new_post)
        next_id += 1
        return redirect(url_for('home'))
    return render_template("make-post.html", form=form, is_edit=False)


# --- Day 56: Edit Post ---
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = next((post for post in all_posts if post["id"] == post_id), None)
    edit_form = PostForm(
        title=post_to_edit["title"],
        subtitle=post_to_edit["subtitle"],
        img_url=post_to_edit["img_url"],
        author=post_to_edit["author"],
        body=post_to_edit["body"],
    )
    if edit_form.validate_on_submit():
        post_to_edit["title"] = edit_form.title.data
        post_to_edit["subtitle"] = edit_form.subtitle.data
        post_to_edit["img_url"] = edit_form.img_url.data
        post_to_edit["author"] = edit_form.author.data
        post_to_edit["body"] = edit_form.body.data
        return redirect(url_for('show_post', post_id=post_id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# --- Day 56: Delete Post ---
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    global all_posts
    all_posts = [post for post in all_posts if post["id"] != post_id]
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
