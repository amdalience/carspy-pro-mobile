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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
