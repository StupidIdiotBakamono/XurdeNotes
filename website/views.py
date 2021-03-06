from flask import Blueprint, render_template, redirect, flash
from . import open_settings
from flask_login import login_required, current_user

# views blueprint
views = Blueprint(name="views", import_name=__name__)

# opening settings
settings = open_settings()

# Home page
@views.route("/")
def home():
    return render_template("index.html", settings=settings, user=current_user)