"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    assert extract() == "data/historical_projections.csv"


def test_query():
    assert query() == "Success"


def test_load():
    assert load() == "NBA_2015.db"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
