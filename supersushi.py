from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key = "YouDontNeedASecretKey!"
app.permanent_session_lifetime = timedelta(days=1)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes/")
def recipes():
    return render_template("recipes.html")

@app.route("//recipes/whatyouneed/")
def whatYouNeed():
    return render_template("whatyouneed.html")

@app.route("//recipes/californiaroll/")
def californiaroll():
    return render_template("californiaroll.html")

@app.route("//recipes/sushirice/")
def sushirice():
    return render_template("sushirice.html")

@app.route("/adminlogin/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["emailfield"]
        password = request.form["passwordfield"]
        session["user"] = user
        if user == "admin@admin.com" and password == "secret":
            return redirect(url_for("cmshome", usr=user))
        else:
            return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("cmshome"))
        return render_template("login.html")

@app.route("/logout/")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/cmshome/")
def cmshome():
    if "user" in session:
        user = session["user"]
        return render_template("cmshome.html", username=user)
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
