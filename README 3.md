# Day 67 - Deploying the Flask App

Builds on Day 66's deployment-ready app. General steps for a host
like Render or Heroku (exact UI varies by provider):

1. **Push to GitHub** — the host builds from your repo.
2. **Create a new Web Service** on the host, pointing at the repo.
3. **Set the build command** — usually
   `pip install -r requirements.txt`.
4. **Set the start command** — matches the `Procfile`:
   `gunicorn main:app`.
5. **Add environment variables** in the host's dashboard — `FLASK_KEY`,
   `DB_URI`, and any API keys, instead of hardcoding them.
6. **Provision a database** — if using Postgres in production, the
   host usually gives you a connection string to plug into `DB_URI`.
7. **Deploy** and check the build logs if anything fails — the two
   most common issues are a missing dependency in
   `requirements.txt` and a `SECRET_KEY`/`DB_URI` that's still
   hardcoded instead of read from the environment.

Once live, the app is reachable at the host's generated URL (or a
custom domain if you've configured one).
