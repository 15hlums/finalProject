import pandas as pd
import sqlite3

# changes the arrival time with respect to the delay
def delay_changetime(delay, arrival_time):
    t = delay
    (m, s) = t.split(':')
    num = int(m) * 60 + int(s)
    current_time = arrival_time
    current_min = (current_time[3] + current_time[4])
    current_hour = (current_time[0] + current_time[1])
    added_hour = 0

    # if the minutes plus the delay time is less than an hour
    if (int(current_min) + int(num)) < 60:
        final_min = str(int(current_min) + int(num))
        if len(final_min) == 1:
            final_time = (current_time[0] + current_time[1] + current_time[2] + '0' + final_min[0])
            return final_time
        else:
            final_time = (current_time[0] + current_time[1] + current_time[2] + final_min[0] + final_min[1])
            return final_time

    # if the minutes plus the delay time is larger than an hour (carries over to next hour)
    elif (int(current_min) + int(num)) > 60:
        # if the hour is 23:00
        if int(current_hour) == 23:
            final_min = str((int(current_min) + int(num)) - 60)
            final_hour = '0'
            if len(final_min) == 1:
                final_time = (final_hour[0] + final_hour[0] + current_time[2] + '0' + final_min[0])
                return final_time
            else:
                final_time = (final_hour[0] + final_hour[0] + current_time[2] + final_min[0] + final_min[1])
                return final_time

        # if the hour is not 23:00
        else:
            # if the hour is less than 09:00
            if int(current_hour) < 9:
                final_min = str(int(current_min) + int(num))
                while int(final_min) >= 60:
                    final_min = str(int(final_min) - 60)
                    added_hour += 1
                final_hour = str(int(current_hour[0] + current_hour[1]) + added_hour)
                if len(final_min) == 1:
                    final_time = ('0' + str(final_hour[0] + current_time[2] + '0' + final_min[0]))
                    return final_time
                else:
                    final_time = ('0' + str(final_hour[0] + current_time[2] + final_min[0] + final_min[1]))
                    return final_time

            # if the hour is or greater than 09:00
            else:
                final_min = str(int(current_min) + int(num))
                while int(final_min) >= 60:
                    final_min = str(int(final_min) - 60)
                    added_hour += 1
                final_hour = str(int(current_hour[0] + current_hour[1]) + added_hour)
                if len(final_min) == 1:
                    if len(final_hour) == 1:
                        final_time = (str(final_hour[0] + '0' + current_time[2] + '0' + final_min[0]))
                        return final_time
                    else:
                        final_time = (str(final_hour[0] + final_hour[1] + current_time[2] + '0' + final_min[0]))
                        return final_time
                else:
                    if len(final_hour) == 1:
                        final_time = (str(final_hour[0] + '0' + current_time[2] + final_min[0] + final_min[1]))
                        return final_time
                    else:
                        final_time = (
                            str(final_hour[0] + final_hour[1] + current_time[2] + final_min[0] + final_min[1]))
                        return final_time


    # if the minutes plus the delay time is exactly an hour
    elif (int(current_min) + int(num)) == 60:
        # if the hour is 23:00
        if int(current_hour) == 23:
            final_hour = '0'
            final_time = (final_hour[0] + final_hour[0] + current_time[2] + final_hour[0] + final_hour[0])
            return final_time

        # if the hour is not 23:00
        else:
            # the hour is less than 09:00
            if int(current_hour) < 9:
                final_min = str((int(current_min) + int(num)) - 60)
                final_hour = str(int(current_hour) + 1)
                final_time = ('0' + str(final_hour[0] + current_time[2] + final_min[0] + final_min[0]))
                return final_time

            # if the hour is or greater than 09:00
            else:
                final_min = str((int(current_min) + int(num)) - 60)
                final_hour = str(int(current_hour) + 1)
                final_time = (str(final_hour[0] + final_hour[1] + current_time[2] + final_min[0] + final_min[0]))
                return final_time

# imports the data from the excel file into the database
def import_excel_to_database(database):
    '''
    this imports the data from excel into a database
    :param database: the database the excel data will be imported into
    :return: database with excel data in
    '''
    excel_read = pd.read_excel('FlightData.xlsx', sheet_name='Sheet1', index_col=0)
    excel_read.to_sql(name='flightdata', con=database, if_exists='replace', index=0)
    database.commit()

