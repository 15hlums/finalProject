import sys
from PyQt5 import QtWidgets, uic, QtCore
import sqlite3
import functions as f

# creates a database from excel file
database = sqlite3.connect('flightdata.db')
f.import_excel_to_database(database)

# this imports the designs from QT Designer
gui1 = uic.loadUiType('pyqt_design.ui')[0]
gui2 = uic.loadUiType('instructions_menu.ui')[0]
gui3 = uic.loadUiType('variables_menu.ui')[0]
gui4 = uic.loadUiType('amendflights_menu.ui')[0]
gui5 = uic.loadUiType('filterflights_menu.ui')[0]
gui6 = uic.loadUiType('addflights_menu.ui')[0]
gui7 = uic.loadUiType('deleteflights_menu.ui')[0]
gui8 = uic.loadUiType('delay_menu.ui')[0]
gui9 = uic.loadUiType('extendedturnaround_menu.ui')[0]
gui10 = uic.loadUiType('exturnover2_menu.ui')[0]
gui11 = uic.loadUiType('rescheduleflight_menu.ui')[0]

# this class creates the main schedule window
class ScheduleWindow(QtWidgets.QMainWindow, gui1):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set column width for table
        self.schedule_table.setColumnWidth(0,90)
        self.schedule_table.setColumnWidth(1, 90)
        self.schedule_table.setColumnWidth(2, 125)
        self.schedule_table.setColumnWidth(3, 125)
        self.schedule_table.setColumnWidth(4, 125)
        self.schedule_table.setColumnWidth(5, 125)
        self.schedule_table.setColumnWidth(6, 80)
        self.load_data()

        # sets classes
        self.instructions_menu = InstructionsWindow(self)
        self.variables_menu = VariablesWindow(self)
        self.amendflights_menu = AmendWindow(self)
        self.clearflights_menu = FilterWindow(self)

        # connects button to call function
        self.instructions_button.clicked.connect(self.instructions_connect)
        self.variables_button.clicked.connect(self.variables_connect)
        self.amend_button.clicked.connect(self.amend_connect)
        self.clear_button.clicked.connect(self.clear_connect)

    def instructions_connect(self):
        '''
        connects the instructions button click with opening the instructions menu
        :return: showing the instructions menu
        '''
        self.instructions_menu.show()

    def variables_connect(self):
        '''
        connects the variables button click with opening the variables menu
        :return: showing the variables menu
        '''
        self.variables_menu.show()

    def amend_connect(self):
        '''
        connects the amend flights button click with opening the amend flights menu
        :return: showing the amend flights menu
        '''
        self.amendflights_menu.show()

    def clear_connect(self):
        '''
        connects the clear flights button click with opening the clear flights menu
        :return: showing the clear flights menu
        '''
        self.clearflights_menu.show()

    def load_data(self):
        '''
        this loads the data from the database into the main GUI table
        :return: GUI which displays data from database
        '''
        # set cursor
        cur = database.cursor()
        sqlquery = 'SELECT * FROM flightdata LIMIT 100'

        # clear contents and set row count
        self.schedule_table.clearContents()
        self.schedule_table.setRowCount(100)

        # set to 0 so can loop
        tablerow = 0

        # call the database and put in rows for table widget
        for row in cur.execute(sqlquery):
            self.schedule_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.schedule_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.schedule_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.schedule_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.schedule_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.schedule_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.schedule_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))

            tablerow += 1

# this class creates the instructions window !!NOT DONE!!
class InstructionsWindow(QtWidgets.QMainWindow, gui2):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the variables window
class VariablesWindow(QtWidgets.QMainWindow, gui3):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # sets parent to Schedule Window class
        self.parent = parent

        # sets classes
        self.delay_menu = DelayFlightsWindow(self)
        self.extendedturnaround_menu = ExtendedTurnaroundWindow(self)

        # connects the buttons to the functions
        self.delay_button.clicked.connect(self.delay_connect)
        self.maintenance_button.clicked.connect(self.extendedturnaround_connect)

    def delay_connect(self):
        '''
        connects the delay flights button click with opening the delay flights menu
        :return: showing the delay flights menu
        '''
        self.delay_menu.show()

    def extendedturnaround_connect(self):
        '''
        connects the maintenance button click with opening the maintenance menu
        :return: showing the maintenance menu
        '''
        self.extendedturnaround_menu.show()

