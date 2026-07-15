"""
Day 66 - Getting a Flask App Ready for Deployment
Key changes needed before deploying (using the Day 61-62 blog as
the example app):
  1. Swap Flask's dev server for a production WSGI server (Gunicorn)
  2. Move secrets (SECRET_KEY, DB URL) out of source code and into
     environment variables
  3. Add a requirements.txt and a Procfile for the host to use
This file documents those changes; requirements.txt and Procfile
are alongside it.
"""
import os
from flask import Flask

app = Flask(__name__)

# Before: app.config['SECRET_KEY'] = 'a-secret-key-change-this'
# After: read from an environment variable, with a dev fallback
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY", "dev-only-fallback-key")

# Before: 'sqlite:///blog.db'
# After: read from an environment variable so production can point
# at a real Postgres database while local dev still uses SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///blog.db")


@app.route('/')
def home():
    return "<h1>Ready for deployment!</h1>"


# NOTE: no app.run(debug=True) at the bottom for production —
# Gunicorn imports this "app" object directly instead. Keep a
# debug-only run block guarded like this for local testing:
if __name__ == "__main__":
    app.run(debug=True)
