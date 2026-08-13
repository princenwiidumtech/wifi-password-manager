import sqlite3
from encryption import encrypt_password, decrypt_password

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

    if not rows:
        print("No Wi-Fi password saved.")
        return

    for row in rows:
        wifi_id, ssid, encrypted_password = row

        password = decrypt_password(encrypted_password)

        print(f"ID: {wifi_id}")
        print(f"SSID: {ssid}")
        print(f"Password: {password}")
        print("-" * 30)