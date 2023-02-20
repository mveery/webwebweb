from flask import Flask, redirect, url_for, render_template
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)

