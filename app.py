from flask import Flask, render_template, request
from wifi_manager import save_wifi

app = Flask(__name__)


@app.route("/")
def home():
    return "Wi-Fi Password Manager is running!"


@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        ssid = request.form["ssid"]
        password = request.form["password"]

        save_wifi(ssid, password)

        return "Wi-Fi saved successfully!"

    return render_template("save.html")


if __name__ == "__main__":
    app.run(debug=True)