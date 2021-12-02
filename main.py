import pandas as pd

data = {'Arrival': ['09:00', '09:05', '09:10', '09:15', '09:20'],
        'Previous Desitination': ['Tokyo Haneda Airport HND', 'Los Angeles International Airport LAX',
                                  'Mexico City International Airport MEX', 'John F. Kennedy International Airport JFK',
                                  'Frankfurt Airport FRA'],
        'Departure': ['09:30', '09:35', '09:40', '09:45', '09:50'],
        'Next Desitination': ['Dubai International Airport DXB', 'Hong Kong International Airport HKG',
                                  'Indira Gandhi International Airport DEL', 'Madrid Barajas Airport MAD',
                                  'Sydney Kingsford-Smith Airport SYD']
        }

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

table = df.to_string


print (table(index = False))