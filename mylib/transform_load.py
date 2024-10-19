"""
Transforms and Loads data into the databricks database

"""

import csv
import os
from databricks import sql
from dotenv import load_dotenv


def load(dataset="data/historical_projections.csv"):
    """Transforms and Loads data into the databricks database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS nba_2015 (Player STRING, 
                Position STRING, ID STRING, Draft_Year INT, 
                Projected_SPM FLOAT, Superstar FLOAT, Starter FLOAT, 
                Role_Player FLOAT, Bust FLOAT)"""
            )

            cursor.execute("SELECT * FROM nba_2015")
            result = cursor.fetchall()
            if not result:
                print("test")
                sql_str = "INSERT INTO nba_2015 VALUES"
                for i in payload:
                    sql_str += "\n" + str(tuple(i)) + ","
                sql_str = sql_str[:-1] + ";"
                print(sql_str)

                cursor.execute(sql_str)

            # cursor.executemany(
            #     "INSERT INTO nba_2015 VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?)",
            #     payload,
            # )

            # result = cursor.fetchall()

            # for row in result:
            #     print(row)

            cursor.close()
            connection.close()
    return "db loaded"


if __name__ == "__main__":
    load()
