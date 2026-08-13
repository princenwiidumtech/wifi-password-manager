from flask import Flask, render_template, request
from wifi_manager import save_wifi, view_wifi

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        ssid = request.form["ssid"]
        password = request.form["password"]

        save_wifi(ssid, password)

        return render_template("save.html")

    return render_template("save.html")


@app.route("/view")
def view():
    wifi_list = view_wifi()

    return render_template("view.html", wifi_list=wifi_list)


if __name__ == "__main__":
    app.run(debug=True)
