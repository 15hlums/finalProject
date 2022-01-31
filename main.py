import pandas as pd

bob = pd.ExcelFile('FlightData.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
x=[]
x.append(bob['Arrival'])
print(x)
