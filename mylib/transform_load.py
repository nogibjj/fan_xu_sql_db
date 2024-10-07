"""
Transforms and Loads data into the local SQLite3 database

"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/fan_xu_sql_assn/data/historical_projections.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("NBA_2015.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS NBA_2015")
    c.execute(
        """CREATE TABLE NBA_2015 (Player,Position,ID,Draft Year,
        Projected SPM,Superstar,Starter,Role Player,Bust)"""
    )
    # insert
    c.executemany("INSERT INTO NBA_2015 VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "NBA_2015.db"
