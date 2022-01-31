def write_to_excel(data, file_name, sheet_name):
    '''
    this function writes data into an excel file
    :param data: the data wanted in the excel file

    :param file_name: name of excel file to be written to
    :param sheet_name: name of sheet in excel file to be written to
    :return: the data into the excel file
    '''
    df = pd.DataFrame(data)
    flights = df.to_excel(file_name, sheet_name=sheet_name)
    return flights

def read_from_excel(file_name, sheet_name):
    '''
    this functions will read and display data from an excel file
    :param file_name: name of excel file to be written to
    :param sheet_name: name of sheet in excel file to be written to
    :return: data from excel file
    '''
    flights = pd.read_excel(file_name, sheet_name=sheet_name, index_col=0)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(flights)

def write_excel_sql():
    '''
    this fucntion will writed data in excel file into sql database
    :return: makes sql database containing excel data
    '''
    cxn = sqlite3.connect('flightdata.db')
    wb = pd.read_excel('FlightData.xlsx', sheet_name='Sheet1')
    wb.to_sql(name='flightdata', con=cxn, if_exists='replace', index=False)
    cxn.commit()
    cxn.close()
