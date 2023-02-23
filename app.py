from flask import Flask, redirect, url_for, render_template
from views import views
from datetime import timedelta

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)

