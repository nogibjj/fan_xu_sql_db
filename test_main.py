"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import csv
import os
from databricks import sql
from dotenv import load_dotenv


def test_extract():
    """Test extract function"""
    extract_test = extract()
    assert extract_test == "data/historical_projections.csv"


def test_load():
    """tests load function"""
    load_test = load()
    assert load_test == "db loaded"


def test_query():
    """test query function"""
    query_test = query()
    assert query_test == "query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
