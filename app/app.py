from flask import Flask
import json
from app import bikes

app = Flask(__name__)


@app.route("/bikes/stdev")
def get_bikes_stdev():
    stdev = bikes.stdev()
    return json.dumps(stdev)
