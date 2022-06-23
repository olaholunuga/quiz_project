#!/usr/bin/python3
"""authentication views"""
from flask import Blueprint, jsonify, abort, render_template, request, flash, session, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from models import storage
from models.user import User
from .forms import SignupForm, LoginForm

auth_bp = Blueprint(name="auth_bp", url_prefix="/auth", template_folder="templates", static_folder="static", import_name="__name__")

from .app import login_manager

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.get(email=form.email.data)
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
                website=form.website.data,
                password=form.password.data
            )
            user.save()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('home'))
        flash('A user already exists with that email address.')
        return redirect(url_for('auth_bp.signup_page'))
    return render_template(
        'signup.jinja2',
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.get(email=form.email.data)
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))
    return render_template(
        'login.jinja2',
        form=form,
        title='Log in.',
        template='login-page',
        body="Log in with your User account."
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

@auth_bp.route("/hello")
def say_hello():
    return jsonify({"msg": "hello_world"})