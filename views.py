from flask import Blueprint, render_template, redirect, url_for
views = Blueprint(__name__, "views", static_folder="static", template_folder="templates")

@views.route("/")
def home():
    return render_template("views.html", name="Mary")


@views.route("/profile/<username>")
def profile(username):
    return render_template("home.html", name=username)