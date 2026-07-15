"""
Day 69 - Moving to PostgreSQL for Production
SQLite (a single file) works for local development, but most hosts
recommend Postgres in production since it handles concurrent
connections properly. The only app-side change is the connection
string and the driver — the SQLAlchemy models stay identical.
Requires: pip install psycopg2-binary
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Local development (SQLite):
#   DB_URI=sqlite:///blog.db
# Production (Postgres), typically supplied by the host as:
#   DB_URI=postgresql://user:password@host:5432/dbname
db_uri = os.environ.get("DB_URI", "sqlite:///blog.db")

# Some hosts still hand back an old-style "postgres://" URL, which
# SQLAlchemy 1.4+ rejects — normalise it if needed.
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()
    print(f"Connected using: {db_uri.split('@')[-1] if '@' in db_uri else db_uri}")
