#!/usr/bin/python3
"""quiz app"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_login import LoginManager
from auth import auth_bp
from models import storage
from os import getenv

login_manager = LoginManager()

app = Flask(__name__)

CORS(app, resources=r"/*", origins="0.0.0.0")
login_manager.init_app(app)

app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return "Hello world"

@app.errorhandler(404)
def not_found_error(error):
    return jsonify(
        {
            "error": "Not found"
        }
    )

@app.teardown_appcontext
def teardown_app(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST"), port=getenv("HBNB_API_PORT"), threaded=True)