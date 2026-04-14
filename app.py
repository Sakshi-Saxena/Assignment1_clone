import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Path to the backend data file
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def read_data():
    """Read and return data from the JSON file."""
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@app.route("/api", methods=["GET"])
def get_data():
    """Return the full list from the data file as JSON."""
    data = read_data()
    return jsonify(data)


@app.route("/")
def index():
    return (
        "<h2>Flask API</h2>"
        "<p>Visit <a href='/api'>/api</a> to get the JSON data.</p>"
    )


if __name__ == "__main__":
    app.run(debug=True)