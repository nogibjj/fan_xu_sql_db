"""Query the database"""

import os
from databricks import sql
from dotenv import load_dotenv

full_query = """
WITH bust_chance AS (
  SELECT Position,
  AVG(Bust) AS bust_avg,
  COUNT(Position) AS position_count
  FROM default.nba_2015
  GROUP BY Position
)

SELECT * FROM nba_2015
JOIN bust_chance 
ON nba_2015.Position = bust_chance.Position
ORDER BY bust_chance.bust_avg DESC;
"""


# load the csv file and insert into a new sqlite3 database
def query():
    """Query the databricks database"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(full_query)
            result = cursor.fetchall()

            for row in result:
                print(row)
            cursor.close()
            connection.close()
    return "query successful"


if __name__ == "__main__":
    query()
