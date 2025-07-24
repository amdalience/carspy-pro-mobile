from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CarSpy backend en ligne 🚗"})

@app.route("/api/vehicules-populaires")
def popular_vehicles():
    data = [
        {"nom": "Clio 5", "type": "citadine", "locations": 128},
        {"nom": "Peugeot 3008", "type": "SUV", "locations": 93},
        {"nom": "Tesla Model 3", "type": "électrique", "locations": 74}
    ]
    return jsonify(data)
