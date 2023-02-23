from flask import Blueprint, render_template, redirect, url_for
progress = Blueprint(__name__, "progress", static_folder="static", template_folder="templates")

@progress.route("/")
def home():
    return render_template("progress.html")


@progress.route("/activities")
def activities():
    return render_template("activities.html")

@progress.route("/academics")
def academics():
    return render_template("academics.html")

@progress.route("/upcoming")
def upcoming():
    return render_template("upcoming.html")

@progress.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")