import sqlite3
import os

# Create database folder
os.makedirs("database", exist_ok=True)

# Database location
DB_PATH = "database/wifi.db"

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Create cursor
cursor = conn.cursor()

# Create wifi table
cursor.execute("""
CREATE TABLE IF NOT EXISTS wifi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssid TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Save changes
conn.commit()

# Close database
conn.close()

print("Database created successfully!")