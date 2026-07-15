"""
Day 58 - Authentication with Flask
User registration, login, and logout using Flask-Login and
Werkzeug's password hashing (never store plaintext passwords).
Requires: pip install flask flask-login flask-sqlalchemy werkzeug
"""
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        if User.query.filter_by(email=email).first():
            flash("That email is already registered, log in instead.")
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=email, password=hashed_password, name=request.form.get("name"))
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
        elif not check_password_hash(user.password, password):
            flash("Incorrect password, please try again.")
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
