import pandas as pd
import sqlite3
con = sqlite3.connect("reuters.db")
frequency = pd.read_sql("select * from Frequency",con)
book = frequency.groupby(by=["docid"])["count"].sum()
book = book[book > 300]
print book
