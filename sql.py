import sqlite3
import pandas as pd

database = sqlite3.connect('flightdata.db')
def import_excel_to_database(database):
        excel_read = pd.read_excel('FlightData.xlsx', sheet_name='Sheet1', index_col=0)
        excel_read.to_sql(name='flightdata', con=database, if_exists='replace', index=0)
        database.commit()

import_excel_to_database(database)
cursor = database.cursor()


for row in cursor.execute('SELECT * FROM flightdata'):
        print(row)
