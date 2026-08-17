from flask import Flask, render_template, request, redirect
from wifi_manager import save_wifi, view_wifi, delete_wifi, update_wifi
import splite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        ssid = request.form.get("ssid")
        password = request.form.get("password")

        save_wifi(ssid, password)

        return """
        <h1>Wi-Fi Saved Successfully!</h1>
        <p>Your Wi-Fi has been saved.</p>

        <a href="/save">Save Another Wi-Fi</a>
        <br><br>
        <a href="/view">View Saved Wi-Fi</a>
        <br><br>
        <a href="/">Back Home</a>
        """

    return render_template("save.html")

@app.route("/view")
def view():
    wifi_list = view_wifi()

    return render_template("view.html", wifi_list=wifi_list)

@app.route("/delete/<int:wifi_id>")
def delete(wifi_id):
    delete_wifi(wifi_id)

    return redirect("/view")

@app.route("/edit/<int:wifi_id>")
def edit(wifi_id):
    conn = sqlite3.connect("database/wifi.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, ssid FROM wifi WHERE id = ?",
        (wifi_id,)
    )

    wifi = cursor.fetchone()

    conn.close()

    return render_template("edit.html", wifi=wifi)
@app.route("/update/<int:wifi_id>", methods=["POST"])
def update(wifi_id):
    ssid = request.form["ssid"]
    password = request.form["password"]

    update_wifi(wifi_id, ssid, password)

    return redirect("/view")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
