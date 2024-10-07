"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_query():
    assert query() == "Success"


def test_load():
    assert load() == "NBA_2015.db"


if __name__ == "__main__":
    test_load()
    test_query()
