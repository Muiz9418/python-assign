"""
Day 68 - Environment Variables & Secrets Management
Demonstrates loading secrets from a local .env file for development
(never committed to git) while still reading from real environment
variables in production.
Requires: pip install python-dotenv
"""
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from a local .env file, if present

SECRET_KEY = os.environ.get("FLASK_KEY")
DB_URI = os.environ.get("DB_URI")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

if not SECRET_KEY:
    raise RuntimeError("FLASK_KEY is not set — check your .env file or host's env vars.")

print("Secrets loaded successfully (values not printed on purpose).")
