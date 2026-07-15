"""
Days 59-60 - Flask with SQLite & SQLAlchemy: Virtual Bookshelf
Day 59 introduces SQLAlchemy models and basic Create/Read; Day 60
completes it with Update and Delete — a full CRUD bookshelf app.
Requires: pip install flask flask-sqlalchemy
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = Book.query.order_by(Book.title).all()
    return render_template("index.html", books=all_books)


# --- Day 59: Create ---
@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"]),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


# --- Day 60: Update ---
@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)


# --- Day 60: Delete ---
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
