from flask import Flask

application = Flask(__name__)

@application.route("/")
def get_bikes():
    return 'bikes', 200