"""
Days 61-62 - Blog Capstone: Users, Comments & Admin-Only Access
Combines the Day 54-57 blog with the Day 58 auth system and Day
59-60 database patterns: registered users can comment on posts,
and only the first registered user (admin, id==1) can create,
edit, or delete posts — enforced with a custom decorator.
Requires: pip install flask flask-sqlalchemy flask-login werkzeug
"""
from functools import wraps
from flask import Flask, render_template, redirect, url_for, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("blog_post.id"))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first():
            return redirect(url_for('login'))
        new_user = User(
            email=request.form["email"],
            password=generate_password_hash(request.form["password"], method='pbkdf2:sha256', salt_length=8),
            name=request.form["name"],
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>', methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        new_comment = Comment(
            text=request.form["comment"],
            author_id=current_user.id,
            post_id=post_id,
        )
        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template("post.html", post=requested_post, comments=comments)


@app.route('/new-post', methods=["GET", "POST"])
@admin_only
def add_new_post():
    if request.method == "POST":
        new_post = BlogPost(
            title=request.form["title"],
            subtitle=request.form["subtitle"],
            body=request.form["body"],
            img_url=request.form["img_url"],
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("make-post.html")


@app.route('/delete/<int:post_id>')
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
