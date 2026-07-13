import sqlite3


def save_prediction(email, prediction, confidence):

    connection = sqlite3.connect("database/history.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO history
        (email, prediction, confidence)
        VALUES (?, ?, ?)
    """, (email, prediction, confidence))

    connection.commit()

    connection.close()