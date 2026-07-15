"""
Days 63-65 - RESTful API Capstone: Cafe & Wifi API
Day 63: GET endpoints (random cafe, all cafes, search by location)
Day 64: POST endpoint to add a new cafe
Day 65: PATCH (update price) and DELETE (with API-key auth) — a
complete RESTful API following HTTP method conventions.
Requires: pip install flask flask-sqlalchemy
"""
import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

API_KEY = "TopSecretAPIKey"


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


# ---- Day 63: GET endpoints ----
@app.route("/random")
def get_random_cafe():
    all_cafes = Cafe.query.all()
    if not all_cafes:
        return jsonify(error={"Not Found": "No cafes in the database yet."}), 404
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    matching_cafes = Cafe.query.filter_by(location=query_location).all()
    if matching_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in matching_cafes])
    return jsonify(error={"Not Found": "No cafes found at that location."}), 404


# ---- Day 64: POST endpoint ----
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


# ---- Day 65: PATCH endpoint ----
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "A cafe with that id was not found."}), 404
    cafe.coffee_price = request.args.get("new_price")
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200


# ---- Day 65: DELETE endpoint (API key required) ----
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error={"Forbidden": "That's not allowed. Missing/invalid API key."}), 403

    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "A cafe with that id was not found."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe."}), 200


if __name__ == "__main__":
    app.run(debug=True)
