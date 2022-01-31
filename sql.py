import sqlite3
import pandas as pd

database = sqlite3.connect('flightdata.db')
excel_read = pd.read_excel('FlightData.xlsx', sheet_name='Sheet1', index_col=0)
excel_read.to_sql(name='flightdata', con=database, if_exists='replace', index=0)
database.commit()

cursor = database.cursor()
for row in cursor.execute('SELECT * FROM flightdata WHERE Arrival="09:00"'):
        print(row)