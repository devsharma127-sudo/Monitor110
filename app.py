from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

def load_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    summary = load_json("summary.json")
    return render_template("dashboard.html", summary=summary)

@app.route("/news")
def news():
    data = load_json("analyzed_data.json")
    return render_template("news.html", news=data)

if __name__ == "__main__":
    app.run(debug=True)