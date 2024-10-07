"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the NBA_2015 table"""
    conn = sqlite3.connect("NBA_2015.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NBA_2015")
    print("Top 5 rows of the NBA_2015 table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
