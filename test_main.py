"""
Test goes here

"""

import main


def test_query():
    assert main.query() == "Success"


def test_load():
    assert main.load() == "NBA_2015.db"
