"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="""https://github.com/fivethirtyeight/data/raw
    /refs/heads/master/nba-draft-2015/historical_projections.csv""",
    file_path="data/historical_projections.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
