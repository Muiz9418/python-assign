# Day 70 - Deployment Checklist / Web Dev Section Wrap-Up

A consolidated checklist covering everything from Days 66-69,
useful to run through before shipping any Flask project from this
course:

- [ ] `SECRET_KEY` and DB credentials read from environment
      variables, not hardcoded (Day 68)
- [ ] `.env` and `*.db` added to `.gitignore` so secrets/local data
      never get committed
- [ ] `requirements.txt` lists every dependency the app actually
      imports, including `gunicorn` (Day 66)
- [ ] `Procfile` (or host-equivalent) points at the right WSGI
      entry point, e.g. `gunicorn main:app` (Day 66)
- [ ] `app.run(debug=True)` only runs when the script is executed
      directly (`if __name__ == "__main__":`), never in production
- [ ] Database connection string works for both SQLite locally and
      Postgres in production, with the `postgres://` →
      `postgresql://` fix if needed (Day 69)
- [ ] Static files (CSS/images) load correctly under the
      production URL, not just `localhost`
- [ ] Test the deployed app's routes end-to-end after going live,
      not just the build/deploy logs (Day 67)

With that, the core Flask/web-dev arc (Days 41-70) is complete —
HTML/CSS → scraping → Flask basics → forms → a full blog capstone
→ auth → databases → REST API → deployment.
