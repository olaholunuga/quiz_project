#!/usr/bin/python3
"""authentication views"""
from flask import Blueprint, jsonify, abort, render_template, request, flash, session, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from models import storage
from models.user import User
from .forms import SignupForm, LoginForm

auth_bp = Blueprint(name="auth_bp", url_prefix="/auth", template_folder="templates", static_folder="static", import_name="__name__")