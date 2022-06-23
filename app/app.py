#!/usr/bin/python3
"""quiz app"""

from turtle import title
from flask import Flask, jsonify, render_template, url_for, redirect, flash
from flask_cors import CORS
from flask_login import LoginManager, login_required, logout_user
from .auth import auth_bp
from models import storage
from os import getenv
from models.user import User
# from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
# db = SQLAlchemy()

app = Flask(__name__)

CORS(app, resources=r"/*", origins="0.0.0.0")
app.config.from_pyfile('config.py')
login_manager.init_app(app)

app.register_blueprint(auth_bp)


@app.route("/")
def landing():
    return render_template(
        "landing.html",
        title="Quizera",
    )

@app.route("/dashboard")
@login_required
def home():
    return "I am really sorry couldn't get enough time to build a dashboard"

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.get(user_id=user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

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