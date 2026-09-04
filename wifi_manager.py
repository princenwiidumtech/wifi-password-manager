import sqlite3
import os
from encryption import encrypt_password, decrypt_password
from werkzeug.security import generate_password_hash, check_password_hash

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

DB_PATH = "database/wifi.db"

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS wifi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssid TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

    conn.commit()
    conn.close()

init_database()

def save_wifi(ssid, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    encrypted_password = encrypt_password(password)

    cursor.execute(
        "INSERT INTO wifi (ssid, password) VALUES (?, ?)",
        (ssid, encrypted_password)
    )

    conn.commit()

    print("Saved:", ssid)
    print("Rows in database:", cursor.rowcount)

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

def delete_wifi(wifi_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM wifi WHERE id = ?",
        (wifi_id,)
    )

    conn.commit()
    conn.close()

    print("Wi-Fi deleted successfully!")

def update_wifi(wifi_id, ssid, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    encrypted_password = encrypt_password(password)

    cursor.execute(
        "UPDATE wifi SET ssid = ?, password = ? WHERE id = ?",
        (ssid, encrypted_password, wifi_id)
    )

    conn.commit()
    conn.close()

    print("Wi-Fi updated successfully!")

def create_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()