# finds the rows needed to be deleted when filter is submitted
def filter_deleterows(filter_names, filter_data):
    '''
    this finds the rows that do not fit the filter requirements and deletes them from the table
    :param filter_names: the names of the colums where filter data has been inputted
    :param filter_data: the data which needs to be filtered in the table
    :return: sql statement updating the database
    '''
    database_connect = sqlite3.connect('flightdata.db')
    cursor = database_connect.cursor()

    # when the first item in the list of filters is arrival time
    if filter_names[0] == 'arrival':
        if len(filter_names) == 1:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Arrival Time" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

            for row in cursor.execute(filter_delete_query, filter_data):
                print(row)

        elif len(filter_names) == 2:
            # when the second item in the list is ...
            if filter_names[1] == 'departure':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Arrival Time" NOT LIKE (?) 
                AND "Departure Time" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'prevdest':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Arrival Time" NOT LIKE (?) 
                AND "Previous Destination" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'nextdest':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Arrival Time" NOT LIKE (?) 
                AND "Next Destination" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'gatenum':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Arrival Time" NOT LIKE (?)
                AND "Gate Number" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            else:
                print('error')

        elif len(filter_names) == 3:
            # when the second item in the list is departure
            if filter_names[1] == 'departure':
                # and when the third item in the list is ...
                if filter_names[2] == 'prevdest':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Departure Time" NOT LIKE (?)
                    AND "Previous Destination" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                elif filter_names[2] == 'nextdest':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Departure Time" NOT LIKE (?)
                    AND "Next Destination" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                elif filter_names[2] == 'gatenum':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Departure Time" NOT LIKE (?)
                    AND "Gate Number" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                else:
                    print('error')
            # when the second item in the list is previous destination
            elif filter_names[1] == 'prevdest':
                # and when the third item in the list is ...
                if filter_names[2] == 'nextdest':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Previous Destination" NOT LIKE (?)
                    AND "Next Destination" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                elif filter_names[2] == 'gatenum':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Previous Destination" NOT LIKE (?)
                    AND "Gate Number" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                else:
                    print('error')
            # when the second item in the list is next destination
            elif filter_names[1] == 'nextdest':
                # and when the third item in the list is ...
                if filter_names[2] == 'gatenum':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Arrival Time" NOT LIKE (?)
                    AND "Next Destination" NOT LIKE (?)
                    AND "Gate Number" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
            else:
                print('error')

        elif len(filter_names) == 4:
            # when the second item in the list is departure
            if filter_names[1] == 'departure':
                # and when the third item in the list is previous destination
                if filter_names[2] == 'prevdest':
                    # and when the fourth item in the list is ...
                    if filter_names[3] == 'nextdest':
                        filter_delete_query = '''
                        DELETE FROM flightdata
                        WHERE "Arrival Time" NOT LIKE (?)
                        AND "Departure Time" NOT LIKE (?)
                        AND "Previous Destination" NOT LIKE (?)
                        AND "Next Destination" NOT LIKE (?) '''
                        cursor.execute(filter_delete_query, filter_data)
                    elif filter_names[3] == 'gatenum':
                        filter_delete_query = '''
                        DELETE FROM flightdata
                        WHERE "Arrival Time" NOT LIKE (?)
                        AND "Departure Time" NOT LIKE (?)
                        AND "Previous Destination" NOT LIKE (?)
                        AND "Gate Number" NOT LIKE (?) '''
                        cursor.execute(filter_delete_query, filter_data)
                    else:
                        print('error')
                # when the third item in the list is next destination
                elif filter_names[2] == 'nextdest':
                    # and when the fourth item in the list is ...
                    if filter_names[3] == 'gatenum':
                        filter_delete_query = '''
                        DELETE FROM flightdata
                        WHERE "Arrival Time" NOT LIKE (?)
                        AND "Departure Time" NOT LIKE (?)
                        AND "Next Destination" NOT LIKE (?)
                        AND "Gate Numner" NOT LIKE (?) '''
                        cursor.execute(filter_delete_query, filter_data)
                    else:
                        print('error')
            # when the second item in the list is previous destination
            elif filter_names[1] == 'prevdest':
                # and when the third item in the list is next destination
                if filter_names[2] == 'nextdest':
                    # and when the fourth item in the list is ...
                    if filter_names[3] == 'gatenum':
                        filter_delete_query = '''
                        DELETE FROM flightdata
                        WHERE "Arrival Time" NOT LIKE (?)
                        AND "Previous Destination" NOT LIKE (?)
                        AND "Next Destination" NOT LIKE (?)
                        AND "Gate Number" NOT LIKE (?) '''
                        cursor.execute(filter_delete_query, filter_data)
                    else:
                        print('error')
                else:
                    print('error')
            else:
                print('error')

        elif len(filter_names) == 5:
            # when all items are in the list
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Arrival Time" NOT LIKE (?)
            AND "Departure Time" NOT LIKE (?)
            AND "Previous Destination" NOT LIKE (?)
            AND "Next Destination" NOT LIKE (?)
            AND "Gate Number" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        else:
            print('error')

    # when the first item in the list of filters is departure time
    elif filter_names[0] == 'departure':
        if len(filter_names) == 1:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Departure Time" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        elif len(filter_names) == 2:
            # when the second item in the list is ...
            if filter_names[1] == 'prevdest':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Departure Time" NOT LIKE (?)
                AND "Previous Destination" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'nextdest':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Departure Time" NOT LIKE (?)
                AND "Next Destination" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'gatenum':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Departure Time" NOT LIKE (?)
                AND "Gate Number" NOT LIKE (?)'''
                cursor.execute(filter_delete_query, filter_data)
            else:
                print('error')

        elif len(filter_names) == 3:
            # when the second item in the list is previous destination
            if filter_names[1] == 'prevdest':
                # and when the third item in the list is ...
                if filter_names[2] == 'nextdest':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Departure Time" NOT LIKE (?)
                    AND "Previous Destination" NOT LIKE (?)
                    AND "Next Destination" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                elif filter_names[2] == 'gatenum':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Departure Time" NOT LIKE (?)
                    AND "Previous Destination" NOT LIKE (?)
                    AND "Gate Number" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                else:
                    print('error')
            # when the second item in the list is next destination
            elif filter_names[1] == 'nextdest':
                # and when the third item in the list is ...
                if filter_names[2] == 'gatenum':
                    filter_delete_query = '''
                    DELETE FROM flightdata
                    WHERE "Departure Time" NOT LIKE (?)
                    AND "Next Destination" NOT LIKE (?)
                    AND "Gate Number" NOT LIKE (?) '''
                    cursor.execute(filter_delete_query, filter_data)
                else:
                    print('error')
            else:
                print('error')

        elif len(filter_names) == 4:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Departure Time" NOT LIKE (?)
            AND "Previous Destination" NOT LIKE (?)
            AND "Next Destination" NOT LIKE (?)
            AND "Gate Number" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        else:
            print('error')

    # when the first item in the list of filters is previous destination
    elif filter_names[0] == 'prevdest':
        if len(filter_names) == 1:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Previous Destination" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        elif len(filter_names) == 2:
            # when the second item in the list is ...
            if filter_names[1] == 'nextdest':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Previous Destination" NOT LIKE (?)
                AND "Next Destination" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            elif filter_names[1] == 'gatenum':
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Previous Destination" NOT LIKE (?)
                AND "Gate Number" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
            else:
                print('error')

        elif len(filter_names) == 3:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Previous Destination" NOT LIKE (?)
            AND "Next Destination" NOT LIKE (?)
            AND "Gate Number" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        else:
            print('error')

    # when the first item in the list of filters is next destination
    elif filter_names[0] == 'nextdest':
        if len(filter_names) == 1:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Next Destination" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        elif len(filter_names) == 2:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Next Destination" NOT LIKE (?)
            AND "Gate Number" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        else:
            print('error')

    # when the first item in the list of filters is gate number
    elif filter_names[0] == 'gatenum':
        if len(filter_names) == 1:
            filter_delete_query = '''
            DELETE FROM flightdata
            WHERE "Gate Number" NOT LIKE (?) '''
            cursor.execute(filter_delete_query, filter_data)

        else:
            print('error')