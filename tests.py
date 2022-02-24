import pandas as pd

def test_check_exceldataframe(func, column_name):
  try:
    assert func(column_name) == True
  except:
    print('columns do not match')

def check_excel_dataframe(column_name):
    '''
    this function will test that the data in the column name written and the excel file in the column name in the dataframe match
    :param column_name: column name in both file
    :return: True or False
    '''
    dataframe_check = []
    excel_check = []
    exceldf = pd.read_excel('FlightData.xlsx', index_col=0) # turns excel into dataframe
    excel_column = exceldf[column_name]
    table_column = df[column_name]
    dataframe_data = table_column.values  # this gets values from dataframe and excel dataframe
    excel_data = excel_column.values
    for x in range(0, len(dataframe_data)):
        dataframe_check.append(dataframe_data[x]) # appends both to lists so can compare
    for x in range(0, len(excel_data)):
        excel_check.append(excel_data[x])
    if dataframe_check == excel_check: # this checks if the values are the same
        return True
    else:
        return False

def test_check_excelsql(func, column_name):
    try:
        assert func(column_name) == True
    except:
        print('columns do not match')

def check_excel_sql(column_name):
    '''
    this function will check that the data in the excel file is the same as in the sql database
    :param column_name: name of the column
    :return: true or false
    '''
    sql_data = []
    sql_check = []
    dataframe_check = []
    for column in cursor.execute('SELECT Arrival FROM flightdata'):
        sql = (column[0])
        sql_data.append(sql)
    table_column = df[column_name]
    dataframe_data = table_column.values
    for x in range(0, len(dataframe_data)):
        dataframe_check.append(dataframe_data[x])  # appends both to lists so can compare
    for x in range(0, len(sql_data)):
        sql_check.append(sql_data[x])
    if dataframe_check == sql_check:  # this checks if the values are the same
        return True
    else:
        return False