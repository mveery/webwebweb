from flask import Flask, redirect, url_for, render_template
from progress import progress
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(progress, url_prefix="/progress")
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)

