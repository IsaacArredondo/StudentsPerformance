import pandas as pd
from connection import engine

with engine.connect() as con:
    data = con.execute('SELECT * FROM students') 

for row in data:
    print(row)