# this class creates the amend flights window
class AmendWindow(QtWidgets.QMainWindow, gui4):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent as Schedule Window class
        self.parent = parent

        # set classes
        self.addflights_menu = AddFlightsWindow(self)
        self.deleteflights_menu = DeleteFlightsWindow(self)

        # connects click buttons to the functions
        self.addflights_button.clicked.connect(self.addflights_connect)
        self.deleteflights_button.clicked.connect(self.deleteflights_connect)

    def addflights_connect(self):
        '''
        connects the add flights button click with opening the add flights menu
        :return: showing the add flights menu
        '''
        self.addflights_menu.show()

    def deleteflights_connect(self):
        '''
        connects the delete flights button click with opening the delete flights menu
        :return: showing the delete flights menu
        '''
        self.deleteflights_menu.show()

# this class creates the filter flights window
class FilterWindow(QtWidgets.QMainWindow, gui5):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent as Schedule Window class
        self.parent = parent

        # connect clicked buttons to functions
        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)
        self.resetbutton.clicked.connect(self.reset_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
        # this connects to the database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # gets the input text from the gui
        arrival = self.arrivaltime_input.text()
        departure = self.departuretime_input.text()
        prevdest = self.prevdest_input.text()
        nextdest = self.nextdest_input.text()
        gatenum = self.gatenum_input.text()

        # empty lists for data
        filter_list = []
        filter_names = []
        filter_data = []

        # if the arrival time input box has text
        if arrival != 'None':
            filter_list.clear()
            filter_list.append(arrival)
            filter_data.append(arrival)
            filter_names.append('arrival')

            filterarrival_query = '''
            SELECT *
            FROM flightdata
            WHERE "Arrival Time" LIKE (?) '''

            cursor.execute(filterarrival_query, filter_list)

        # if the departure time input box has text
        if departure != 'None':
            filter_list.clear()
            filter_list.append(departure)
            filter_data.append(departure)
            filter_names.append('departure')

            filterdeparture_query = '''
            SELECT *
            FROM flightdata
            WHERE "Departure Time" LIKE (?) '''

            cursor.execute(filterdeparture_query, filter_list)

        # if the previous destination input box has text
        if prevdest != 'None':
            filter_list.clear()
            filter_list.append(prevdest)
            filter_data.append(prevdest)
            filter_names.append('prevdest')

            filterprevdest_query = '''
            SELECT *
            FROM flightdata
            WHERE "Previous Destination" LIKE (?) '''

            cursor.execute(filterprevdest_query, filter_list)

        # if the next destination input box has text
        if nextdest != 'None':
            filter_list.clear()
            filter_list.append(nextdest)
            filter_data.append(nextdest)
            filter_names.append('nextdest')

            filternextdest_query = '''
            SELECT *
            FROM flightdata
            WHERE "Nest Destination" LIKE (?) '''

            cursor.execute(filternextdest_query, filter_list)

        # if the gate number input box has text
        if gatenum != 'None':
            filter_list.clear()
            filter_list.append(gatenum)
            filter_data.append(gatenum)
            filter_names.append('gatenum')

            filtergatenum_query = '''
            SELECT *
            FROM flightdata
            WHERE "Gate Number" LIKE (?) '''

            cursor.execute(filtergatenum_query, filter_list)

        # when there is nothing in the list (None is inputted for every box)
        if len(filter_names) == 0:
            None

        # when the first item in the list of filters is arrival time
        elif filter_names[0] == 'arrival':
            if len(filter_names) == 1:
                filter_delete_query = '''
                DELETE FROM flightdata
                WHERE "Arrival Time" NOT LIKE (?) '''
                cursor.execute(filter_delete_query, filter_data)
                self.parent.load_data()

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
                print(filter_data)
                print(filter_names)
                print(filter_list)
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

        # commits to database
        database_connect.commit()

        # loads function from parent to update gui
        self.parent.load_data()

        # closes the cursor
        cursor.close()

        # closes the database
        if database_connect:
            database_connect.close()

    def reset_connect(self):
        '''
        resets the database after filter function has been used
        :return: updated gui
        '''
        # connects to database
        database = sqlite3.connect('flightdata.db')

        # uses function from functions file to import excel data to database
        f.import_excel_to_database(database)

        # loads function from parent to update gui
        self.parent.load_data()

# this class creates the add flights window
class AddFlightsWindow(QtWidgets.QMainWindow, gui6):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parents as Amend Window class
        self.parent = parent

        # connects clicked buttons to functions
        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.prevflightnum_input.clear()
        self.nextflightnum_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
        # connects to database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # gets text from gui input boxes
        arrival = self.arrivaltime_input.text()
        departure = self.departuretime_input.text()
        prev_destination = self.prevdest_input.text()
        next_destination = self.nextdest_input.text()
        prev_flightnum = self.prevflightnum_input.text()
        next_flightnum = self.nextflightnum_input.text()
        gate_num = self.gatenum_input.text()

        # SQL statement to add flight to database
        data = (arrival, departure, prev_destination, next_destination, prev_flightnum, next_flightnum, gate_num)
        query = "INSERT INTO flightdata values(?,?,?,?,?,?,?)"
        cursor.execute(query, data)

        # commit to database
        database_connect.commit()

        # load function from parent of parent class to update gui
        self.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

# this class creates the delete flights window
class DeleteFlightsWindow(QtWidgets.QMainWindow, gui7):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent class as Amend Window class
        self.parent = parent

        # connect clicked buttons to function
        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the data in the gui buttons
        '''
        self.flightnum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then deletes the relevant row from the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
        # connect to database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # get text from gui input boxes
        arrival = self.arrivaltime_input.text()
        prev_flightnum = self.prevflightnum_input.text()

        # SQL statement to delete row from database
        data = (arrival, prev_flightnum)
        query = ''' 
        DELETE FROM flightdata 
        WHERE "Arrival Time" = (?) 
        AND "Previous Flight Number" = (?) '''
        cursor.execute(query, data)

        # commit to database
        database_connect.commit()

        # get function from parent of parent to load data to gui
        self.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

# this class creates the delay flights window !!GATE COLLISION AVOIDANCE NOT WORKING!!
class DelayFlightsWindow(QtWidgets.QMainWindow, gui8):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent class as Variables Window class
        self.parent = parent

        # connect clicked button to function
        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears data from the gui buttons
        '''
        self.flightnum_input.clear()
        self.arrivaltime_input.clear()
        self.delaytime_input.clear()

    def submit_connect(self):
        '''
        takes input from the gui buttons and changes the time from the relevant delay amount and updates database and
        gui with the new times and gate numbers
        :return: updated database and gui
        '''
        # connect to database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # get text from gui input boxes
        delay = self.delaytime_input.text()
        arrival_time = self.arrivaltime_input.text()
        flight_num = self.flightnum_input.text()

        # SQL statement gets the departure time from the table
        departure_query = '''
            SELECT "Departure Time"
            FROM flightdata
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        departure_data = (arrival_time, flight_num)
        cursor.execute(departure_query, departure_data)

        for row in cursor.execute(departure_query, departure_data):
            departure_time = (row[0])

        # SQL statement updates database with new arrival time with the delay
        arrival_query = '''
            UPDATE flightdata
            SET "Arrival Time" = (?)
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        arrival_data = (f.delay_changetime(delay, arrival_time), arrival_time, flight_num)
        cursor.execute(arrival_query, arrival_data)

        # SQL statement updates database with new departure time with the delay
        departure_update_query = '''
            UPDATE flightdata
            SET "Departure Time" = (?)
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        departure_update_data = (f.delay_changetime(delay, departure_time), f.delay_changetime(delay, arrival_time), flight_num)
        cursor.execute(departure_update_query, departure_update_data)

        # SQL statement gets the gate number of any flights that arrive at the same time
        gatenum_delay = '''
            SELECT "Gate Number"
            FROM flightdata
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        data_gatenum = (f.delay_changetime(delay, arrival_time), flight_num)
        cursor.execute(gatenum_delay, data_gatenum)

        # these are the gates available at the terminal
        gates = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5']

        # this compares and sees if a gate is available or not at the allocated time
        for row in cursor.execute(gatenum_delay, data_gatenum):
            if row:
                for i in range(0, len(gates)):
                    if gates[i] != row[0]:
                        # updates database with new gate number
                        updategates_query = '''
                            UPDATE flightdata
                            SET "Gate Number" = (?)
                            WHERE "Arrival Time" = (?)
                            AND "Previous Flight Number" = (?)'''
                        updategates_data = (gates[i], f.delay_changetime(delay, arrival_time), flight_num)
                        cursor.execute(updategates_query, updategates_data)

                        break
                    else:
                        None

        # commit to database
        database_connect.commit()

        # gets function from parent of parent to load data to gui
        self.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

# this class creates the extended turnarounds window
class ExtendedTurnaroundWindow(QtWidgets.QMainWindow, gui9):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent class as Variables Window class
        self.parent = parent

        # connect clicked button to function
        self.submitbutton.clicked.connect(self.submit_connect)
        self.clearbutton.clicked.connect(self.clear_connect)

    def clear_connect(self):
        '''
        this clears the buttons on the gui
        '''
        self.flightnum_input.clear()
        self.arrivaltime_input.clear()
        self.esttime_input.clear()

    def submit_connect(self):
        '''
        this takes input and chooses if less or more than 2 hours
        :return: either less than or more than 2 hour function
        '''
        # get text from gui input boxes
        estimated_time = self.esttime_input.text()

        # decides if input is more or less than 2 hours
        if float(estimated_time[1]) < 2.00 and float(estimated_time[1]) >= 0.00:
            self.less_2hours()
        elif float(estimated_time[1]) >= 2.00:
            self.more_2hours()
        else:
            None

    def less_2hours(self):
        '''
        when the extended turnaround is less than 2 hours, it will just delay the flight by the specified time
        :return: new times and gate numbers in the gui table
        '''
        # connects to database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # gets text from gui input boxes
        flight_num = self.flightnum_input.text()
        arrival_time = self.arrivaltime_input.text()
        estimated_time = self.esttime_input.text()

        # SQL statement gets the departure time from the table
        departure_query = '''
                    SELECT "Departure Time"
                    FROM flightdata
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''
        departure_data = (arrival_time, flight_num)
        cursor.execute(departure_query, departure_data)

        # get departure time for each row
        for row in cursor.execute(departure_query, departure_data):
            departure_time = (row[0])

        # SQl statement updates database with new arrival time with the delay
        arrival_query = '''
                    UPDATE flightdata
                    SET "Arrival Time" = (?)
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''
        arrival_data = (f.delay_changetime(estimated_time, arrival_time), arrival_time, flight_num)
        cursor.execute(arrival_query, arrival_data)

        # SQl statement updates database with new departure time with the delay
        departure_update_query = '''
                    UPDATE flightdata
                    SET "Departure Time" = (?)
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''
        departure_update_data = (
        f.delay_changetime(estimated_time, departure_time), f.delay_changetime(estimated_time, arrival_time), flight_num)
        cursor.execute(departure_update_query, departure_update_data)

        # SQl statement gets the gate number of any flights that arrive at the same time
        gatenum_delay = '''
                    SELECT "Gate Number"
                    FROM flightdata
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''

        data_gatenum = (f.delay_changetime(estimated_time, arrival_time), flight_num)
        cursor.execute(gatenum_delay, data_gatenum)

        # these are the gates available at the terminal
        gates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

        # this compares and sees if a gate is available or not at the allocated time
        for row in cursor.execute(gatenum_delay, data_gatenum):
            if row:
                for i in range(0, len(gates)):
                    if gates[i] != row[0]:
                        # updates database with new gate number
                        updategates_query = '''
                                    UPDATE flightdata
                                    SET "Gate Number" = (?)
                                    WHERE "Arrival Time" = (?)
                                    AND "Previous Flight Number" = (?)'''
                        updategates_data = (gates[i], f.delay_changetime(estimated_time, arrival_time), flight_num)
                        cursor.execute(updategates_query, updategates_data)

                        break
                    else:
                        None

        # commit to database
        database_connect.commit()

        # get function from parent of parent to load data to gui
        self.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

    def more_2hours(self):
        '''
        opens a new window which gives the user two options to either cancel or reschedule the flight as the extended
        turnaround is too long
        :return: opens exturnover2 window
        '''
        # connects to another menu as it is over 2 hours
        self.exturnover2_menu = ExtendedTurnaroundOverTwoWindow(self)
        self.exturnover2_menu.show()

# this class creates a window when the extended turnarounds is equal to or greater than 2 hours
class ExtendedTurnaroundOverTwoWindow(QtWidgets.QMainWindow, gui10):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent class as Extended Turnaround Window class
        self.parent = parent

        # connect clicked button to function
        self.submitbutton.clicked.connect(self.submit_connect)

    def submit_connect(self):
        '''
        waits for user input if they choose to cancel or reschedule flight
        :return: new gui menu
        '''
        # checks which radio button the user has chosen
        if self.cancelbutton.isChecked() == True:
            self.cancel_connect()
        elif self.reschedulebutton.isChecked() == True:
            self.reschedule_connect()
        else:
            None

    def cancel_connect(self):
        '''
        this cancels the flight when the extended turnaround is over 2 hours
        :return: updated gui table
        '''
        #  connects database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # gets text from gui input
        flight_num = self.parent.flightnum_input.text()
        arrival_time = self.parent.arrivaltime_input.text()

        # SQL statement to delete row from database
        cancel_data = (arrival_time, flight_num)
        cancel_query = ''' 
        DELETE FROM flightdata 
        WHERE "Arrival Time" = (?) 
        AND "Previous Flight Number" = (?) '''
        cursor.execute(cancel_query, cancel_data)

        # commit database
        database_connect.commit()

        # get function from parent of parent to load data to gui
        self.parent.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

    def reschedule_connect(self):
        '''
        this reschedules the flight (adds new flight)
        :return: updated gui table
        '''
        # connects to Reschedule Flight Window class
        self.rescheduleflight_menu = RescheduleFlightWindow(self)
        self.rescheduleflight_menu.show()

# this class creates a window when user wants to reschedule a flight when the ex. turnaround is greater/equal to 2 hours
class RescheduleFlightWindow(QtWidgets.QMainWindow, gui11):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set parent as Extended Turnaround Over Two Window class
        self.parent = parent

        # connect clicked buttons to functions
        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.prevflightnum_input.clear()
        self.nextflightnum_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
        # connect to database
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        # get text from gui input boxes
        arrival = self.arrivaltime_input.text()
        departure = self.departuretime_input.text()
        prev_destination = self.prevdest_input.text()
        next_destination = self.nextdest_input.text()
        prev_flightnum = self.prevflightnum_input.text()
        next_flightnum = self.nextflightnum_input.text()
        gate_num = self.gatenum_input.text()

        # SQL statement to add flight to database
        data = (arrival, departure, prev_destination, next_destination, prev_flightnum, next_flightnum, gate_num)
        query = "INSERT INTO flightdata values(?,?,?,?,?,?,?)"
        cursor.execute(query, data)

        # commit to database
        database_connect.commit()

        # get function from parent of parent to load data
        self.parent.parent.load_data()

        # close cursor
        cursor.close()

        # close database
        if database_connect:
            database_connect.close()

# this function creates objects from the class that opens the main window
def main():
    # this resizes the window to fit with it's contents
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    # opens main window
    app = QtWidgets.QApplication(sys.argv)
    main_window = ScheduleWindow()
    main_window.show()
    app.exec_()

# opens main
if __name__ == '__main__':
    main()