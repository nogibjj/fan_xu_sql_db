"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create, read, update, delete

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# create
print("Creating data...")
create()

# read
print("Reading data...")
read()

# update
print("Updating data...")
update()

# delete
print("Deleting data...")
delete()
