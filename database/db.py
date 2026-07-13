import sqlite3
import os

# Create database folder if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")


def create_database():

    connection = sqlite3.connect("database/history.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            email TEXT NOT NULL,

            prediction TEXT NOT NULL,

            confidence REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")