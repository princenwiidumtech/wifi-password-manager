import sqlite3
import os
from encryption import encrypt_password, decrypt_password

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

DB_PATH = "database/wifi.db"


def save_wifi(ssid, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    encrypted_password = encrypt_password(password)

    cursor.execute(
        "INSERT INTO wifi (ssid, password) VALUES (?, ?)",
        (ssid, encrypted_password)
    )

    conn.commit()
    conn.close()

    print("Wi-Fi saved successfully!")


def view_wifi():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM wifi")
    rows = cursor.fetchall()

    conn.close()

    wifi_list = []

    for row in rows:
        wifi_id, ssid, encrypted_password = row
        password = decrypt_password(encrypted_password)

        wifi_list.append({
            "id": wifi_id,
            "ssid": ssid,
            "password": password
        })

    return wifi_list
