"""Query the database"""

import sqlite3


def create():
    """Create a fake data"""
    conn = sqlite3.connect("NBA_2015.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO NBA_2015 VALUES "
        "(Lebron James,SF,lebron-james,2003,100,100,100,100,100)"
    )
    conn.commit()
    conn.close()
    return "Sucessfully created!"


def read():
    """Read and print the database for all the rows of the table"""
    conn = sqlite3.connect("NBA_2015.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NBA_2015")
    print(cursor.fetchall())
    conn.close()
    return "Successfully read!"


def update():
    """Update bust status if bust percentage above 50%"""
    conn = sqlite3.connect("NBA_2015.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE NBA_2015 SET Bust = 'LOSER' WHERE Bust > '0.5';")
    conn.commit()
    conn.close()
    return "Successfully updated!"


def delete():
    """Delete all rows where position is center"""
    conn = sqlite3.connect("NBA_2015.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM NBA_2015 WHERE Position = 'C';")
    conn.commit()
    conn.close()
    return "Sucessfully deleted!"


if __name__ == "__main__":
    create()
    read()
    update()
    delete()
