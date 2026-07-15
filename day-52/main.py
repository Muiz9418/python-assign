"""
Day 52 - Advanced Flask: WTForms
A Flask-WTF contact form with validation (required fields, email
format, min length), CSRF protection, and Bootstrap-styled rendering.
Requires: pip install flask flask-wtf flask-bootstrap5 email-validator
"""
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a-secret-key-change-this'


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send')


@app.route('/', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real app: send an email or save to a database here
        print(f"New message from {form.name.data} ({form.email.data}): {form.message.data}")
        return redirect(url_for('success'))
    return render_template("contact.html", form=form)


@app.route('/success')
def success():
    return "<h1>Thanks! Your message was sent.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
